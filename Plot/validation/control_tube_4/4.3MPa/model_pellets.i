viscosity =  0.0000179
T = 300
advected_interp_method = 'upwind'
velocity_interp_method = 'rc'


pellet_radius = 0.00397
cladding_radius = 0.0041656
height_stack = 0.03176
height_plenum = ${fparse (0.0254*6-height_stack)/2}

porosity_gap = 1
porosity_pellets = 0.089
empirical_factor = 1.56914e-10
#  quadratic = 3e10
refinement = 0 



[Mesh] 
  uniform_refine = ${refinement}
 [gen]
   type = CartesianMeshGenerator
   dim = 2
   dx =  '${cladding_radius}'
   dy =  '${height_stack}'
   ix = '10'
   iy = '30'
 []
 coord_type = 'RZ'
 rz_coord_axis = 'Y'
[]


[GlobalParams]
  rhie_chow_user_object = 'rc'
  fp = air  
[]


[FluidProperties]
  [air]
    type = IdealGasFluidProperties
  []
[]

[UserObjects]
  [rc]
    type = INSFVRhieChowInterpolator
    u = superficial_vel_x
    v = superficial_vel_y
    pressure = pressure
    smoothing_layers = 2
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
  [viscosity_var]
    type = MooseVariableFVReal
  []
[]

[ICs]
  [pellets_porosity_ICs]
    type = FunctionIC
    variable = porosity_var
    function = ${porosity_pellets} 
  []
  # [measuring_chamber_porosity_ICs]
  #   type = FunctionIC
  #   variable = porosity_var
  #   function = 1
  #   block = 1
  # []
[]

[AuxKernels]
  [viscosity_aux_kernel]
    type = FunctorElementalAux
    functor = sutherland_mu
    variable = viscosity_var
  []
  [speed]
    type = VectorMagnitudeAux
    variable = 'velocity_norm'
    x = superficial_vel_x
    y = superficial_vel_y
  []
[]

[Materials]
  [drho_dt]
    type = GeneralFunctorFluidProps
    pressure = pressure
    T_fluid = ${T} 
    characteristic_length = 1
    porosity = porosity_var
    speed = 'velocity_norm'
  [] 
  [hon_factor_porous]
    type = DarcyFrictionFactorMaterialFunctor
    mu = sutherland_mu 
    porosity = porosity_var
    c = ${empirical_factor}
  []
  [sutherland_mu]
    type = AirSutherlandMuMaterial
    T = ${T}
  []
  # [quadratic_coefficient]
  #   type = ADGenericFunctorMaterial
  #   prop_names = 'Forecheimer'
  #   prop_values = ${quadratic}
  # []
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
    []
  [u_time]
    type = WCNSFVMomentumTimeDerivative
    variable = superficial_vel_x
    drho_dt = drho_dt
    rho = rho
    momentum_component = 'x'
  []
  [u_advection]
    type = PINSFVMomentumAdvection
    variable = superficial_vel_x
    momentum_component = 'x'
    porosity = porosity_var
    rho = rho
  []
  [u_viscosity]
    type = PINSFVMomentumDiffusion
    variable = superficial_vel_x
    mu = viscosity_var
    momentum_component = 'x'
    porosity = porosity_var
  []
  [u_pressure]
    type = PINSFVMomentumPressure
      variable = superficial_vel_x
      momentum_component = 'x'
      pressure = pressure
      porosity = porosity_var
    []
  [u_porous_friction]
      type = INSFVMomentumFriction
        variable = superficial_vel_x
        momentum_component = 'x'
        linear_coef_name = 'darcy_friction_factor'
        # quadratic_coef_name = 'Forecheimer'
        porosity = porosity_var
  []
  [v_time]
    type = WCNSFVMomentumTimeDerivative
    variable = superficial_vel_y
    drho_dt = drho_dt
    rho = rho
    momentum_component = 'y'
   []
   [v_advection]
    type = PINSFVMomentumAdvection
    variable = superficial_vel_y
    momentum_component = 'y'
    porosity = porosity_var
    rho = rho
  []
  [v_viscosity]
    type = PINSFVMomentumDiffusion
    variable = superficial_vel_y
    mu = viscosity_var
    momentum_component = 'y'
    porosity = porosity_var
  []
  [v_pressure]
    type = PINSFVMomentumPressure
    variable = superficial_vel_y
    momentum_component = 'y'
    pressure = pressure
    porosity = porosity_var
  []
  [v_porous_friction]
    type = INSFVMomentumFriction
    variable = superficial_vel_y
    momentum_component = 'y'
    linear_coef_name = 'darcy_friction_factor'
    # quadratic_coef_name = 'Forecheimer'
    porosity = porosity_var
  []
[]


[FVBCs]
  [no_slip_x]
    type = INSFVNaturalFreeSlipBC
    variable = superficial_vel_x
    boundary = 'bottom right'
    momentum_component = x
  []

  [no_slip_y]
    type = INSFVNaturalFreeSlipBC
    variable = superficial_vel_y
    boundary = 'bottom right'
    momentum_component = y
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

  # [TimeStepper]
  #   type = IterationAdaptiveDT
  #   dt = 1e-2
  #   optimal_iterations = 40
  #   iteration_window = 1
  # []
  dt = 1
  end_time = 300
 

  l_abs_tol = 1e-3
  nl_abs_tol = 1e-3
  nl_max_its = 100
  line_search = 'none'

  automatic_scaling = true
[]

# Some basic Postprocessors to visually examine the solution
[Postprocessors]
  [inlet-p]
    type = SideAverageValue
    variable = pressure
    boundary = bottom
    execute_on = 'INITIAL TIMESTEP_BEGIN'
  []
  [outlet-p]
    type = SideAverageValue
    variable = pressure
    boundary = top
    execute_on = 'INITIAL TIMESTEP_BEGIN'
  []

[]


# BLOCKS TO CHANGE

initial_pressure = 4582919

[Functions] 
  [outlet_pressure_csv]
    type = PiecewiseLinear
    data_file = pressure_bc.csv
    scale_factor = 1.0
    format = columns 
  []
[]

[Outputs]
  exodus = false
  csv = true
[]

[Debug]
 show_material_props = true
[]

 
