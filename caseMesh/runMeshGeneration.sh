#!/bin/bash
#---Call the OpenFOAM functions
# cd ${0%/*} || exit 1
. $WM_PROJECT_DIR/bin/tools/RunFunctions
#------------------------------

echo ------- Mesh Creation -------
echo

# source ../../scripts/bashFunction.sh

# includeSettings FILE GENERATION FOR SETUP
rm -rf includeSettingsSnappy.py
mkdir -p include
mkdir -p constant/geometry
mkdir -p constant/triSurface
python3 scripts/getBoxAndIntPoint.py
python3 scripts/includeSettingsSnappyTransform.py

source include/includeSettings.sh

# CLEAN constant, logs AND time DIRECTORIES
rm -rf constant/geometry/*
rm -rf constant/triSurface/*
rm -rf constant/extendedFeatureEdgeMesh/*
rm -rf constant/polyMesh/*
rm -rf log*
rm -rf 0.*
rm -rf processor*

# IF SCALE = on --> SCALE finalFile.stl WITH surfaceConvert AND COPY TO constant/geometry
# IF SCALE = off --> COPY finalFile.stl TO constant/geometry
if [ $scaleOnOff == "on" ];
then
    # surfaceConvert finalFile.stl constant/geometry/finalFile.stl -clean -scale $scale > log.surfaceConvert
    surfaceConvert finalFile.stl constant/triSurface/finalFile.stl -clean -scale $scale > log.surfaceConvert
    echo escalando y copiando finalFile.stl
elif [ $scaleOnOff == "off" ];
then
    # cp finalFile.stl constant/geometry/.
    cp finalFile.stl constant/triSurface/.
    echo copiando finalFile.stl
else
    echo error en seteo de scale on/off
fi

# RUN surfaceFeatures TO CREATE .eMesh FILE
runApplication surfaceFeatureExtract

# ---------------------------------------------------------------
echo

startTime=$(date +"%T")
echo blockMesh startTime $startTime
# RUN blockMesh
runApplication blockMesh || { echo "Error en blockMesh"; exit 1; }
# checkMesh > log.bMcheckMesh

endTime=$(date +"%T")
echo blockMesh endTime $endTime
# ---------------------------------------------------------------
echo

# RUN decomposePar --> snappyHexMesh --> reconstructPar
# runApplication decomposePar -copyZero || { echo "Error en decomposePar"; exit 2; }
runApplication decomposePar -copyZero -force

# ---------------------------------------------------------------
echo

startTime=$(date +"%T")
echo snappy startTime $startTime

echo Running snappyHexMesh
# mpirun -np $nProcs snappyHexMesh -parallel -overwrite > log.snappyHexMesh || { echo "Error en snappyHexMesh"; exit 3; }
runParallel snappyHexMesh -overwrite

endTime=$(date +"%T")
echo snappy endTime $endTime

# ---------------------------------------------------------------
echo

runApplication reconstructParMesh -constant
# checkMesh > log.sHMcheckMesh

# CLEAN processor* DIRECTORIES
rm -rf processor*

# PYTHONS SCRIPT TO GO THROUGH snappy LOG AND GET THE AMOUNT OF CELLS PER STEP IN THE MESHING PROCESS
# python3 scripts/snappyRefinementSampling.py
#
echo
echo ------------------------------------------------

