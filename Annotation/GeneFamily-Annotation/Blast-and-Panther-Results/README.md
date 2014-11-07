BLAST and Panther searches
==========================

Removal of poetntial contaminants
---------------------------------

BLAST every fasta file against a Uniprot Custom database that contains
sprot and trembl for fungi and plants (obtained on August 30 2013). 

Sprot and Trembl files were combined to create a taxonomic filter in which 
only the best BLAST hits that hit a 'green' taxon (alga or plant) are 
retained. 

All 'green' sequence IDs were extracted and are stored in [plantIDs](https://github.com/bastodian/Dimensions/blob/master/Annotation/GeneFamily-Annotation/Blast-and-Panther-Results/plantIDs)

```bash
#BLAST.sh will BLAST Taxon.fst against Uniprot and creates Taxon.out

./BLAST.sh Uniprot.db

# After BLAST searches are done the Taxon.out BLAST reports are used to 
# filter protein fasta files retaining only 'green' sequences which 
# creates Taxon.algal.fst files

./SubsetFastaForPanther.py
```

Identification of gene families
-------------------------------

Panther HMMs are scanned against the taxonomically filteres sequence file (algal.fst)
and the outputs are written to algal.panther files. This creates a mapping of 
gene family (Panther) ID to gene ID (compID).


```bash
# The following Panther database dependencies were hardcoded:
#
# ~/bin/pantherScore1.03/pantherScore.pl <- the program
# ~/bin/PANTHER8.1 <- the database

# Run Panther HMMs against the pruned fasta files (Taxon.algal.fst) 
# and results to Taxon.algal.panther

./Panther.sh
```
