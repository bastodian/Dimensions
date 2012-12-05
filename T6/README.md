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
