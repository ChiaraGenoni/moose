
[StochasticTools]
[]

[GlobalParams]
  sampler = csv
[]

[MultiApps]
  [runner] 
    type = SamplerTransientMultiApp
    # mode = batch-reset
    input_files = 'model_pellets.i'
  []
[]

[Samplers]
  [csv]
    type = CSVSampler
    samples_file = 'parameters.csv'
    column_names = 'particle_diameter_1'
    execute_on = PRE_MULTIAPP_SETUP
  []
[] 


[Transfers]
  [results]
    type = SamplerReporterTransfer
    from_multi_app = runner
    stochastic_reporter = results
    from_reporter = 'inlet-p/value'
  []
[]


[Reporters]
  [results]
    type = StochasticReporter
    parallel_type = ROOT
  []
[]


[VectorPostprocessors]
  [data]
    type = SamplerData
    execute_on = 'initial timestep_end'
  []
[]

[Controls]
  [cmdline]
  type = MultiAppSamplerControl
  multi_app = runner
  param_names = 'particle_diameter_1'
  []
[]


[Outputs]
  execute_on = 'FINAL'
  csv = true
[]


[Executioner]
  type = Transient
  dt = 1
  end_time = 1400
[]
