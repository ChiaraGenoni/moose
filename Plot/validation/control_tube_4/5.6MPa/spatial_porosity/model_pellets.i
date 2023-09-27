viscosity =  0.0000179
T = 300
advected_interp_method = 'upwind'
velocity_interp_method = 'rc'
outlet_pressure = 101325
epsilon = 0.05
const = 1e-8

pp1 = 0.09
pp2 = 0.91

pellet_radius = 0.00397
cladding_radius = 0.0041656
porosity_gap = 1

height_stack = 0.03176
height_plenum = 0.01

[Mesh]
   uniform_refine = 1
  [gen]
    type = GeneratedMeshGenerator
    dim = 2
    xmin = 0
    xmax = ${pellet_radius}
    ymin = 0
    ymax = ${height_stack}
    nx = 10
    ny = 30
    bias_x = 1.0
    bias_y = 1.0
  []
  coord_type = 'RZ'
  rz_coord_axis = 'Y'
[]

[GlobalParams]
  rhie_chow_user_object = 'rc'
  fp = air 
[]


[FluidProperties]
  [air]
    type = IdealGasFluidProperties
  []
[]

[UserObjects]
  [rc]
    type = INSFVRhieChowInterpolator
    u = superficial_vel_x
    v = superficial_vel_y
    pressure = pressure
  []
[]

[Variables]
  [superficial_vel_x]
    type = PINSFVSuperficialVelocityVariable
    initial_condition = 1e-7
  []
  [superficial_vel_y]
    type = PINSFVSuperficialVelocityVariable
    initial_condition = 1e-7
  []
  [pressure]
    type = INSFVPressureVariable
    initial_condition = ${initial_pressure}
    # scaling = 1e-3
  []
[]

[AuxVariables]
  [velocity_norm]
    type = MooseVariableFVReal
  []
  [porosity_var]
    type = MooseVariableFVReal
  []
  [viscosity_var]
  type = MooseVariableFVReal
  []
[]

[AuxKernels]
  [porosity_aux_kernel]
    type = FunctionAux
    variable = porosity_var
    function = porosity_distribution
  []
  [viscosity_aux_kernel]
    type = FunctorElementalAux
    functor = mu
    variable = viscosity_var
  []
  [speed]
    type = VectorMagnitudeAux
    variable = 'velocity_norm'
    x = superficial_vel_x
    y = superficial_vel_y
  []
[]

[Materials]
  [drho_dt]
    type = GeneralFunctorFluidProps
    fp = air
    pressure = pressure
    T_fluid = ${T} 
    characteristic_length = 1
    porosity = porosity_var
    speed = 'velocity_norm'
  []
  [friction_factor_material]
    type = FrictionFactorFromMuMaterial
    mu = mu 
    porosity = porosity_distribution
    c_x = 1e-8
    c_y = 1e-8 
    c_z = 1e-8
  []
[]




[FVKernels]
  [mass_time]
    type = WCNSFVMassTimeDerivative
    variable = pressure
    drho_dt = drho_dt
  []
  [mass]
    type = INSFVMassAdvection
    variable = pressure
    advected_interp_method = ${advected_interp_method}
    velocity_interp_method = ${velocity_interp_method}
    rho = rho
    []

  [u_time]
    type = WCNSFVMomentumTimeDerivative
    variable = superficial_vel_x
    drho_dt = drho_dt
    rho = rho
    momentum_component = 'x'
  []
  [u_advection]
    type = PINSFVMomentumAdvection
    variable = superficial_vel_x
    momentum_component = 'x'
    porosity = porosity_var
    rho = rho
  []
  [u_viscosity]
    type = PINSFVMomentumDiffusion
    variable = superficial_vel_x
    mu = mu
    momentum_component = 'x'
    porosity = porosity_var
  []
  [u_pressure]
    type = PINSFVMomentumPressure
    variable = superficial_vel_x
    momentum_component = 'x'
    pressure = pressure
    porosity = porosity_var
    []
  [u_friction]
      type = PINSFVMomentumFriction
      variable = superficial_vel_x
      momentum_component = 'x'
      Darcy_name = 'darcy_friction_factor'
      porosity = porosity_var
      rho = rho
  []

  [v_time]
    type = WCNSFVMomentumTimeDerivative
    variable = superficial_vel_y
    drho_dt = drho_dt
    rho = rho
    momentum_component = 'y'
   []
   [v_advection]
    type = PINSFVMomentumAdvection
    variable = superficial_vel_y
    momentum_component = 'y'
    porosity = porosity_var
    rho = rho
  []
  [v_viscosity]
    type = PINSFVMomentumDiffusion
    variable = superficial_vel_y
    mu = mu
    momentum_component = 'y'
    porosity = porosity_var
  []
  [v_pressure]
    type = PINSFVMomentumPressure
    variable = superficial_vel_y
    momentum_component = 'y'
    pressure = pressure
    porosity = porosity_var
  []
  [v_friction]
    type = PINSFVMomentumFriction
    variable = superficial_vel_y
    momentum_component = 'y'
    Darcy_name = 'darcy_friction_factor'
    porosity = porosity_var
    rho = rho
  []
