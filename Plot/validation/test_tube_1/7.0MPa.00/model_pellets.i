mu =  0.0000179
temperature = 300
advected_interp_method = 'upwind'
velocity_interp_method = 'rc'
coefficient = 1.8e6
outlet_pressure = 101325

pp1 = 0.09
pp2 = 0.91

pellet_radius = 0.00397
cladding_radius = 0.0041656
porosity_pellet = 0.05
porosity_gap = 1

height_rod = 0.03176
height_plenum = 0.01

[Mesh]
   uniform_refine = 0
  [gen]
    type = GeneratedMeshGenerator
    dim = 2
    xmin = 0
    xmax = ${pellet_radius}
    ymin = 0
    ymax = ${height_rod}
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
[]


[FluidProperties]
  [fp]
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
[]

[AuxKernels]
  [porosity_aux_kernel]
  type = FunctionAux
  variable = porosity_var
  function = porosity_distribution
  []
[]

[Materials]
  [drho_dt]
    type = GeneralFunctorFluidProps
    fp = fp
    pressure = pressure
    T_fluid = ${temperature} 
    characteristic_length = 1
    porosity = ${porosity_pellet}
    speed = 'velocity_norm' 

  []
  [darcy]
    type = ADGenericVectorFunctorMaterial
    prop_names = 'Darcy_coefficient'
    prop_values = '${coefficient} ${coefficient} ${coefficient}'
  []
[]


[FVKernels]
  [mass_time]
    type = WCNSFVMassTimeDerivative
    variable = pressure
    drho_dt = drho_dt
    porosity = porosity_var
  []
  [mass]
    type = INSFVMassAdvection
    variable = pressure
    advected_interp_method = ${advected_interp_method}
    velocity_interp_method = ${velocity_interp_method}
    rho = rho
    porosity = porosity_var
  []

  [u_time]
    type = WCNSFVMomentumTimeDerivative
    variable = superficial_vel_x
    drho_dt = drho_dt
    rho = rho
    momentum_component = 'x'
  []
  [u_viscosity]
    type = PINSFVMomentumDiffusion
    variable = superficial_vel_x
    mu = ${mu}
    porosity = ${porosity_pellet}
    momentum_component = 'x'
  []
  [u_pressure]
    type = PINSFVMomentumPressure
    variable = superficial_vel_x
    momentum_component = 'x'
    pressure = pressure
    porosity = ${porosity_pellet}
    []
  
  
  [u_friction]
      type = PINSFVMomentumFriction
      variable = superficial_vel_x
      momentum_component = 'x'
      Darcy_name = 'Darcy_coefficient'
      rho = rho
      porosity = ${porosity_pellet}
  []

  [v_time]
    type = WCNSFVMomentumTimeDerivative
    variable = superficial_vel_y
    drho_dt = drho_dt
    rho = rho
    momentum_component = 'y'
   []
  [v_viscosity]
    type = PINSFVMomentumDiffusion
    variable = superficial_vel_y
    mu = ${mu}
    momentum_component = 'y'
    porosity = ${porosity_pellet}
  []
  [v_pressure]
    type = PINSFVMomentumPressure
    variable = superficial_vel_y
    momentum_component = 'y'
    pressure = pressure
    porosity = ${porosity_pellet}
  []

  [v_friction]
    type = PINSFVMomentumFriction
    variable = superficial_vel_y
    momentum_component = 'y'
    Darcy_name = 'Darcy_coefficient'
    rho = rho
    porosity = ${porosity_pellet}
[]
[]

[AuxKernels]
  [speed]
    type = VectorMagnitudeAux
    variable = 'velocity_norm'
    x = superficial_vel_x
    y = superficial_vel_y
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

#   [TimeStepper]
#     type = IterationAdaptiveDT
#     dt = 1e-2
#     optimal_iterations = 40
#     iteration_window = 1
#   []
  dt = 1.0
  end_time = 50



  nl_abs_tol = 1e-4
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
  #   variable = superficial_vel_y
  #   boundary = 'top'
  # []

  [pellet-inlet-p]
    type = SideAverageValue
    variable = pressure
    boundary = 'bottom'
    execute_on = 'INITIAL TIMESTEP_BEGIN'
  []
  # [gap-inlet-p]
  #   type = FunctionValuePostprocessor
  #   function = outlet_pressure_csv
  #   execute_on = 'INITIAL TIMESTEP_BEGIN'
  # []
  # [inlet-p]
  # type = LinearCombinationPostprocessor
  # pp_coefs = '${pp1} ${pp2}'
  # pp_names = 'gap-inlet-p pellet-inlet-p'
  # execute_on = 'INITIAL TIMESTEP_BEGIN'
  # []
[]


# BLOCKS TO CHANGE

initial_pressure = 7002980

[Functions] 
  [outlet_pressure_csv]
    type = PiecewiseLinear
    data_file = pressure_bc.csv
    scale_factor = 1.0
    format = columns
  []
  [porosity_distribution]
    type = ParsedFunction
    value = 0.05 #10*y
  []
[]

[Outputs]
  exodus = true
  csv = true
[]