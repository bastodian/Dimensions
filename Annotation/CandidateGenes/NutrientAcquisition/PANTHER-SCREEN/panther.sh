#!/bin/bash

# Script that runs panther against taxonomically pruned fasta files

for i in ./*pruned.fst
do
    ~/bin/pantherScore1.03/pantherScore.pl \
        -l ~/bin/PANTHER8.1/ \
        -D B \
        -i $i \
        -n \
        -c 24 > ${i/fst/panther}
done