[]


[FVBCs]
  [no_slip_x]
    type = INSFVNoSlipWallBC
    variable = superficial_vel_x
    boundary = 'bottom right'
    momentum_component = x
    function = 0
  []

  [no_slip_y]
    type = INSFVNoSlipWallBC
    variable = superficial_vel_y
    boundary = 'bottom right'
    momentum_component = y
    function = 0
  []
  
  [outlet_p]
    type = INSFVOutletPressureBC
    variable = pressure
    boundary = 'top'
    function  = 'outlet_pressure_csv'
  []
[]



[Executioner]
  type = Transient
  solve_type = 'NEWTON'
  petsc_options_iname = '-pc_type -pc_factor_shift_type -snes_linesearch_damping'
  petsc_options_value = 'lu       NONZERO                0.9'

  # [TimeStepper]
  #   type = IterationAdaptiveDT
  #   dt = 1e-2
  #   optimal_iterations = 40
  #   iteration_window = 1
  # []
  dt = 0.1
  end_time = 20


  l_abs_tol = 1e-3
  nl_abs_tol = 1e-3
  nl_max_its = 100
  line_search = 'none'

  automatic_scaling = true
[]

# Some basic Postprocessors to visually examine the solution
[Postprocessors]
  # [outlet-p]
  #   type = SideAverageValue
  #   variable = pressure
  #   boundary = 'top'
  #   execute_on = TIMESTEP_BEGIN
  # []
  # [outlet-v]
  #   type = SideAverageValue
  #   variable = vel_y
  #   boundary = 'top'
  # []
  [pellet-inlet-p]
    type = SideAverageValue
    variable = pressure
    boundary = 'bottom'
    execute_on = 'INITIAL TIMESTEP_BEGIN'
  []
[]

# [VectorPostprocessors]
#   [axial_pressure_distribution]
#   type = LineValueSampler
#   end_point = ${height_stack}
#   start_point = 0 
#   num_point = 60
#   variable = pressure
#   []
# []


# BLOCKS TO CHANGE

initial_pressure = 4293339

[Functions] 
  [outlet_pressure_csv]
    type = PiecewiseLinear
    data_file = pressure_bc.csv
    scale_factor = 1.0
    format = columns
  []
  # [porosity_distribution]
  #   type = ParsedFunction
  #   expression = ${epsilon}
  # []
  [porosity_distribution]
    type = PiecewiseConstant
    axis = y
    xy_data = '${fparse height_stack/4} 0.05
               ${fparse height_stack/2} 0.07
               ${fparse 3*height_stack/4} 0.05
               ${fparse height_stack} 0.07'
               direction = RIGHT
  []
  # [porosity_distribution]
  #   type = PiecewiseConstant
  #   axis = y
  #   xy_data = '${fparse height_stack/2} 0.07
  #              ${fparse height_stack} 0.05'
  #              direction = RIGHT
  # []
[]


[Outputs]
 [exodus_07_05]
   type = Exodus
 []
 [csv_07_05]
    type = CSV
 [] 
[]

[Debug]
 show_material_props = true
[]

