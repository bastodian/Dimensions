#!/bin/bash

# Extract TPM counts for every Bottle using ParseTPM.py
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

# Extract DE results for every comparison using ParseDE.py
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

# Create summary plots for logFC and FDR values using the 
# PlotsExpression.R script stored in each subfolder; creates
# separate pdf files for each DE comparison
for i in ./*DE_results_A; do ID=`echo $i | awk -F 'v' '{ print $1}'`
    for j in $ID*
    do
        if [[ "$j" == "$ID"* &&  "$j" == *"_B"* ]]
        then
            echo $ID
            Rscript ./PlotsExpression.R $i $j "$ID.DE_results.pdf"
        fi
    done
done


cd ../NutrientAcquisition
for i in ./*DE_results_A; do ID=`echo $i | awk -F 'v' '{ print $1}'`
    for j in $ID*
    do
        if [[ "$j" == "$ID"* &&  "$j" == *"_B"* ]]
        then
            echo $ID
            Rscript ./PlotsExpression.R $i $j "$ID.DE_results.pdf"
        fi
    done
done
