import re
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
import os
import sys
from inspect import getsourcefile

file_path = os.path.dirname(os.path.abspath(getsourcefile(lambda:0)))
file_main_dir = os.path.dirname(os.path.dirname(os.path.abspath(getsourcefile(lambda:0))))


sys.path.insert(1, file_main_dir)

import includeSettings as iS

cells = []
faces = []
points = []
iterations = []
counter = 0
with open(file_path + '/log.snappyHexMesh','r') as snappyLog:
    for line in snappyLog:
        if (
            line.startswith('Initial mesh') or
            line.startswith('After refinement') or
            line.startswith('After introducing baffles') or
            line.startswith('Snapped mesh')
        ):
            counter += 1
            iterations.append(counter)
            index_1 = line.find('cells:') + 6
            index_2 = line.find('  faces:')
            index_3 = index_2 + 8
            index_4 = line.find('  points:')
            index_5 = index_4 + 9
            cells.append(int(line[index_1:index_2]))
            faces.append(int(line[index_3:index_4]))
            points.append(int(line[index_5:]))

label_cells = 'Max cells: ' + str(f'{max(cells):,}'.replace(',','.'))
label_faces = 'Max faces: ' + str(f'{max(faces):,}'.replace(',','.'))
label_points = 'Max points: ' + str(f'{max(points):,}'.replace(',','.'))

fig, ax = plt.subplots()
ax.plot(iterations, cells, marker = 'x', color = 'blue', label = label_cells)
plt.xlim([1, max(iterations)])
plt.ylim([0,max(cells)*1.10])
plt.yticks(range(0,max(cells)+100000,100000))
plt.xticks(range(1,max(iterations)+1,2))
plt.legend(loc = 'upper left')
plt.title('Cells vs iterations in snappyHexMesh refinement process', pad = 16.0)
plt.xlabel('Number of iterations')
plt.ylabel('Number of cells')
plt.savefig('cells.png')

fig, ax = plt.subplots()
ax.plot(iterations, faces, marker = 'x', color = 'red', label = label_faces)
plt.xlim([1, max(iterations)])
plt.ylim([0,max(faces)*1.10])
plt.yticks(range(0,max(faces)+500000,500000))
plt.xticks(range(1,max(iterations)+1,2))
plt.legend(loc = 'upper left')
plt.title('Faces vs iterations in snappyHexMesh refinement process', pad = 16.0)
plt.xlabel('Number of iterations')
plt.ylabel('Number of faces')
plt.savefig('faces.png')

fig, ax = plt.subplots()
ax.plot(iterations, points, marker = 'x', color = 'green', label = label_points)
plt.xlim([1, max(iterations)])
plt.ylim([0,max(points)*1.10])
plt.yticks(range(0,max(points)+100000,100000))
plt.xticks(range(1,max(iterations)+1,2))
plt.legend(loc = 'upper left')
plt.title('Points vs iterations in snappyHexMesh refinement process', pad = 16.0)
plt.xlabel('Number of iterations')
plt.ylabel('Number of points')
plt.savefig('points.png')

with open('snappyAnalysis.md','w') as file:
    file.writelines('# snappyHexMesh log analysis:\n\n')

    file.writelines('## snappyHexMeshDict settings:\n')
    file.writelines('- refinement level of eMesh = ' + str(iS.level_eMesh) + '\n')
    file.writelines('- min refinement level of surfaces = ' + str(iS.level_min_refinementSurfaces) + '\n')
    file.writelines('- max refinement level of surfaces = ' + str(iS.level_max_refinementSurfaces) + '\n')
    file.writelines('- refinement level of refinement region = ' + str(iS.level_refinementRegion) + '\n')
    file.writelines('- snapping tolerance = ' + str(iS.snapControls_tolerance) + '\n\n')

    file.writelines('## iterations\n')
    file.writelines('- total number of iterations: ' + str(max(iterations)) + '\n\n')

    file.writelines('## cells\n')
    file.writelines('- initial number of cells: ' + str(cells[0]) + '\n')
    file.writelines('- max number of cells: ' + str(max(cells)) + '\n')
    file.writelines('- final number of cells: ' + str(cells[len(cells)-1]) + '\n\n')
    file.writelines('![cells vs iterations](cells.png)\n')
    
    file.writelines('## faces\n')
    file.writelines('- initial number of faces: ' + str(faces[0]) + '\n')
    file.writelines('- max number of faces: ' + str(max(faces)) + '\n')
    file.writelines('- final number of faces: ' + str(faces[len(faces)-1]) + '\n\n')
    file.writelines('![faces vs iterations](faces.png)\n')

    file.writelines('## points\n')
    file.writelines('- initial number of points: ' + str(points[0]) + '\n')
    file.writelines('- max number of points: ' + str(max(points)) + '\n')
    file.writelines('- final number of points: ' + str(points[len(points)-1]) + '\n\n')
    file.writelines('![points vs iterations](points.png)\n')

with open('snappyAnalysis.csv','w') as file:
    file.writelines(
        str(iS.level_eMesh) + ',' 
        + str(iS.level_min_refinementSurfaces) + ',' 
        + str(iS.level_max_refinementSurfaces) + ','
        + str(iS.level_refinementRegion) + ','
        + str(iS.snapControls_tolerance) + ','
        + str(max(iterations)) + ','
        + str(cells[0]) + ','
        + str(max(cells)) + ','
        + str(cells[len(cells)-1]) + ','
        + str(faces[0]) + ','
        + str(max(faces)) + ','
        + str(faces[len(faces)-1]) + ','
        + str(points[0]) + ','
        + str(max(points)) + ','
        + str(points[len(points)-1])
    )

# fig, ax = plt.subplots()
# fig.subplots_adjust(right=0.75)

# twin1 = ax.twinx()
# twin2 = ax.twinx()

# # Offset the right spine of twin2.  The ticks and label have already been
# # placed on the right by twinx above.
# twin2.spines.right.set_position(("axes", 1.2))

# p1, = ax.plot(iterations, cells, 'blue', label=label_cells , marker = 'x')
# p2, = twin1.plot(iterations, faces, "red", label=label_faces, marker = '.')
# p3, = twin2.plot(iterations, points, "green", label=label_points, marker = 'v')

# ax.set(xlim=(1, max(iterations)), ylim=(0, max(cells)*1.01), xlabel="Iterations", ylabel="Cells")
# twin1.set(ylim=(0, max(faces)*1.01), ylabel="Faces")
# twin2.set(ylim=(0, max(points)*1.05), ylabel="Points")

# ax.yaxis.label.set_color(p1.get_color())
# twin1.yaxis.label.set_color(p2.get_color())
# twin2.yaxis.label.set_color(p3.get_color())

# ax.tick_params(axis='y', colors=p1.get_color())
# twin1.tick_params(axis='y', colors=p2.get_color())
# twin2.tick_params(axis='y', colors=p3.get_color())

# ax.legend(handles=[p1, p2, p3])

# plt.show()
