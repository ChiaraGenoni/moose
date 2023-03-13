
# Darcy flow
[Mesh]
    second_order = true
    [set_up]
        type = FileMeshGenerator
        file = combined_annular_porous_flow.e
    []
[]

[GlobalParams]
  PorousFlowDictator = dictator
[]

[Variables]
  [porepressure]
  []
[]

[ICs]
  [InitialConditioms]
    type = FunctionIC
    variable = 'porepressure'
    function = atm_pressure
  []
[]

[Functions]
  [atm_pressure]
    type = ParsedFunction
    value = '187509.5-5427235.516*z'
  []
[]

[PorousFlowBasicTHM]
  porepressure = porepressure
  coupling_type = Hydro
  gravity = '0 -1 0'
  fp = the_simple_fluid
[]

[BCs]
  [constant_injection_porepressure]
    type = DirichletBC
    variable = porepressure
    value = 101325
    boundary = low_pressure
  []
[]

[FluidProperties]
  [the_simple_fluid]
    type = SimpleFluidProperties
    viscosity = 0.0000179
    density0 = 1.322
  []
[]

[Materials]
  [porosity]
    type = PorousFlowPorosityConst
    porosity = 1
    []

  # [porosity]
  # type = PorousFlowPorosity
  # fluid = true
  # mechanical = true
  # porosity_zero = 0.107*
  # biot_coefficient = 0.1
  # solid_bulk = 3.02e9
  # []

  [biot_modulus]
    type = PorousFlowConstantBiotModulus
    biot_coefficient = 1
    solid_bulk_compliance = 1e22                                                                                                           
    fluid_bulk_modulus = 1
  []
  
  [gap_permeability]
    type = PorousFlowPermeabilityConst
    permeability = '1e-9 0 0   0 1e-9 0   0 0 1e-9 '
    block = annulus
    []
    [fuel_permeability]
    type = PorousFlowPermeabilityConst
    permeability = '3.88e-13 0 0  0 3.88e-13 0  0 0 3.88e-13'
    block = pellet
    []
[]


[Preconditioning]
  active = basic
  [basic]
    type = SMP
    full = true

  []
  [preferred_but_might_not_be_installed]
    type = SMP
    full = true
    petsc_options_iname = '-pc_type -pc_factor_mat_solver_package'
    petsc_options_value = ' lu       mumps'
  []
[]

[Postprocessors]
  [AveragePressure]
  type = SideAverageValue
  boundary = high_pressure
  variable = porepressure
  execute_on = 'initial timestep_end'
  []
[]

[Executioner]
  type = Transient
  solve_type = Newton
  end_time = 50
  dt = 1
  nl_abs_tol =1E-13
  l_max_its = 100
[]

[Outputs]
  [exodus]
  type = Exodus
  []
[]



