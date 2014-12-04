#!/bin/bash

for i in ./*fasta
do
    tblastx -query ChlamyVitaminQueries.fst -db $i -evalue 1e-20 -num_threads 24 -outfmt 7 > ${i/fasta/BLAST}
done
