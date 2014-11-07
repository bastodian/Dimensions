#!/bin/bash

# DEPENDENCIES:
#
# A specific custom version of Uniprot available at:
#
#
# screed: https://github.com/ctb/screed
#
# Panther version 8.1 installed in the following locations:
# 
# ~/bin/pantherScore1.03/pantherScore.pl <- the program
# ~/bin/PANTHER8.1 <- the database

UNIPROT_DB=$1

# First runs a BLAST against Uniprot Custom database that contains
# sprot and trembl for fungi and plants obtained on August 30 2013
#
# sprot and trembl files were combined to create a taxonomic filter
# in which only the best BLAST hits that hit a 'green' taxon (alga or
# plant). All 'green' sequence IDs were extracted and are stored in
# plantIDs


# BLAST.sh will BLAST Taxon.fst against Uniprot and creates Taxon.out
# that contains the BLAST hits
./BLAST.sh $UNIPROT_DB

# After BLAST searches are done use the *.out BLAST reports to filter
# protein fasta files retaining only 'green' sequences
./SubsetFastaForPanther.py

# Run Panther HMMs against the pruned fasta files (*.algal.fst) and
# write output to *.algal.panther
./Panther.sh
