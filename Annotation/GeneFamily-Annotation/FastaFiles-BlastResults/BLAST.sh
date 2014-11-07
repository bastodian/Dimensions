#!/bin/bash

UNIPROT=$1
           blastp -num_threads 24 -query ./Chl.fst -db $UNIPROT -max_target_seqs 1 -outfmt 6 -out ./Chl.out -evalue 1e-5 &
nice -n 3  blastp -num_threads 24 -query ./Clo.fst -db $UNIPROT -max_target_seqs 1 -outfmt 6 -out ./Clo.out -evalue 1e-5 &
nice -n 6  blastp -num_threads 24 -query ./Cos.fst -db $UNIPROT -max_target_seqs 1 -outfmt 6 -out ./Cos.out -evalue 1e-5 &
nice -n 9  blastp -num_threads 24 -query ./Pan.fst -db $UNIPROT -max_target_seqs 1 -outfmt 6 -out ./Pan.out -evalue 1e-5 &
nice -n 12 blastp -num_threads 24 -query ./Sce.fst -db $UNIPROT -max_target_seqs 1 -outfmt 6 -out ./Sce.out -evalue 1e-5 &
nice -n 15 blastp -num_threads 24 -query ./Sel.fst -db $UNIPROT -max_target_seqs 1 -outfmt 6 -out ./Sel.out -evalue 1e-5 &
nice -n 18 blastp -num_threads 24 -query ./Sta.fst -db $UNIPROT -max_target_seqs 1 -outfmt 6 -out ./Sta.out -evalue 1e-5 &
nice -n 21 blastp -num_threads 24 -query ./Tet.fst -db $UNIPROT -max_target_seqs 1 -outfmt 6 -out ./Tet.out -evalue 1e-5 &
