p_initial = 4293339
temperature=300
u_in = 1e-15
porous_x = 0.00397
porosity_gap = 1
porosity_pellet = 0.05
coefficient = 1e8
mu = 1.79e-5

[GlobalParams]
  fp = fp
  limiter = 'vanLeer'
  two_term_boundary_expansion = true
[]


[Mesh]
  #uniform_refine = 2
  [gen]
    type = GeneratedMeshGenerator
    dim = 2
    xmin = 0
    xmax = 0.0041656
    ymin = 0
    ymax = 0.03176
    nx = 10
    ny = 50
  []
  coord_type = 'RZ'
  rz_coord_axis = 'Y'
[]

[FluidProperties]
  [fp]
    type = IdealGasFluidProperties
  []
[]

[Problem]
  fv_bcs_integrity_check = false
[]

[Variables]
  [pressure]
    type = MooseVariableFVReal
    initial_condition = ${p_initial}
  []
  [superficial_vel_x]
    type = MooseVariableFVReal
    initial_condition = ${u_in}
  []
  [superficial_vel_y]
    type = MooseVariableFVReal
    initial_condition = ${u_in}
  []
[]

[AuxVariables]
  [rho]
    type = MooseVariableFVReal
  []
  [superficial_rhou]
    type = MooseVariableFVReal
  []
  [variable_porosity]
    type = MooseVariableFVReal
  []
[]

[AuxKernels]
  [rho]
    type = ADMaterialRealAux 
    variable = rho
    property = rho
    execute_on = 'timestep_end'
  []
  [superficial_rhou]
    type = ADMaterialRealAux
    variable = superficial_rhou
    property = superficial_rhou
    execute_on = 'timestep_end'
  []
  [aux_porosity]
    type = FunctionAux
    variable = variable_porosity
    function = variable_porosity_distribution
  []
[]

[FVKernels]
  [mass_time]
    type = FVMatPropTimeKernel
    mat_prop_time_derivative = 'dsuperficial_rho_dt'
    variable = pressure
  []
  [mass_advection]
    type = PCNSFVKT
    variable = pressure
    eqn = "mass"
    porosity = material_porosity
  []

  [momentum_time_x]
    type = FVMatPropTimeKernel
    mat_prop_time_derivative = 'dsuperficial_rhou_dt'
    variable = superficial_vel_x
  []
  [momentum_advection_x]
    type = PCNSFVKT
    variable = superficial_vel_x
    eqn = "momentum"
    momentum_component = 'x'
    porosity = material_porosity
  []
  [momentum_diffusion_x]
    type = FVDiffusion
    variable = superficial_vel_x
    coeff = ${mu}
  []
  [momentum_friction_x]
    type = PCNSFVMomentumFriction
    variable = superficial_vel_x
    momentum_component = 'x'
    Darcy_name = 'darcy_coefficient'
    porosity = variable_porosity
    momentum_name = superficial_rhou
  []

  [momentum_time_y]
    type = FVMatPropTimeKernel
    mat_prop_time_derivative = 'dsuperficial_rhou_dt'
    variable = superficial_vel_y
  []
  [momentum_advection_y]
    type = PCNSFVKT
    variable = superficial_vel_y
    eqn = "momentum"
    momentum_component = 'y'
    porosity = material_porosity
  []
  [momentum_diffusion_y]
    type = FVDiffusion
    variable = superficial_vel_y
    coeff = ${mu}
  []
  [momentum_friction_y]
    type = PCNSFVMomentumFriction
    variable = superficial_vel_y
    momentum_component = 'y'
    Darcy_name = 'darcy_coefficient'
    porosity = variable_porosity
    momentum_name = superficial_rhov
  []
[]

[FVBCs]
  [rho_right]
    type = PCNSFVStrongBC
    boundary = 'right'
    variable = pressure
    superficial_velocity = ${u_in}
    T_fluid = ${temperature}
    pressure = 101325
    eqn = 'mass'
  []
  [wall_no_slip]
    type = PCNSFVStrongBC
    boundary = 'right top bottom'
    variable = superficial_vel_x
    pressure = ${p_initial}
    eqn = 'momentum'
    momentum_component = 'x'
    superficial_velocity = ${u_in}
  []
[]

[Materials]
  [material_variable]
    type = PorousPrimitiveVarMaterial
    pressure = pressure
    T_fluid = ${temperature}
    superficial_vel_x = superficial_vel_x
    superficial_vel_y = superficial_vel_y
    fp = fp
    porosity = variable_porosity
  []

#   [material_porosity]
#      type = CoupledVariableValueMaterial
#      coupled_variable = variable_porosity
#      prop_name = material_porosity
#   []
  
[material_porosity]
        type = ParsedMaterial
        property_name = material_porosity
        function = 'if(x<=${porous_x}, ${porosity_pellet}, ${porosity_gap})'
  []
  [darcy_coefficient]
    type = ADGenericConstantVectorMaterial
    prop_names = darcy_coefficient
    prop_values = '${coefficient} ${coefficient} ${coefficient} '
  []
[]

[Functions]
  [variable_porosity_distribution]
    type = ParsedFunction
    value = 'if(x<=${porous_x}, ${porosity_pellet}, ${porosity_gap})'
  []

#   [darcy]
#     type = ParsedFunction
#     value = 'if(x<=${porous_x}, ${coefficient}, 0)'
#     value = ${coefficient}
#   []

#  [material_porosity_distribution]
#      type = ParsedFunction
#      value ="if(x<+${porous_x}, ${porosity_pellet}, ${porosity_gap})"
     
#    []

[]

[Executioner]
  solve_type = NEWTON
  type = Transient
  nl_max_its = 20
  [TimeStepper]
    type = IterationAdaptiveDT
    dt = 5e-5
    optimal_iterations = 10
  []
  steady_state_detection = false
  steady_state_tolerance = 1e-12
  abort_on_solve_fail = false
  end_time = 100
  nl_abs_tol = 1e-8
  dtmin = 5e-5
  automatic_scaling = true
  compute_scaling_once = false
  verbose = true

  petsc_options_iname = '-pc_type -pc_factor_mat_solver_type -pc_factor_shift_type -snes_linesearch_minlambda'
  petsc_options_value = 'lu       mumps                      NONZERO               1e-3 '
[]

[Postprocessors]
  [inlet-p]
    type = SideAverageValue
    variable = pressure
    boundary = 'bottom'
    execute_on = TIMESTEP_BEGIN
  []
  [outlet-p]
    type = SideAverageValue
    variable = pressure
    boundary = 'top'
    execute_on = TIMESTEP_BEGIN
  []
  [outlet-v]
    type = SideAverageValue
    variable = superficial_vel_y
    boundary = 'top'
  []
[]

[Outputs]
  [exo]
    type = Exodus
    execute_on = 'final'
  []
  [csv]
    type = CSV
  []
[]

[Debug]
  show_var_residual_norms = true
[]
