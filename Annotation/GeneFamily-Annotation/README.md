Gene Family Annotation of transcriptomes
========================================

Overview
--------

Identify the membership of genes from each transcriptome to gene families
as defined by the [PANTHER database](http://www.pantherdb.org/). Use 
these mappings of genes to gene families to aggregate count values from
RSEM mapping and read abundance estimation.

BLAST searches were used to remove potential contaminant sequences before
performing HMM searches of Panther gene family HMMs against the monocultures
transcripomes.

BLAST and HMM searches are documented in:
* [BLAST and PANTHER HMM searches](https://github.com/bastodian/Dimensions/tree/master/Annotation/GeneFamily-Annotation/Blast-and-Panther-Results)

Summing of read counts across count files are documented in:
* [Gene Family abundance conversion](https://github.com/bastodian/Dimensions/tree/master/Annotation/GeneFamily-Annotation/PantherAbundances)

RSEM count files are stored in:
* [RSEM count files](https://github.com/bastodian/Dimensions/tree/master/Annotation/GeneFamily-Annotation/RSEM)
