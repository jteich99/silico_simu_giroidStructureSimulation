set -e # this ensures that the scripts exits on any error, to rpevent unwanted deletes

max=0                       # assuming they're non-negative integers!
for x in processor0/[1-9]* ; do 
    n=${x##*/};                # take just the number so that comparisons work 
    [ "$n" -gt "$max" ] && max=$n 
done
latestTime=$max
for processorNum in $(seq 0 1 7 | tr , .); do
    cd processor$processorNum
    
    for dir in */; do
        if [[ $dir != "$max/" ]]; then
            rm -r $dir
        fi
    done

    cd ..
done
