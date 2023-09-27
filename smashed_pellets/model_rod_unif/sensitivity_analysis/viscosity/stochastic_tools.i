[StochasticTools]
[]




[Samplers]
  [cartesian]
    type = InputMatrix
    matrix = '1.9271e-5; 2.2099e-5; 2.6691e-5; 3.3621e-5; 4.3257e-5; 4.9497e-5'
    execute_on = PRE_MULTIAPP_SETUP
  []
[]



[MultiApps]
  [runner]
    type = SamplerTransientMultiApp
    sampler = cartesian
    input_files = 'model_pellets_gap_no_chamber.i'
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
  # [stats]
  #   type = StatisticsReporter
  #   reporters = 'results/results:acc:pellet-inlet-p:value'
  #   compute = 'mean stddev'
  #   ci_method = 'percentile'
  #   ci_levels = '0.05 0.95'
  # []
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
  param_names = 'mu'
  []
[]


[Executioner]
  type = Transient
  dt = 0.1
  end_time = 30
[]