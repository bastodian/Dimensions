#!/bin/bash
#
## Extract TPM counts for every Bottle
#echo `pwd`
#cd NutrientAcquisition/
#echo `pwd`
#for i in ../../../Annotation/GeneFamily-Annotation/RSEM/D*
#do
#    ../ParseTPM.py $i
#done
#
#cd ../Facilitation
#echo `pwd`
#for i in ../../../Annotation/GeneFamily-Annotation/RSEM/D*
#do
#    ../ParseTPM.py $i
#done

## Extract DE results for every comparison
#echo `pwd`
##cd ../NutrientAcquisition/
#cd ./NutrientAcquisition/
#echo `pwd`
#for i in ../../GeneLevelDE/DC*/edgeR_*/*.counts.matrix.condA_vs_condB.edgeR.DE_results
#do
#    ../ParseDE.py $i
#done
#
#cd ../Facilitation
#echo `pwd`
#for i in ../../GeneLevelDE/DC*/edgeR_*/*.counts.matrix.condA_vs_condB.edgeR.DE_results
#do
#    ../ParseDE.py $i
#done

cd Facilitation
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
