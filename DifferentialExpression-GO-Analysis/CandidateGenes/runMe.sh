#!/bin/bash

# Extract TPM counts for every Bottle
echo `pwd`
cd NutrientAcquisition/
echo `pwd`
for i in ../../../Annotation/GeneFamily-Annotation/RSEM/D*
do
    ../ParseTPM.py $i
done

cd ../Facilitation
echo `pwd`
for i in ../../../Annotation/GeneFamily-Annotation/RSEM/D*
do
    ../ParseTPM.py $i
done

# Extract DE results for every comparison
echo `pwd`
cd ../NutrientAcquisition/
echo `pwd`
for i in ../../GeneLevelDE/DC*/edgeR_*/*.counts.matrix.condA_vs_condB.edgeR.DE_results
do
    ../ParseDE.py $i
done

cd ../Facilitation
echo `pwd`
for i in ../../GeneLevelDE/DC*/edgeR_*/*.counts.matrix.condA_vs_condB.edgeR.DE_results
do
    ../ParseDE.py $i
done
