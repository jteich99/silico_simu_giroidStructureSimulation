function timeDifference {
    t1=($1 $2 $3)
    t2=($4 $5 $6)
    # if the minutes on the first time are less than the ones on the second time
    if (( $((t1[2])) < $((t2[2])) ))
    then
        # add 60 minutes to time 1
        (( t1[2] += 60 ))
        # and subtract an hour
        (( t1[1] -= 1 ))
    fi
    if (( $((t1[1])) < $((t2[1])) ))
    then
        # add 60 minutes to time 1
        (( t1[1] += 60 ))
        # and subtract an hour
        (( t1[0] -= 1 ))
    fi
    # now subtract the hours and the minutes

    H=$(printf "%02d" $((t1[0] -t2[0])))
    M=$(printf "%02d" $((t1[1] -t2[1])))
    S=$(printf "%02d" $((t1[2] -t2[2])))
    
    echo $H:$M:$S
}

function splitTime {
    IFS=":" read -r h m s <<< $1
    h=${h#0}
    m=${m#0}
    s=${s#0}
    local -n t=($h, $m, $s)
    echo $t
}


