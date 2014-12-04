#!/usr/bin/env python

'''
Screen uniprot BLAST hits against green taxa to remove contaminants
'''

import sys

BLASTfile = sys.argv[1]

taxa = []

with open('./plantTaxa', 'rU') as taxonfile:
    for line in taxonfile:
        taxa.append(line.rstrip())

with open(BLASTfile, 'rU') as infile:
    GeneList = []
    for line in infile:
        if ''.join([x for x in line.split()[1].split('.') if 'OS=' in x]) in taxa:
            GeneList.append(line.split()[0])
            
for item in GeneList:
    print item
