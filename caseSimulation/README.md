# directorio para la simulación de la malla creada

### example of `includeSettingsSimulationBase.py`
```python
# NUMBER OF PROCESSOR TO USE
nProcs = 8

# BOUNDARY CONDITION
BC = 'flow' # 'pressure' or 'flow'
value1 = 1.15741e-5 # flow for inlet1
value2 = 1.15741e-5 # flow for inlet2
# total flow = flow1 + flow2

# VISCOSITY
viscosity = 0.01 / 1000

# DENSITY
density = 1000
```

### inputs
> los inputs son cargados en el archivo **includeSettingsSimulation.py**, definiendo las variables como se definen en python

inputs a proveer:
- número de procesadores a utilizar
- tipo de condición de borde a poner en el inlet
    - se tiene implementadas de poner un caudal o poner una presión
- valor de la condición de borde impuesta
    - luego el script `includeSettingsSimulationTransform.py` lo renombra pressure o flow según sea el caso

### outputs
- problema simulado, visualizable en [Paraview](https://www.paraview.org/) abriendo archivo **mesh.foam**.
- en la terminal se pueden observar los tiempos que demoraron cada paso de la simulación, lo cuál podría ser útil para comparar los requerimientos computacionales entre dispositivos, mallas y condiciones de borde.
