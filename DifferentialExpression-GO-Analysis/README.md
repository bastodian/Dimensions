Differential Expression Analysis and GO annotation
==================================================

[Gene family level differential expression](https://github.com/bastodian/Dimensions/tree/master/DifferentialExpression-GO-Analysis/GeneFamilyLevelDE)
-----------------------------------------------------------------------------------------------------------------------------------------------------

Gene family level differential expression analyses were performed
using [edgeR](http://www.bioconductor.org/packages/release/bioc/html/edgeR.html) through the [Trinity](http://trinityrnaseq.sourceforge.net/) version release 20140717 pipeline.

Count files were obtained from [here](https://github.com/bastodian/Dimensions/tree/master/Annotation/GeneFamily-Annotation/PantherAbundances/GeneFamilyCounts).

Gene family abundances were generated from RSEM gene counts as
documented [here](https://github.com/bastodian/Dimensions/tree/master/Annotation/GeneFamily-Annotation/PantherAbundances).

Additional [documentation](http://trinityrnaseq.sourceforge.net/analysis/diff_expression_analysis.html) is provided through the Trinity sourceforge
repository.

The following is an example of how the necessary count files were generated and how
the edgeR analysis was performed. Yes, did this by hand and I hacked the Perl wrapper 
packaged with Trinity to get it to work with the unexpected data...

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

### IMPORTANT ###
# To make the Trinity wrapper (abundance_estimates_to_matrix.pl) work with the transformed
# Panther gene counts it needs to be modified.
#
# The following keys on lines 85-92 need to be changed from:
0       transcript_id
1       gene_id
2       length
3       effective_length
4       expected_count
5       TPM
6       FPKM
7       IsoPct
### to:
0       gene_id
1       length
2       effective_length
3       expected_count
4       TPM
5       FPKM
# Lastly, line 129 needs to read:
$counts_field = 3;
```

Once the count files are prepared the differential expression analysis can be re-run using the 
following loop.

```bash
cd ./GeneFamilyLevelDE

for MATRIX in ./DC*/*counts.matrix
do
    # What directory are we on?
    DIR=`echo $MATRIX | awk -F '/' '{ print $2}'`
    # Create the prefix for the comparison (eg, DC12vDC10) by stripping the file
    # extension from the counts.matrix file
    COMPARISON=`echo $MATRIX | awk -F '/' '{ print $3 }' | sed 's/.counts.matrix//'`
    # run the differential expression wrapper packaged with trinity; specify the
    # appropriate path to the trinity relaease directory
    trinityrnaseq_r20140717/Analysis/DifferentialExpression/run_DE_analysis.pl \
        --matrix $MATRIX \
        --method edgeR \
        # Which file describes the treatments to group replicates?
        --samples_file ${MATRIX/counts\.matrix/described} \
        --output $DIR/edgeR_$COMPARISON
done
```

To facilitate further analysis log fold changes (FC) and false discovery rates
were exracted and combined for every DE experiment.

A [python script](https://github.com/bastodian/Dimensions/blob/master/DifferentialExpression-GO-Analysis/CombineGeneFamilyLevelDE-Results.py) generated the FC and FDR csv files for [log fold changes](https://github.com/bastodian/Dimensions/blob/master/DifferentialExpression-GO-Analysis/CombinedGeneFamilyLevel-LogFC.csv) and [false discovery Rates](https://github.com/bastodian/Dimensions/blob/master/DifferentialExpression-GO-Analysis/CombinedGeneFamilyLevel-FDR.csv). 

```bash
# Combine FCs into single csv file
./CombineGeneFamilyLevelDE-Results.py CombinedGeneFamilyLevel-LogFC.csv FC

# Combine FDRs into single csv file
./CombineGeneFamilyLevelDE-Results.py CombinedGeneFamilyLevel-FDR.csv FDR
```

[Gene Level Differential Expression](https://github.com/bastodian/Dimensions/tree/master/DifferentialExpression-GO-Analysis/GeneLevelDE)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Write me...

[Gene Ontology Analysis](https://github.com/bastodian/Dimensions/tree/master/DifferentialExpression-GO-Analysis/GO-Analysis-Gene-Families)
------------------------------------------------------------------------------------------------------------------------------------------

Write me...

[Candidate Gene Analysis](https://github.com/bastodian/Dimensions/tree/master/DifferentialExpression-GO-Analysis/CandidateGenes)
--------------------------------------------------------------------------------------------------------------------------------

Write me...
