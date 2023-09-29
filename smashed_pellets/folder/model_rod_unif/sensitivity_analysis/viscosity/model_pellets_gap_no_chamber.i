temperature = 300
advected_interp_method = 'upwind'
velocity_interp_method = 'rc'
T = 300
mu = 0.0000179
     
porosity_pellet = 0.171707174

height_stack = ${fparse pellet_radius*8}
height_plenum = ${fparse (0.0254*6-height_stack)/2}
height_rod = ${fparse height_plenum + height_stack} 
pellet_radius = 0.00397
cladding_radius = 0.0041656
gap = ${fparse cladding_radius-pellet_radius} 
gap_hydraulic_diameter = ${fparse 2*(cladding_radius-pellet_radius)/(cladding_radius-pellet_radius)^2*(cladding_radius^2-pellet_radius^2)/(cladding_radius^4-pellet_radius^4-(cladding_radius^2-pellet_radius^2)^2/log(cladding_radius/pellet_radius))}




[Mesh]
  uniform_refine = 0
  [rod]
    type = GeneratedMeshGenerator
    dim = 2
    xmax = ${cladding_radius}
    xmin = 0
    ymax = ${height_stack}
    ymin = 0
    nx = 10
    ny = 30
  []
 coord_type = 'RZ'
 rz_coord_axis = 'Y'
[]

[UserObjects]
  [rc]
    type = INSFVRhieChowInterpolator
    u = superficial_vel_x
    v = superficial_vel_y
    pressure = pressure
  []
[]

[FluidProperties] 
  [fp]
    type = IdealGasFluidProperties
  []
[]

[GlobalParams]
  rhie_chow_user_object = 'rc'
  fp = air
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
  []
[]



[AuxVariables]
  [porosity_var]
    type = MooseVariableFVReal
  []
  [viscosity_var]
  type = MooseVariableFVReal
  []
  [velocity_norm]
    type = MooseVariableFVReal
  []
[]

[ICs]
  [pellets_porosity_ICs]
    type = FunctionIC
    variable = porosity_var
    function = ${porosity_pellet} 
  []
[]


[AuxKernels]
  [viscosity_aux_kernel]
    type = FunctorElementalAux
    functor = sutherland_mu
    variable = viscosity_var
  []
  [speed]
    type = VectorMagnitudeAux
    variable = 'velocity_norm'
    x = superficial_vel_x
    y = superficial_vel_y
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
    mu = ${mu}
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
  [u_porous_friction]
    type = INSFVMomentumFriction
      variable = superficial_vel_x
      momentum_component = 'x'
      linear_coef_name = 'darcy_friction_factor'
      porosity = porosity_var
  []
  # [u_annulus_friction]
  #   type = INSFVMomentumFriction
  #   variable = superficial_vel_x
  #   momentum_component = 'x'
  #   linear_coef_name = 'laminar_friction_factor'
  # []


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
    mu = ${mu}
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
  [v_porous_friction]
    type = INSFVMomentumFriction
    variable = superficial_vel_y
    momentum_component = 'y'
    linear_coef_name = 'darcy_friction_factor'
    porosity = porosity_var
  []
  # [v_annulus_friction]
  #   type = INSFVMomentumFriction
  #   variable = superficial_vel_y
  #   momentum_component = 'y'
  #   linear_coef_name = 'laminar_friction_factor'
  # []
[]


[FVBCs]
  [no_slip_x]
    type = INSFVNaturalFreeSlipBC
    variable = superficial_vel_x
    boundary = 'bottom right' # pellets_right'
    momentum_component = x
    function = 0
  []
  [no_slip_y]
    type = INSFVNaturalFreeSlipBC
    variable = superficial_vel_y
    boundary = 'bottom right' # pellets_right'
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

  dt = 0.1
  end_time = 30


  l_abs_tol = 1e-3
  nl_abs_tol = 1e-3
  nl_max_its = 50
  line_search = 'none'

  automatic_scaling = true
[]

# Some basic Postprocessors to visually examine the solution
[Postprocessors]
  [inlet-p]
    type = SideAverageValue
    variable = pressure
    boundary = bottom
    execute_on = 'INITIAL TIMESTEP_BEGIN'
  []
  [outlet-p]
    type = SideAverageValue
    variable = pressure
    boundary = top
    execute_on = 'INITIAL TIMESTEP_BEGIN'
  []
[]


# BLOCKS TO CHANGE

initial_pressure = 4293339


[Materials]
  [drho_dt]
    type = GeneralFunctorFluidProps
    fp = fp
    pressure = pressure
    T_fluid = ${temperature} 
    characteristic_length = 1
    porosity = porosity_var
    speed = 'velocity_norm' 
  []
  # [laminar_friction_factor]
  #   type = LaminarFrictionFactorMaterialFunctor
  #   mu = sutherland_mu 
  #   porosity = porosity_var
  #   D_h = 0.5e-06 #${gap_hydraulic_diameter}
  # []
  [darcy_friction_factor]
    type = DarcyFrictionFactorMaterialFunctor
    mu = ${mu}
    porosity = porosity_var
    c = 4e-12
  []
  [sutherland_mu]
    type = AirSutherlandMuMaterial
    T = ${T}
  []

[]


[Functions] 
  [outlet_pressure_csv]
    type = ADPiecewiseLinear
    data_file = pressure_bc.csv
    scale_factor = 1.0
    format = columns
  []
  [empirical_factor]
    type = ParsedFunction
    expression = 'if(x<${pellet_radius}, 1e-8, 1e-15)'
  []
  # [function_hydraulic_diameter]
  #   type = PiecewiseLinear
  #   x = '0 5 8 50'
  #   y = '2e-6 2e-6 ${gap_hydraulic_diameter} ${gap_hydraulic_diameter}'
  # []
[]

[Outputs]
  exodus = false
  csv = true
[]
