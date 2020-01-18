#!/bin/bash

rm 16/*

lines=`wc -l hightemp.txt | cut -f 1 -d " "`
l=`expr $lines / $n`
remainder=`expr $count % $n`

if [ $remainder -eq 0 ]; then
    split --lines=$l --numeric-suffixes=1 --additional-suffix=.txt 16/hightemp_

else
    l=`expr $l + 1`
    h=`expr $l * $remainder`
    !head -n $ hightemp.txt | split --lines=$l --numeric-suffixes=1 --additional-suffix=.txt - 16/hightemp_

    t=`expr $lines - h`
    l=`expr l - 1`
    d=`expr remainder + 1`
    tail -n $t hightemp.txt | split --lines=$l --numeric-suffixes=$d --additional-suffix=.txt - 16/hightemp_
fi

