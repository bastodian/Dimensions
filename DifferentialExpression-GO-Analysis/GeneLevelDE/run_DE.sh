#!/bin/bash

for MATRIX in ./DC*/*counts.matrix
do
    DIR=`echo $MATRIX | awk -F '/' '{ print $2}'`
    COMPARISON=`echo $MATRIX | awk -F '/' '{ print $3 }' | sed 's/.counts.matrix//'`
    /usr/local/src/trinityrnaseq_r20140717/Analysis/DifferentialExpression/run_DE_analysis.pl \
        --matrix $MATRIX \
        --method edgeR \
        --samples_file ${MATRIX/counts\.matrix/described} \
        --output $DIR/edgeR_$COMPARISON
done
