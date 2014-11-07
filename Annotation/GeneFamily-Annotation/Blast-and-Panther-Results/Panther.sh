#!/bin/bash

# Script that runs panther against taxonomically pruned fasta files

~/bin/pantherScore1.03/pantherScore.pl \
        -l ~/bin/PANTHER8.1/ \
        -D B \
        -i ./Chl.algal.fst \
        -n \
        -c 24 > Chl.algal.panther &

nice -n 3 \
    ~/bin/pantherScore1.03/pantherScore.pl \
        -l ~/bin/PANTHER8.1/ \
        -D B \
        -i ./Clo.algal.fst \
        -n \
        -c 24 > Clo.algal.panther &

nice -n 6 \
    ~/bin/pantherScore1.03/pantherScore.pl \
        -l ~/bin/PANTHER8.1/ \
        -D B \
        -i ./Cos.algal.fst \
        -n \
        -c 24 > Cos.algal.panther &

nice -n 9 \
    ~/bin/pantherScore1.03/pantherScore.pl \
        -l ~/bin/PANTHER8.1/ \
        -D B \
        -i ./Pan.algal.fst \
        -n \
        -c 24 > Pan.algal.panther &

nice -n 12 \
    ~/bin/pantherScore1.03/pantherScore.pl \
        -l ~/bin/PANTHER8.1/ \
        -D B \
        -i ./Sce.algal.fst \
        -n \
        -c 24 > Sce.algal.panther &

nice -n 15 \
    ~/bin/pantherScore1.03/pantherScore.pl \
        -l ~/bin/PANTHER8.1/ \
        -D B \
        -i ./Sel.algal.fst \
        -n \
        -c 24 > Sel.algal.panther &

nice -n 18 \
    ~/bin/pantherScore1.03/pantherScore.pl \
        -l ~/bin/PANTHER8.1/ \
        -D B \
        -i ./Sta.algal.fst \
        -n \
        -c 24 > Sta.algal.panther &

nice -n 21 \
    ~/bin/pantherScore1.03/pantherScore.pl \
        -l ~/bin/PANTHER8.1/ \
        -D B \
        -i ./Tet.algal.fst \
        -n \
        -c 24 > Tet.algal.panther
