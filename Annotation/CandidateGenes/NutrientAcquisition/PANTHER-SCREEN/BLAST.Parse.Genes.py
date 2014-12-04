#!/usr/bin/env python

"""
Script to parse Blast results file and extract genes from fasta
"""

import sys, screed

BLASTresult = sys.argv[1]
FastaFile = sys.argv[2]
Contigs = []

with open(BLASTresult, 'rU') as infile:
    for line in infile:
        if '#' not in line:
            Contigs.append(line.split()[1])

for n, record in enumerate(screed.open(FastaFile)):
    if record['name'] in set(Contigs):
        print '>%s\n%s' %  (record['name'], record['sequence'])
