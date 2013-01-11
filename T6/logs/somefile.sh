#!/bin/bash

for file in /home/bastodian/DimensionsData/T6/TrimmedData/D[CN]*/*fq.gz
do
    echo $file | sed 's/\/home\/bastodian\/DimensionsData\/T6\/TrimmedData//g'
    gunzip -c $file |  grep -c 'FC'
done >> NumSeqs.trim 

