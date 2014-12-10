Candidate Gene Summaries
=========================

TPM counts
----------

TPM counts for each gene were extracted from RSEM count files and saved
in two separate folders: "Facilitation" and "Nutrient Acquisition". Within 
these folders the following files contain counts:

DC12.R1T6_1
DC12.R1T6_2
...

Here DC12 refers to the comparison of species 1 with species 2. R1T6 indicates
that this is replicate 1 of timepoint 6. Underscore 1 and 2 indicate which reference
transcriptome the short read fastq file was mapped against; species 1 or species 2. 
The remainder of the files are named accordingly. There should be 187 count files in
each folder.

Differential Expression Results
-------------------------------

Select genes were extracted from a gene level edgeR differential expression analysis
(stored in ../GeneLevelDE/). log2 fold change (logFC), log counts per million (averaged 
counts across replicates), and false discovery rates (FDR) were extracted and stored in
the "Facilitation" and "Nutrient Acquisition" folders. The files of interest are as follows:

DC12vDC10.DE_results_A
DC12vDC20.DE_results_B
...

Here DC12vDC10 refers to the comparison. Ie, the expression levels in the biculture containing 
species 1 and 2 are compared to expression levels in monoculture 1. DC12vDC20 compares expression
to monoculture 2.

Data exploration
----------------

Logged fold changes were plotted for every gene of interest (stored in pdf files). For example 
DC12.DE_results.pdf contains a summary of the DE results for both comparisons of species 1 and 2
to their respective monocultures. In each plot circles represent the first species in the name 
(here 1) while squares represent the second species (here 2). Solid symbols indicate FDR < 0.05.

Scripts
-------

All analyses can be rerun by calling the runMe script; cleanMe should remove the data.

```bash
./runMe.sh
```
