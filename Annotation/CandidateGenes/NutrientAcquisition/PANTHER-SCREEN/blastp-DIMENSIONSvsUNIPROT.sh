#!/bin/bash

for i in ./Dimensions*fst
do
    OUT=${i/fst/blastpVSuniprot}
    blastp \
        -query $i \
        -db UNIPROT/uniprot_trembl.fasta \
        -outfmt 6 \
        -max_target_seqs 1 \
        -num_threads 24 \
        -out $OUT
done
