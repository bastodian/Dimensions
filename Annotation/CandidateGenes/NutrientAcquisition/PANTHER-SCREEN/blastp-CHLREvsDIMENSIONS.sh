#!/bin/bash

for i in ./uniprot*fst
do
    OUT=${i/fst/blastpVSdimensions}
    blastp \
        -query $i \
        -db DimensionsTaxaCombined.pep \
        -outfmt 6 \
        -evalue 1e-10 \
        -num_threads 24 \
        -out $OUT
    ./BLAST.Parse.Genes.py $OUT DimensionsTaxaCombined.pep > ${i/uniprot_Chlamydomonas/Dimensions}
done
