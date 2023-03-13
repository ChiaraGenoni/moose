
# The FEM mesh is defined in the MESH BLOCK. A mesh can be read in from a file (typically Exodus format). 
# In the following an internal mesh-generator is used. 
# The sides of the domain are named as bottom, top ,left, right, front and back

[Mesh]
    [Square]
        type = GeneratedMeshGenerator
        dim = 2
        nx = 10
        ny = 10
    []
[]

# The primary or dependent variables in the PDES are defined in the VARIABLES BLOCK.
# A user-selected name is assigned to each variable
 
[Variables]
    [temperature]
    []
[]

# The Kernels (individual terms in the PDEs being solved) are listed in the KERNELS BLOCK

[Kernels]
    [heat_conduction]
        type = HeatConduction
        variable = temperature
    []
    [heat_source]
        type = HeatSource
        variable = temperature
        value = 10000
    []
[]

# Material properties are defined in the MATERIALS BLOCK. Infarmation from the materials block
# is generally used by some kernels. Here the thermal conductivity is defined for use by the 
# HeatConduction kernel

[Materials]
    [heat_conductor]
        type = HeatConductionMaterial
        thermal_conductivity = 1
        block = 0
    []
[]

# Boundary conditions are defined in the BCs BLOCK

[BCs]
    [leftright]
        type = DirichletBC
        variable = temperature
        boundary = 'left right'
        value = 200
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
