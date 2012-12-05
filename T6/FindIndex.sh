#!/bin/bash

: <<'!'
    This script searches for the 5 prime part of the Truseq index adapter and then 
    cuts the 8 characters following it out of the seqeunce. I keep the most abundant
    8-mer.

    FindIndex.sh PATH/TO/DATA OUTFILE
!

INPATH=$1

for file in ${INPATH}D[CN]*/*1.fq.gz
do
    echo $file
    gunzip -c $file |\
        awk '{for(i=1;i<=NF;i++){if($i~/^GATCGGAAGAGCACACGTCTGAACTCCAGTCAC/){print $i}}}' |\
        cut -c34-41 |\
        sort |\
        uniq -c |\
        sort -r |\
        head -n 1
done 
