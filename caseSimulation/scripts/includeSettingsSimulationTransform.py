import sys
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from includeSettingsSimulation import *

with open('include/includeSettings','w') as file:
    file.writelines('// FILE WITH SETTINGS TO RUN CASE\n\n')
    file.writelines('// NUMBER OF PROCESSOR TO USE\n')
    file.writelines('nProcs ' + str(nProcs) + ';\n\n')

    if BC == 'pressure':
        file.writelines('// FIXED PRESSURE IN INLET BOUNDARY CONDITION\n')
        file.writelines(f'pressure {value / density};\n')
    elif BC == 'flow':
        file.writelines('// FIXED FLOW IN INLET BOUNDARY CONDITION\n')
        file.writelines(f'flow {value};\n')
    
    file.writelines('\n// VISCOSITY\n')
    file.writelines(f'viscosity {viscosity};\n')

    file.writelines('\n// DENSITY\n')
    file.writelines(f'density {density};\n')

with open('include/includeSettings.sh', 'w') as file:
    file.writelines('# NUMBER OF PROCESSOR TO USE\n')
    file.writelines('nProcs=' + str(nProcs) + '\n\n')

    file.writelines(f'BC={BC}\n')





