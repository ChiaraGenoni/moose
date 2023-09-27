
import os

mesh_refinement = [0, 1, 2, 3]
for i in mesh_refinement:
    print(i)
    command_line = 'mpiexec -n 8 ~/projects/moose/modules/combined/combined-opt -i model_pellets.i --allow-unused Mesh/uniform_refine=' + str(i) + " Outputs/file_base=output_" + str(i) 
    os.system(command_line)



