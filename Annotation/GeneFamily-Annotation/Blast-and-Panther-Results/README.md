BLAST and Panther searches
==========================

Removal of poetntial contaminants
---------------------------------

BLAST every fasta file against a Uniprot Custom database that contains
sprot and trembl for fungi and plants (obtained on August 30 2013). 

Sprot and Trembl files were combined to create a taxonomic filter in which 
only the best BLAST hits that hit a 'green' taxon (alga or plant) are 
retained. 

All 'green' sequence IDs were extracted and are stored in [plantIDs]()_

```bash
#BLAST.sh will BLAST Taxon.fst against Uniprot and creates Taxon.out

./BLAST.sh Uniprot.db
```

```bash
~/bin/pantherScore1.03/pantherScore.pl <- the program
~/bin/PANTHER8.1 <- the database
```





# After BLAST searches are done use the *.out BLAST reports to filter
# protein fasta files retaining only 'green' sequences
./SubsetFastaForPanther.py

# Run Panther HMMs against the pruned fasta files (*.algal.fst) and
# write output to *.algal.panther
./Panther.sh

