
[StochasticTools]
[]

[GlobalParams]
  sampler = csv
[]

[Samplers]
  [csv]
    type = CSVSampler
    samples_file = 'parameters.csv'
    column_names = 'particle_diameter_1'
    execute_on = PRE_MULTIAPP_SETUP
  []
[] 


[MultiApps]
  [runner] 
    type = SamplerTransientMultiApp
    input_files = 'model_pellets.i'
  []
[]


# The transfer block is composed of a first “parameters” sub-block, which creates an object able to transfer the listed parameters in a sub-application. The second “results” sub-block has the purpose of transferring the quantity of interest back to the main application. In this case those quantities are the post-processors on the sub-application that compute the pressure.

[Transfers]
  [results]
    type = SamplerReporterTransfer
    from_multi_app = runner
    stochastic_reporter = results
    from_reporter = 'inlet-p/value'
  []
[]


[VectorPostprocessors]
    [data]
      type = SamplerData
      execute_on = 'initial timestep_end'
  []
[]


# The reporters block is used to collect the stochastic results in a vector for each of the quantities of interest. In this case it computes the mean and the standard deviation for the pressure, as well as the 5% and 95% confidence level intervals. 


[Reporters]
  [results]
    type = StochasticReporter
  []
[]


# The output block enables the output of the reported data using JSON files.

[Outputs]
  execute_on = 'FINAL'
  csv = true
[]

[Controls]
  [cmdline]
  type = MultiAppSamplerControl
  multi_app = runner
  param_names = 'particle_diameter_1'
  []
[]


[Executioner]
  type = Transient
  dt = 1
  end_time = 435
[]
