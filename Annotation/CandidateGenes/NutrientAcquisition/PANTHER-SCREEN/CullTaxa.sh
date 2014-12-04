#!/bin/bash

# Script to remove contaminants from fasta files

for i in ./Dimensions*blastpVSuniprot
do
    ./Parse.taxa.py $i \
        | grep -A 1 -f /dev/fd/0 ${i/blastpVSuniprot/fst} \
        | perl -pe 's/--\n//g' > ${i/blastpVSuniprot/pruned.fst}
done
