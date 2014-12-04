#!/bin/bash

for i in ../../uniprot*fst
do
    OUT=${i/fst/blastpVSarabidopsis}
    blastp \
        -query $i \
        -db uniprot-arabidopsis+thaliana.fst \
        -outfmt 6 \
        -evalue 1e-10 \
        -num_threads 24 \
        -out $OUT
    ./BLAST.Parse.Genes.py $OUT uniprot-arabidopsis+thaliana.fst > ${i/uniprot_Chlamydomonas/Arabidopsis}
done
