[Mesh]
    second_order = true
    [tube]
        type = FileMeshGenerator
        file = tube.e
    []
[]

[Problem]
    kernel_coverage_check = false
[]
  
[Variables]
    [pressure]
        initial_condition = 101325
    []
[]

[Functions]
    [pressure_ramp]
        type = ParsedFunction
        value = 10000*t
    []
[]


[BCs]
  [fixed_pressure]
    type = FunctionDirichletBC
    variable = pressure
    boundary = 'high_pressure'
    function = pressure_ramp
  []
[]

# [Controls]
#     [stop]
#       type = TimePeriod
#       enable_objects = fixed_pressure
#       start_time = '0'
#       end_time = '17.2369'
#     []
#   []


[Kernels]
    [DarcyFlux]
        type = DarcyFluxPressure
        variable = pressure
        block = 'interspace box'
    []
[]

[Materials]
    [gas]
        type = GenericConstantMaterial
        prop_names = 'conductivity density'
        prop_values = '6.98646e-09 1.2041'
    []
[]


[Executioner]
    type = Transient
    solve_type = 'PJFNK'
    petsc_options_iname = '-pc_type -pc_factor_mat_solver_package'
    petsc_options_value = 'lu superlu_dist'

    dt = 1.0
    end_time = 3600
[]

[Outputs]
    [out]
      type = Exodus
    []
[]

[Postprocessors]
[volume_average_pressure]
    type = AverageNodalVariableValue
    variable = pressure
    block = box
[]
[]

[UserObjects]
    [time_step_stopper]
      type = Terminator
      expression = 'volume_average_pressure > 172369'
      fail_mode = HARD
      execute_on = TIMESTEP_END
    []
  []

