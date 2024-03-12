#!/bin/bash
#---Call the OpenFOAM functions
# cd ${0%/*} || exit 1
. $WM_PROJECT_DIR/bin/tools/RunFunctions
#------------------------------

mkdir -p cases

echo Nombre del directorio a crear: 
read directoryName

while [ -d $directoryName ]
do
  echo El directorio elegido ya existe
  echo Desea reemplazar? [y/n] 
  read replace
  if [ $replace == y ]
  then
    rm -rf $directoryName
  else
    echo Nombre del directorio a crear
    read directoryName
  fi
done
    
mkdir $directoryName
cp -r salomeGeometry $directoryName/caseGeometry
cp -r baseMesh $directoryName/caseMesh
cp -r baseSimulation $directoryName/caseSimulation

echo
echo Generar includeSettings para cada directorio a partir de includeSettingsAll? [y/n] 
read iSTransform

if [ $iSTransform == y ]
then
  python3 scripts/includeSettingsAllTransform.py
  mv includeSettingsSalomeBase.py $directoryName/caseGeometry/includeSettingsSalomeBase.py
  mv includeSettingsSnappyBase.py $directoryName/caseMesh/includeSettingsSnappyBase.py
  mv includeSettingsSimulationBase.py $directoryName/caseSimulation/includeSettingsSimulationBase.py
  cp includeSettingsAll.py $directoryName/. 
fi

echo
echo 'Correr geometry -> meshing -> simulation? [y/n] '
read run

if [ $run == 'y' ]
then
    cd cases
    mv ../$directoryName .
    cd $directoryName

    echo
    # echo running geometry generation
    cd caseGeometry
    bash ./runSalome.sh

    echo
    # echo running mesh generation
    cd ../caseMesh
    cp ../caseGeometry/finalFile.stl .
    cp ../caseGeometry/trident.stl .
    bash ./runMeshGeneration.sh

    echo
    # echo running simulation
    cd ../caseSimulation
    bash ./runSimulation.sh

    cd ..
fi
