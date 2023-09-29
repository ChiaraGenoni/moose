[StochasticTools]
[]


[GlobalParams]
  sampler = csv
[]

[MultiApps]
  [stochastic]
    type = SamplerFullSolveMultiApp
    mode = batch-reset
    input_files = 'model_pellets.i' 
  []
[]
 
[Samplers]
  [csv]
    type = CSVSampler
    samples_file = 'combinations.csv'
    column_names = 'particle_diameter_1'
    execute_on = PRE_MULTIAPP_SETUP
  []
[]

[Transfers]
  [results]
    type = SamplerReporterTransfer
    from_multi_app = stochastic
    stochastic_reporter = results
    from_reporter = 'acc/inlet-p:value acc/outlet-p:value acc/time:value'
  []
[]

[Reporters]
  [results]
    type = StochasticReporter
    parallel_type = ROOT
  []
[]


[VectorPostprocessors] 
  [samples]
    type = SamplerData
  []
[]


[Controls]
  [param]
    type = MultiAppSamplerControl
    multi_app = stochastic
    param_names = 'particle_diameter_1'
  []
[]

[Outputs]
  [out]
    type = JSON
    vectorpostprocessors_as_reporters = true
  []
[]

