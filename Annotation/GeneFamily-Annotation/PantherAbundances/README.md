Gene Family Abundance Estimation
================================

Individual gene family count files
----------------------------------

Based on gene to PANTHER family ID mappings I created 187 gene family count files 
using a [script](https://github.com/bastodian/Dimensions/blob/master/Annotation/GeneFamily-Annotation/PantherAbundances/PantherAbundanceConvert.py) that sums RSEM counts from all genes predicted to belong to a gene family.

Transformed RSEM count files can be found [here](https://github.com/bastodian/Dimensions/tree/master/Annotation/GeneFamily-Annotation/PantherAbundances/GeneFamilyCounts).
The individual log file document which gene (comp_X_cX)was assigned to which gene
family (PTHR ID).

Files are named as follows: DC12_R1T6_1 is biculture containing species 1 and 2
mapped against species 1. DC12_R1T6_2 is the same biculture mapped against species
2.

Combined count matrix in CSV format
----------------------------------

The following [script](https://github.com/bastodian/Dimensions/blob/master/Annotation/GeneFamily-Annotation/PantherAbundances/CombinedPantherCounts.py) combines gene family counts from the 187 separate count files 
into two single spreadsheets: one that contains [TPM counts](https://github.com/bastodian/Dimensions/blob/master/Annotation/GeneFamily-Annotation/PantherAbundances/Counts-CSV/TPM-Counts.csv) and a second that
contains the [expected counts](https://github.com/bastodian/Dimensions/blob/master/Annotation/GeneFamily-Annotation/PantherAbundances/Counts-CSV/Expected-Counts.csv) (ie, raw counts under the expectation maximization
algorithm implemented in RSEM).

How to recreate the count files?
--------------------------------

To recreate the csv files uncompress the RSEM count files first followed by calling the python
scripts again.

```bash
for File in ../RSEM/*
do
    gunzip $File
done

./PantherAbundanceConvert.py

./CombinedPantherCounts.py Counts-CSV/TPM-Counts.csv TPM

./CombinedPantherCounts.py Counts-CSV/Expected-Counts.csv ExpectedCount
```
