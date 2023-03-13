
# The FEM mesh is defined in the MESH BLOCK. A mesh can be read in from a file (typically Exodus format). 
# In the following an internal mesh-generator is used. 
# The sides of the domain are named as bottom, top ,left, right, front and back

[Mesh]
    [Cylinder]
        type = FileMeshGenerator
        file = Cylinder.e
    []
   
    # coord_type = XYZ
    # [top_square]
    #     type = GeneratedMeshGenerator
    #     dim = 2
    #     nx = 10
    #     ny = 10
    #     ymin = 1.025
    #     ymax = 2.025
    #     boundary_name_prefix = top_square
    # []
    # [top_square_block]
    #     type = SubdomainIDGenerator
    #     input = top_square
    #     subdomain_id = 1
    # []
    # [bottom_Square]
    #     type = GeneratedMeshGenerator
    #     dim = 2
    #     nx = 10
    #     ny = 10
    #     ymin = 0
    #     ymax = 1
    #     boundary_name_prefix = bottom_square
    #     boundary_id_offset = 4
    # []
    # [bottom_square_block]
    #     type = SubdomainIDGenerator
    #     input = bottom_square
    #     subdomain_id = 2
    # []
    # [two_blocks]
    #         type = MeshCollectionGenerator
    #         inputs = 'top_square_block bottom_square_block'
    #     []
    # [block_rename]
    #         type = RenameBlockGenerator
    #         input = two_blocks
    #         old_block = '1 2'
    #         new_block = 'top_square bottom_square'
    #     []
    # []

    # [Square1]
    # type = BoundingBoxNodeSetGenerator
    # input = Square
    # bottom_left =  '0.45 -0.05 0'
    # top_right = '0.55 0.05 0'
    # new_boundary = fixed1
    # []
    # [Square2]
    #     type = BoundingBoxNodeSetGenerator
    #     input = Square1
    #     bottom_left =  '0.45 0.45 0'
    #     top_right = '0.55 0.55 0'
    #     new_boundary = fixed2
    #     []


# The primary or dependent variables in the PDES are defined in the VARIABLES BLOCK.
# A user-selected name is assigned to each variable
 
[Variables]
    [temperature]
    []
    [disp_x]
    []
    [disp_y]
    []
[]

[GlobalParams]
    displacements = 'disp_x disp_y'
[]

# The Kernels (individual terms in the PDEs being solved) are listed in the KERNELS BLOCK

[Kernels]
    [heat_conduction]
        type = HeatConduction
        variable = temperature
        block = 'bottom_square top_square'
    []
    [heat_source]
        type = HeatSource
        variable = temperature
        value = 10000
        block = bottom_square
    []
[]

[Modules/TensorMechanics/Master]
    [top_square]
        block = top_square
        add_variables = false
        strain = FINITE
        eigenstrain_names = thermal_eigenstrain
        temperature = temperature
    []
    [bottom_square]
        block = bottom_square
        add_variables = false
        strain = FINITE
        eigenstrain_names = thermal_eigenstrain
        temperature = temperature

    []
[]


# Material properties are defined in the MATERIALS BLOCK. Infarmation from the materials block
# is generally used by some kernels. Here the thermal conductivity is defined for use by the 
# HeatConduction kernel

[Materials]
    [heat_conductor]
        type = HeatConductionMaterial
        thermal_conductivity = 1
        block = 'top_square bottom_square'
    []
    [elasticity_tensor1]
        type = ComputeIsotropicElasticityTensor
        block = 0
        youngs_modulus = 10e6
        poissons_ratio = 0.3
    []
    [thermal_expansion_strain]
        type = ComputeThermalExpansionEigenstrain
        stress_free_temperature = 200
        thermal_expansion_coeff = 1.0e-4
        temperature = temperature
        eigenstrain_name = thermal_eigenstrain
        block = 0
    []
    [stress1]
        type = ComputeFiniteStrainElasticStress
        block = 0
    []
[]


# Boundary conditions are defined in the BCs BLOCK

[BCs]
[leftright_temp]
    type = DirichletBC
    variable = 


    # [leftright_temp]
    #     type = DirichletBC
    #     variable = temperature
    #     boundary = 'left right'
    #     value = 1000
    # []
    # [leftright_disp_x]
    #     type = DirichletBC
    #     variable = disp_x
    #     boundary = 'left'
    #     value = 0
    # []
    # [leftright_disp_y]
    #         type = DirichletBC
    #         variable = disp_y
    #         boundary = 'bottom'
    #         value = 0
    # []
    # [fixed2_disp_x]
    #     type = DirichletBC
    #     variable = disp_x
    #     boundary = fixed2
    #     value = 0
    # []
    # [fixed2_disp_y]
    #     type = DirichletBC
    #     variable = disp_y
    #     boundary = fixed2
    #     value = 0
    # []
    # [fixed1_disp_x]
    #     type = DirichletBC
    #     variable = disp_x
    #     boundary = fixed1
    #     value = 0
    # []
    
[]

[Contact]
    [mechanical]
        model = frictionless
        formulation = mortar
        primary = bottom_square_top
        secondary = top_square_bottom
        c_normal = 1e4
    []
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
    exodus = true
[]

[Postprocessors]
    [peak_temperature]
    type = NodalExtremeValue
    variable = temperature
    []
[]
