# snappyHexMesh Giroid Meshing Settings Guide
> this guide intends to be a guide to mesh giroids using snappyHexMesh.

## preamble
Prior to configuration of the different "modules" of the snappyHexMeshDict, we must configure the modules to apply when calling snappyHexMesh. For our current development, we set only the first 2:
```c++
castellatedMesh     true;
snap                true;
addLayers           false;
```
Also, due to the settings file used in this directory being in `include/includeSettings`, we have to include before anything:
```c++
#include '../include/includeSettings'
```

The present guide only considers the `castellatedMesh` and `snap` modules. The `addLayers` or *layering* module should be considered in a future update.

## geometry
The geometry has to be set prior to modules setup, in this case we use as a generalization the 'main.stl' as file.
> **future update**: generalize the name of the .stl file from the `includeSettings.py` file to adapt to the input .stl

## castellatedMeshControls
Main controls present in this module:
- **maxLocalCells**: maximum amount of cells that 1 core will have. Set to 90.000.000 as to not limit the meshing process.
- **maxGlobalCells**: maximum amount of cells in total. Set to 90.000.000 as to not limit the meshing process.
- **nCellsBetweenLevels**: amount of cells in between levels. Set to 1.
- **features**: here the *.eMesh* file is informed, and it's level of refinement is set. In theory this should give a different refinement level in edges in the .stl. In reality it only refines the mesh in certain parts of edges without any substantial improvement. **Recommendation: keep same value of level of refinement as general level of refinement**. `level_eMesh` is set in `includeSettings.py`
- **refinementSurfaces**: define surface with which to refine according to distance to it.
- **resolveFeatureAngle**: angle from which, if an angle is less than it, it uses de maximum surface level of refinement to refine cells in that zone. Set to 30.
- **refinementRegions**: define the regions in which refinement will be done. **Important: in our case we want an interior mesh, hence the mode is set to inside.** Most tutorials and base configuration cases have exterior meshes. `level_refinementRegions` is set in `includeSettings.py`
- **insidePoint**: inside point as to differenciate what is inside. **Recommendation: before setting, test in paraView to get an interior point and avoid errors.**. The 3 coordinates of `intPoint` are set in `includeSettings.py`

## snapControls
This is the most important module for our goal. The main controls present are:
- **nFeatureSnapIter**: from [snappyWiki](https://sites.google.com/site/snappywiki/snappyhexmesh/snappyhexmeshdict) *"controls the number of morph iterations within main snapping iterative process, to attract mesh points to surface and avoid sharp edges problems"*. This parameter isn't set in the main tutorials, but is crucial in our case to be able to snap to the outside faces edges. Set to 10 by default.
- **nSmoothPatch**: set to 1 to be able to snap to outside faces edges.
- **tolerance**: distance up to which a point "searches" for the surface to snap. If too small no snapping will happen, if too large, ill snapping will take place, having unwanted spikes. The `snapControls_tolerance` is set in `includeSettings.py`
- **nSolveIter**: set to 1 to be able to snap to outside faces edges.
- **nRelaxIter**: set to 1 to be able to snap to outside faces edges.
- **implicitFeatureSnap**: set to true to use it. It is the "new" method in OpenFOAM that automates the feature snapping. When using **explicitFeatureSnap**, worse meshes are made.
- **explicitFeatureSnap**: set to false in order to use **implicitFeatureSnap**.
- **multiRegionFeatureSnap*: set to false in order to use **implicitFeatureSnap**.


## future updates
- [ ] make an analysis of amount of cells in final mesh in relation with cell length of background mesh made by `blockMesh`.
- [ ] generalize the .stl file name to allow for other file names.
- [ ] 
