# SETTINGS FOR SALOME
D = 1.8  # channel diameter [mm]
R = 1.8  # sweep radius [mm]

Nx = 4 # amount of giroids in x direction
Ny = 4 # amount of giroids in y direction
Nz = 4 # amount of giroids in z direction

pyramidLow = False 
pyramidTop = False

quadrant = True

# SETTINGS FOR MESHING
nProcs = 8 # NUMBER OF PROCESSOR TO USE
cell_length = 0.1 / 1000 # CELL LENGTH [m]

# SCALING OF main.stl
scaleOnOff = 'on' # on/off
scale = 1 / 1000

# snappyHexMeshDict SETTINGS
level_eMesh = 1
level_min_refinementSurfaces = 0
level_max_refinementSurfaces = 0
level_refinementRegion = 0
snapControls_tolerance = 1

# SETTINGS FOR SIMULATION
# BOUNDARY CONDITION
# BC = 'pressure' # 'pressure' or 'flow'
BC = 'flow' # 'pressure' or 'flow'
# value = 0.1 # value of flow in inlet [m3/s] or pressure in inlet [Pa]
value = 5.78704e-10 # value of flow in inlet [m3/s] or pressure in inlet [Pa]
# Note: in the includeSettingsTransform scripts the value in [Pa] is converted into [m2/s2] by dividing with the density to give openFoam the rho-normalized pressure.

# VISCOSITY
viscosity =  0.01 / 1000 # kinematic viscosity [m2/s] = dynamic viscosity [Pa s] / density [kg/m3]

# DENSITY
density = 1000 # [kg/m3]
