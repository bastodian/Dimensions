#!/bin/bash

for i in ./*fasta
do
    grep -v '#' ${i/fasta/BLAST} | \
        awk '{ print $2}' | \
        sort -u | \
        grep -A 1 -f /dev/fd/0 $i | \
        perl -pe 's/--\n//g' > temp.fst 
    blastx -query ./temp.fst -db /home/bastodian/DimensionsData/T6/Annotation/PANTHER/SCRATCH/UNIPROT/uniprot_trembl.fasta -outfmt 7 -num_threads 24 -max_target_seqs 1 > ./temp
    ./Parse.taxa.py temp > ${i/fasta/Facilitation}
    rm temp && rm temp.fst
done
