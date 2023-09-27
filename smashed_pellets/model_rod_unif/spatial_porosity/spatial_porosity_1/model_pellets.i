temperature = 300
advected_interp_method = 'upwind'
velocity_interp_method = 'rc'
T = 300


height_stack = '${fparse pellet_radius*8}'
initial_pressure = 7002980
particle_diameter_1 =  0.00028
particle_diameter_2 = 2e-7 

pellet_radius = 0.00397  
cladding_radius = 0.0041656


[Outputs]
  [3_csv]
    type = CSV
    interval = 200
  []
  # [1_exodus]
  #   type = exodus
  # []
  # [along_line]
  #   type = CSV
  #   execute_vector_postprocessors_on = timestep_end
  #   interval = 10
  # []
  # exodus = true
  # csv = true
[]


pellet_1 = 0.028571 
pel_1 = '${fparse pellet_1}'
pellet_2 =  0.029315
pel_2 = '${fparse pellet_2}'
pellet_3 = 0.017565
pel_3 = '${fparse pellet_3}'
pellet_4 = 0.028869 
pel_4 = '${fparse pellet_4}'

[Mesh] 
  uniform_refine = 0
 [gen]
   type = CartesianMeshGenerator 
   dim = 2
   dx =  '${cladding_radius}'
   dy =  '${height_stack}' 
   ix = '10'
   iy = '240'
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
  [air]
    type = IdealGasFluidProperties
  []
[]

[GlobalParams]
  rhie_chow_user_object = 'rc'
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
  [reynolds]
    type = MooseVariableFVReal
  []
[]

[ICs]
  [pellets_porosity_ICs]
    type = FunctionIC
    variable = porosity_var
    function = 'smeared_porosity'
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
  [Re]
    type = ReynoldsNumberFunctorAux
    mu = sutherland_mu
    rho = rho
    speed = superficial_vel_y
    variable = reynolds
  []
[]


[Materials]
  [drho_dt]
    type = GeneralFunctorFluidProps
    fp = air
    pressure = pressure
    T_fluid = ${temperature}
    characteristic_length = 1
    porosity = porosity_var
    speed = 'velocity_norm'
  []
  [darcy_friction_factor]
    type = DarcyFrictionFactorMaterialFunctor
    mu = sutherland_mu
    porosity = porosity_var
    rho = rho
    Dp_1 = ${particle_diameter_1}
    Dp_2= ${particle_diameter_2} 
  []
  [sutherland_mu]
    type = AirSutherlandMuMaterial
    T = ${T}
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
    mu = sutherland_mu
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
    mu = sutherland_mu
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
  []
[]

[FVBCs]
  [no_slip_x]
    type = INSFVNaturalFreeSlipBC
    variable = superficial_vel_x
    boundary = 'right'
    momentum_component = x
  []
  [no_slip_y]
    type = INSFVNaturalFreeSlipBC
    variable = superficial_vel_y
    boundary = 'right'
    momentum_component = y
  []
  [outlet_p]
    type = INSFVOutletPressureBC
    variable = pressure
    boundary = 'top'
    function = 'outlet_pressure_csv'
  []
[]

[Executioner]
  type = Transient
  solve_type = 'NEWTON'
  petsc_options_iname = '-pc_type -pc_factor_shift_type -snes_linesearch_damping'
  petsc_options_value = 'lu       NONZERO                0.9'

  #   [TimeStepper]
  #     type = IterationAdaptiveDT
  #     dt = 1e-2
  #     optimal_iterations = 40
  #     iteration_window = 1
  #   []
  dt = 1
  end_time = 3000

  l_abs_tol = 1e-3
  nl_abs_tol = 1e-3
  nl_max_its = 50
  line_search = 'none'

  automatic_scaling = true
[]

# Some basic Postprocessors to visually examine the solution
[Postprocessors]
  [time]
    type = TimePostprocessor
  []
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

[Functions]
  [outlet_pressure_csv]
    type = ADPiecewiseLinear
    data_file = pressure_bc.csv
    scale_factor = 1.0
    format = columns
  []
  [smeared_porosity]
    type = PiecewiseConstant
    axis = y
    direction = RIGHT_INCLUSIVE
    x = '0.00794 0.01588 0.02382 0.03176'
    y = '${pel_1} ${pel_2} ${pel_3} ${pel_4}'
  []
[]



[VectorPostprocessors]
  [pressure_distribution]
    type = LineValueSampler
    variable = pressure
    start_point = '0 0 0'
    end_point = '0 ${height_stack} 0'
    sort_by = y
    num_points = 240
    execute_on = timestep_end
  []
[]

# [Reporters]
#   [acc]
#     type = AccumulateReporter
#     reporters = 'inlet-p/value outlet-p/value time/value'
#   []
# []
