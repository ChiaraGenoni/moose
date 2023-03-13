
# The sides of the domain are named as bottom, top ,left, right, front and back

[GlobalParams]
    order = SECOND
[]

[Mesh]
    second_order = true
    [Square]
        type = FileMeshGenerator
        file = fuel_2.e
    []
    # [primary_subdomain]
    #     type = LowerDBlockFromSidesetGenerator
    #     input = Square
    #     sidesets = 'clad_inner'
    #     new_block_id = '10001'
    #     new_block_name = 'primary_lower'
    #   []
    #   [secondary_subdomain]
    #     type = LowerDBlockFromSidesetGenerator
    #     input = primary_subdomain
    #     sidesets = 'fuel_lateral'
    #     new_block_id = '10000'
    #     new_block_name = 'secondary_lower'
    #   []
[]



# [GlobalParams]
#     displacements = 'disp_x disp_y disp_z'
# []

# The primary or dependent variables in the PDES are defined in the VARIABLES BLOCK.
# A user-selected name is assigned to each variable
 
[Variables]
    [temperature]
        initial_condition = 300
    []
    # [disp_x]
    # []
    # [disp_y]
    # []
    # [disp_z]
    # []
[]

# The Kernels (individual terms in the PDEs being solved) are listed in the KERNELS BLOCK

[Kernels]
    [heat_conduction]
        type = HeatConduction
        variable = temperature
        block = 'fuel cladding'
    []
    [heat_source]
        type = HeatSource
        variable = temperature
        value = 6.67e8
        block = fuel
    []
[]

[ThermalContact]
   [thermal_contact]
      type = GapHeatTransfer
      gap_conductivity = 0.277
      variable = temperature
      gap_geometry_type  = CYLINDER
      primary = clad_inner
      secondary = fuel_lateral
      cylinder_axis_point_1 = '0 0 0'
      cylinder_axis_point_2 = '0 0 1'
   []
[]

# [MortarGapHeatTransfer]
#     [thermal_contact]
#         temperature = temperature
#         boundary = clad_inner
#         gap_conductivity = 0.277
#         primary_boundary = clad_inner 
#         secondary_boundary = fuel_lateral
#         gap_flux_options = 'CONDUCTION'
#         gap_geometry_type = CYLINDER
#         primary_subdomain = primary_lower
#         secondary_subdomain = secondary_lower
#     []
# []

# [Modules/TensorMechanics/Master]
#     [fuel]
#         block = fuel
#         add_variables = false
#         strain = FINITE
#         eigenstrain_names = thermal_eigenstrain
#         temperature = temperature
#     []
#     [cladding]
#         block = cladding
#         add_variables = false
#         strain = finite
#         eigenstrain_names = thermal_eigenstrain
#         temperature = temperature
#     []
# []


# Material properties are defined in the MATERIALS BLOCK. Infarmation from the materials block
# is generally used by some kernels. Here the thermal conductivity is defined for use by the 
# HeatConduction kernel

[Materials]
    [clad_heat_conductor]
        type = HeatConductionMaterial
        thermal_conductivity = 18.69
        block = cladding
    []
    [fuel_heat_conductor]
        type = HeatConductionMaterial
        thermal_conductivity = 3.011
        block = fuel
    []

    # [clad_elasticity_tensor]
    #     type = ComputeIsotropicElasticityTensor
    #     block = cladding
    #     youngs_modulus = 99e9
    #     poissons_ratio = 0.406
    # []
    # [fuel_elasticity_tensor]
    #     type = ComputeIsotropicElasticityTensor
    #     block = cladding
    #     youngs_modulus = 233e9
    #     poissons_ratio = 0.276
    # []

    # [clad_thermal_expansion_strain]
    #     type = ComputeThermalExpansionEigenstrain
    #     stress_free_temperature = 20
    #     thermal_expansion_coeff = 
    #     temperature = temperature
    #     eigenstrain_name = thermal_eigenstrain
    #     block = cladding
    # []
    # [clad_stress]
    #     type = ComputeFiniteStrainElasticStress
    #     block = cladding
    # []
    # [fuel_thermal_expansion_strain]
    #     type = ComputeThermalExpansionEigenstrain
    #     stress_free_temperature = 20
    #     thermal_expansion_coeff = 0.223e-3
    #     temperature = temperature
    #     eigenstrain_name = thermal_eigenstrain
    #     block = fuel
    # []
    # [fuel_stress]
    #     type = ComputeFiniteStrainElasticStress
    #     block = fuel
    # []
[]


# Boundary conditions are defined in the BCs BLOCK

[BCs]
    [clad_outer_temp]
        type = DirichletBC
        variable = temperature
        boundary = 'clad_outer'
        value = 613
    []
    # [leftright_disp_x]
    #     type = DirichletBC
    #     variable = disp_x
    #     boundary = 'left right'
    #     value = 0
    # []
[]

# The EXECUTIONER BLOCK defines the method that is applied to solve the problem 

[Executioner]
    type = Transient
    solve_type = 'PJFNK'
    petsc_options_iname = '-pc_type -pc_factor_mat_solver_package'
    petsc_options_value = 'lu superlu_dist'

    dt = 1.0
    end_time = 1.0
[]

# The OUTPUT blocks contains the output file type (in this case exodus, which is the most common, 
# controllable and well supported output type).  The "short cut" sytnax implies the default naming 
# scheme for the output file, meaning that it utilizes the input file name with the "_out" suffix.
# The sub block syntax is also available and it allows to use the actual sub-block user-defined 
# name as suffix in the output file name. 
# EXAMPLE of sub-block syntax
# [Outputs]
#    [output]
#       type = Exodus
# []

[Outputs]
    [out]
      type = Exodus
    []
[]

[Postprocessors]
    [peak_temperature]
    type = NodalExtremeValue
    variable = temperature
    []
[volume_average_fuel]
    type = AverageNodalVariableValue
    variable = temperature
    block = fuel
[]
[volume_average_clad]
    type = AverageNodalVariableValue
    variable = temperature
    block = cladding
[]

[]