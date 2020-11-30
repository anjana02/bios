#! /usr/bin/env bash 
factorial()
{
NUM=$1
echo $NUM
FACT=1
while [ $NUM -gt 1 ];do
    FACT=$(($FACT * $NUM))
    NUM=$(($NUM - 1))
done
echo $FACT
return $(($FACT))
}

factorial 10