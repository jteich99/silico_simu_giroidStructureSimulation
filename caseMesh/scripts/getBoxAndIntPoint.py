import sys
import os
from shutil import copy

current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

copy(f'{parent_directory}/includeSettingsSnappyBase.py', f'{parent_directory}/includeSettingsSnappy.py')

from includeSettingsSnappyBase import *

# GET BOUNDINGS OF ORIGINAL .stl
xBox = [1000,-1000]
yBox = [1000,-1000]
zBox = [1000,-1000]

def checkMinMax(toCheck, boxBound):
    if toCheck > boxBound[1]:
        boxBound[1] = toCheck
    if toCheck < boxBound[0]:
        boxBound[0] = toCheck

with open(f'{parent_directory}/finalFile.stl', 'r') as stlFile:
    for line in stlFile:
        if line.startswith('     vertex'):
            lineValues = line.lstrip('     vertex').rstrip('\n').split(' ')
            while '' in lineValues:
                lineValues.remove('')
            line_x = float(lineValues[0])
            line_y = float(lineValues[1])
            line_z = float(lineValues[2])
            checkMinMax(line_x, xBox)
            checkMinMax(line_y, yBox)
            checkMinMax(line_z, zBox)

# IF scaling=on --> SCALE THE BOUNDINGS
if scaleOnOff == 'on':
    xBox[0] *= scale
    xBox[1] *= scale
    yBox[0] *= scale
    yBox[1] *= scale
    zBox[0] *= scale
    zBox[1] *= scale

xBox[0] -= abs(xBox[1]) * 0.05
yBox[0] -= abs(yBox[1]) * 0.05
zBox[0] -= abs(zBox[1]) * 0.05
xBox[1] += abs(xBox[1]) * 0.05
yBox[1] += abs(yBox[1]) * 0.05
zBox[1] += abs(zBox[1]) * 0.05

blockMeshVertexs = [
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1, 1],
    [ 1, -1, 1],
    [ 1,  1, 1],
    [-1,  1, 1],   
]

with open(f'{parent_directory}/includeSettingsSnappy.py', 'a') as includeSettings:
    for rowNum in range(len(blockMeshVertexs)):
        vertex = blockMeshVertexs[rowNum]
        if vertex[0] == -1:
            includeSettings.writelines(f'vertex{rowNum}_x={xBox[0]}\n')
        elif vertex[0] == 1:
            includeSettings.writelines(f'vertex{rowNum}_x={xBox[1]}\n')
        if vertex[1] == -1:
            includeSettings.writelines(f'vertex{rowNum}_y={yBox[0]}\n')
        elif vertex[1] == 1:
            includeSettings.writelines(f'vertex{rowNum}_y={yBox[1]}\n')
        if vertex[2] == -1:
            includeSettings.writelines(f'vertex{rowNum}_z={zBox[0]}\n')
        elif vertex[2] == 1:
            includeSettings.writelines(f'vertex{rowNum}_z={zBox[1]}\n')


xBoxTrident = [1000,-1000]
yBoxTrident = [1000,-1000]
zBoxTrident = [1000,-1000]

with open(f'{parent_directory}/trident.stl', 'r') as stlFile:
    for line in stlFile:
        if line.startswith('     vertex'):
            lineValues = line.lstrip('     vertex').rstrip('\n').split(' ')
            while '' in lineValues:
                lineValues.remove('')
            line_x = float(lineValues[0])
            line_y = float(lineValues[1])
            line_z = float(lineValues[2])
            checkMinMax(line_x, xBoxTrident)
            checkMinMax(line_y, yBoxTrident)
            checkMinMax(line_z, zBoxTrident)

# IF scaling=on --> SCALE THE BOUNDINGS
if scaleOnOff == 'on':
    xBoxTrident[0] *= scale
    xBoxTrident[1] *= scale
    yBoxTrident[0] *= scale
    yBoxTrident[1] *= scale
    zBoxTrident[0] *= scale
    zBoxTrident[1] *= scale

internalPoint = []
internalPoint.append((xBoxTrident[1] + xBoxTrident[0]) / 2)
internalPoint.append((yBoxTrident[1] + yBoxTrident[0]) / 2)
internalPoint.append((zBoxTrident[1] + zBoxTrident[0]) / 2)

coordinates = ['x', 'y', 'z']

with open(f'{parent_directory}/includeSettingsSnappy.py', 'a') as includeSettings:
    includeSettings.writelines('\n# INTERNAL POINT FOR SNAPPY\n')
    for i in range(len(internalPoint)):
        includeSettings.writelines(f'intPoint_{coordinates[i]} = {internalPoint[i]}\n')
