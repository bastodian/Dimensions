Analysis of final time point of experiment (T6)
===============================================

Overview
--------

We received libraries from 200 samples for the analysis of the final timepoint
of the experiment.

Initial QC
----------

The quality of all libraries was assessed using FASTQC. I counted the sequences in all
libraries using the following command:

    for file in /mnt/pond/BGIhdd/F12FPCUSAT0183_ALGjhnT/Data/D[CN]*/*1.fq.gz
    do 
        echo $file | sed 's/\/mnt\/pond\/BGIhdd\/F12FPCUSAT0183_ALGjhnT\/Data\///g'
        gunzip -c $file |  grep -c 'FC'
    done >> NumSeqs.raw 

In addition, I was interested in figuring out what the sequence of the index used by
BGI for multiplexing was, so that I could include that sequence in downstream clean ups
of the data. From previous work with BGI data I knew to expect an 8-mer rather than the 
standard Illumina 6-mer. I could only find adapter and primer sequences in the test batch 
of 8 samples we sequenced prior to the remainder of the batch for T6.

The following code was used to retrieve the adapter sequence:

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

This yields the following 8 index sequences:

    GTCCGCAC
    ACAGTGAT
    GTGAAACG
    GTGGCCTT
    GTTTCGGA
    GCCAATAT
    TGACCAAT
    ATCACGAT
