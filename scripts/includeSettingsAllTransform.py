import sys
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from includeSettingsAll import *

with open('includeSettingsSalomeBase.py','w') as iSSalomeFile:
    iSSalomeFile.writelines(
            f'D = {D}\n' + 
            f'R = {R}\n\n' + 
            f'Nx = {Nx}\n' + 
            f'Ny = {Ny}\n' + 
            f'Nz = {Nz}\n' +
            f'pyramidLow = {pyramidLow}\n' +
            f'pyramidTop = {pyramidTop}\n' +  
            f'quadrant = {quadrant}\n' 
            )

with open('includeSettingsSnappyBase.py','w') as iSSnappyFile:
    iSSnappyFile.writelines(
            f'# NUMBER OF PROCESSOR TO USE\n' +
            f'nProcs = {nProcs}\n' + 
            f'\n# CELL LENGTH\n' +
            f'cell_length = {cell_length}\n' +
            f'\n#SCALING OF main.stl\n' +
            f'scaleOnOff = \'{scaleOnOff}\'\n' +
            f'scale = {scale}\n' +
            f'\n# snappyHexMeshDict SETTINGS\n' +
            f'level_eMesh = {level_eMesh}\n' +
            f'level_min_refinementSurfaces = {level_min_refinementSurfaces}\n' +
            f'level_max_refinementSurfaces = {level_max_refinementSurfaces}\n' +
            f'level_refinementRegion = {level_refinementRegion}\n' +
            f'snapControls_tolerance = {snapControls_tolerance}\n' +
            f'\n# CORNERS OF blockMeshDict\n' +
            f'# ES IMPORANTE PONER LAS ESQUINAS EN EL ORDEN QUE CORRESPONDE\n' +
            f'# VER https://www.openfoam.com/documentation/user-guide/4-mesh-generation-and-conversion/4.3-mesh-generation-with-the-blockmesh-utility\n' 
            )

with open('includeSettingsSimulationBase.py','w') as iSSimulationFile:
    iSSimulationFile.writelines(
            f'# NUMBER OF PROCESSOR TO USE\n' +
            f'nProcs = {nProcs}\n' +
            f'\n# BOUNDARY CONDITION\n' + 
            f'BC = \'{BC}\'\n' +
            f'value = {value} # pressure value is in [Pa] and flow value is in [m3/s]\n' +
            f'\n# VISCOSITY\n' + 
            f'viscosity = {viscosity}\n' + 
            f'\n# DENSITY\n' + 
            f'density =  {density}\n'
            )
