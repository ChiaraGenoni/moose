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
    samples_file = 'porosities.csv'
    column_names = 'porosity'
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
    param_names = 'porosity_pellets'
  []
[]

[Outputs]
  [out]
    type = JSON
    vectorpostprocessors_as_reporters = true
  []
[]

