#!/bin/bash
n=5
for (( i=1; i<=$n; i++ ))
do
   echo "External process: $i"
   sleep 1
done