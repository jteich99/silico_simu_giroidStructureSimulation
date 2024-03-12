import sys
import os
from shutil import copy

current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from includeSettingsSnappy import *

with open('include/includeSettings','w') as file:
    file.writelines('// FILE WITH BASE VARIABLES TO BE IMPORTED BY openFoam DICTIONARIES\n \n')
    file.writelines('// NUMBER OF PROCESSOR TO USE\n')
    file.writelines('nProcs ' + str(nProcs) + ';\n')
    
    file.writelines('\n')

    file.writelines('// CORNERS OF blockMeshDict BACKGROUND MESH\n')
    for i in range(8):
        exec(f'x = vertex{i}_x')
        exec(f'y = vertex{i}_y')
        exec(f'z = vertex{i}_z')
        file.writelines(f'vertex{i}_x {x};\n')
        file.writelines(f'vertex{i}_y {y};\n')
        file.writelines(f'vertex{i}_z {z};\n')
    
    file.writelines('\n')

    file.writelines('// AMOUNT OF CELLS IN EACH DIRECTION\n')
    file.writelines('cells_x ' + str(int((vertex1_x - vertex0_x) / cell_length)) + ';\n')
    file.writelines('cells_y ' + str(int((vertex2_y - vertex1_y) / cell_length)) + ';\n')
    file.writelines('cells_z ' + str(int((vertex4_z - vertex3_z) / cell_length)) + ';\n')
    
    file.writelines('\n')

    file.writelines('// INTERNAL POINT FOR SNAPPY\n')
    file.writelines('intPoint_x ' + str(intPoint_x) + ';\n')
    file.writelines('intPoint_y ' + str(intPoint_y) + ';\n')
    file.writelines('intPoint_z ' + str(intPoint_z) + ';\n')

    file.writelines('\n')

    file.writelines('// SNAPPY DICT REFINEMENT LEVEL SETTINGS\n')
    file.writelines('level_eMesh ' + str(level_eMesh) + ';\n')
    file.writelines('level_min_refinementSurfaces ' + str(level_min_refinementSurfaces) + ';\n')
    file.writelines('level_max_refinementSurfaces ' + str(level_max_refinementSurfaces) + ';\n')
    file.writelines('level_refinementRegion ' + str(level_refinementRegion) + ';\n')
    file.writelines('snapControls_tolerance ' + str(snapControls_tolerance) + ';\n')

with open('include/includeSettings.sh', 'w') as file:
    file.writelines('# FILE WITH BASE VARIABLES SOURCED BY runMeshGeneration.sh\n\n')
    file.writelines('# SCALING OF main.stl\n')
    file.writelines('scaleOnOff=' + str(scaleOnOff)+ '\n')
    file.writelines('scale=' + str(scale)+ '\n')

    file.writelines('\n')

    file.writelines('nProcs=' + str(nProcs) + '\n')