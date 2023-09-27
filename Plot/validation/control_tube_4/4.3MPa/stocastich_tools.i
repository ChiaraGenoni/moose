
[StochasticTools]
[]


[Samplers]
  [cartesian]
    type = InputMatrix
    matrix = '1.05721E-09;
    7.55868E-10;
    5.24055E-10;
    3.71865E-10;
    2.39161E-10;
    9.00487E-11;
    4.72417E-11;
    2.27825E-11;
    9.3317E-12;
    6.12253E-12;
    4.32291E-12;
    2.95261E-12;'
    execute_on = PRE_MULTIAPP_SETUP
  []
[]





[MultiApps]
  [runner] 
    type = SamplerTransientMultiApp
    sampler = cartesian
    input_files = 'model_pellets.i'
  []
[] 


# The transfer block is composed of a first “parameters” sub-block, which creates an object able to transfer the listed parameters in a sub-application. The second “results” sub-block has the purpose of transferring the quantity of interest back to the main application. In this case those quantities are the post-processors on the sub-application that compute the pressure.

[Transfers]
  [results]
    type = SamplerReporterTransfer
    from_multi_app = runner
    sampler = cartesian
    stochastic_reporter = results
    from_reporter = 'inlet-p/value'
  []
[]


[VectorPostprocessors]
    [data]
      type = SamplerData
      sampler = cartesian
      execute_on = 'initial timestep_end'
  []
[]


# The reporters block is used to collect the stochastic results in a vector for each of the quantities of interest. In this case it computes the mean and the standard deviation for the pressure, as well as the 5% and 95% confidence level intervals. 


[Reporters]
  [results]
    type = StochasticReporter
    outputs = none
  []
[]


# The output block enables the output of the reported data using JSON files.

[Outputs]
  execute_on = 'FINAL'
  [out]
    type = JSON
  [] 
  [out_1]
    type = CSV
  []
[]

[Controls]
  [cmdline]
  type = MultiAppSamplerControl
  multi_app = runner
  sampler = cartesian
  param_names = 'empirical_factor'
  []
[]


[Executioner]
  type = Transient
  dt = 1
  end_time = 300
[]
 