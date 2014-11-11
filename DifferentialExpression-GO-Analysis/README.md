Differential Expression Analysis and GO annotation
==================================================

Gene family level differential expression
-----------------------------------------

Gene family level differential expression analyses were performed
using edgeR through the Trinity version release 20140717 pipeline.

Count files were obtained from [here](https://github.com/bastodian/Dimensions/tree/master/Annotation/GeneFamily-Annotation/PantherAbundances/GeneFamilyCounts).

Gene family abundances were generated from RSEM gene counts as
documented [here](https://github.com/bastodian/Dimensions/tree/master/Annotation/GeneFamily-Annotation/PantherAbundances).

Additional [documentation](http://trinityrnaseq.sourceforge.net/analysis/diff_expression_analysis.html) is provided through the Trinity sourceforge
repository.

The following is an example of how the necessary count files were generated.

```bash
# Move to the appropriate directory
cd GeneFamilyLevelDE/DC12

# Generate read count files necessary for DE analysis
#
# The following creates the input for the DE analysis comparing biculture 12 (DC12) mapped against
# monoculture 1 (_1) against the mapping of the monoculture (DC10).
trinityrnaseq_r20140717/util/abundance_estimates_to_matrix.pl \
    --est_method RSEM \
    ReadCounts/DC10_R1T6_1 \
    ReadCounts/DC10_R2T6_1 \
    ReadCounts/DC10_R3T6_1 \
    ReadCounts/DC12_R1T6_1 \
    ReadCounts/DC12_R2T6_1 \
    ReadCounts/DC12_R1T6_1

# The following calls edgeR and writes the output to edgeR_DC12vDC10
# 
# DC12vDC10.counts.matrix contains the non-normalized counts and DC12vDC10.described
# contains the description of control and tretment for the comparison
trinityrnaseq_r20140717/Analysis/DifferentialExpression/run_DE_analysis.pl \
    --matrix DC12vDC10.counts.matrix \
    --method edgeR \
    --samples_file DC12vDC10.described \
    --output edgeR_DC12vDC10
```

To facilitate further analysis log fold changes (FC) and false discovery rates
were exracted and combined for every DE experiment.

A [python script](https://github.com/bastodian/Dimensions/blob/master/DifferentialExpression-GO-Analysis/CombineGeneFamilyLevelDE-Results.py) generated the FC and FDR csv files for [log fold changes](https://github.com/bastodian/Dimensions/blob/master/DifferentialExpression-GO-Analysis/CombinedGeneFamilyLevel-LogFC.csv) and [falsediscovery Rates](https://github.com/bastodian/Dimensions/blob/master/DifferentialExpression-GO-Analysis/CombinedGeneFamilyLevel-FDR.csv). 

```bash
# Combine FCs into single csv file
./CombineGeneFamilyLevelDE-Results.py CombinedGeneFamilyLevel-LogFC.csv FC

# Combine FDRs into single csv file
./CombineGeneFamilyLevelDE-Results.py CombinedGeneFamilyLevel-FDR.csv FDR
```
