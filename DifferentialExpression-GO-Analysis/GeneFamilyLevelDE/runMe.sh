#!/bin/bash

for i in ./D*/edgeR*/*Rscript
do
    DIR=`echo $i | awk -F '/' '{ print $1"/"$2"/"$3"/"}'`
    SCRIPT=`echo $i | awk -F '/' '{ print "./"$NF}'`
    cd $DIR && \
        pwd && \
        Rscript $SCRIPT \
        && cd /home/bastodian/repos/Dimensions/DifferentialExpression-GO-Analysis/GeneFamilyLevelDE/ \
        && pwd
done
