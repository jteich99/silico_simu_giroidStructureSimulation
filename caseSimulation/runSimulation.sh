#---Call the OpenFOAM functions
# cd ${0%/*} || exit 1
. $WM_PROJECT_DIR/bin/tools/RunFunctions
#------------------------------

echo ------- Simulation -------

source ../../scripts/bashFunction.sh

mkdir -p include
mkdir -p 0
cp -rf includeSettingsSimulationBase.py includeSettingsSimulation.py
python3 scripts/includeSettingsSimulationTransform.py
source include/includeSettings.sh

rm -rf log*

rm -rf 0/U 0/p

if [ $BC == 'pressure' ] ; then
    cp -r 0.org/U.pressure 0/U
    cp -r 0.org/p.pressure 0/p
elif [ $BC == 'flow' ] ; then
    cp -r 0.org/U.flow 0/U
    cp -r 0.org/p.flow 0/p
fi

mkdir -p constant/polyMesh
cp -rf ../caseMesh/constant/polyMesh/* constant/polyMesh/.

# ---------------------------------------------------------------
echo

startTime=$(date +"%T")
echo decomposePar startTime $startTime

runApplication decomposePar -force

endTime=$(date +"%T")
echo decomposePar endTime $endTime
# ---------------------------------------------------------------

echo

startTime=$(date +"%T")
echo foamRun startTime $startTime

runParallel `getApplication`

endTime=$(date +"%T")
echo foamRun endTime $endTime

# file="log.foamRun"
# while read -r line; do
#     if [[ $line == "SIMPLE solution converged"* ]] ; then
#         echo -e "$line\n"
#     fi
# done <$file 

# ---------------------------------------------------------------
echo 

runApplication reconstructPar -latestTime

echo 
echo ------------------------------------------------

# ---------------------------------------------------------------

rm -rf processor*
