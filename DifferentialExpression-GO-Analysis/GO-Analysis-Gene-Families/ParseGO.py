#!/usr/bin/env python

import sys, re

PTHR_Map = sys.argv[1]
DE_Results = sys.argv[2]

# Iterate over the PTHR to GO map once and extract all panther
# family IDs. Every PTHR ID will form a key in a Panther to GO
# dictionary. Here, I just want to ceate a dictionary of empty
# lists to be populated later
GeneFamilyToGO = {}
with open(PTHR_Map, 'r') as GO_Mapping:
    for Line in GO_Mapping:
        PTHR_ID = Line.split()[1].split(':')[0]
        GeneFamilyToGO[PTHR_ID] = []

# Iterate over the PTHR to GO map again and map the GO terms
# to the PTHR ID dictionary
pattern = re.compile('GO:\d+')
with open(PTHR_Map, 'r') as GO_Mapping:
    for Line in GO_Mapping:
        PTHR_ID = Line.split()[1].split(':')[0]
        GO_Terms = pattern.findall(Line)
        for Term in GO_Terms:
            GeneFamilyToGO[PTHR_ID].append(Term)

#for PTHR_ID, GO_Terms in GeneFamilyToGO.iteritems():
#    GeneFamilyToGO[PTHR_ID] = list(set(GO_Terms))
#    for Term in GO_Terms:
#        sys.stdout.write('%s\t%s\n' % (PTHR_ID, Term))

UpRegulated = {}
DownRegulated = {}
with open(DE_Results, 'r') as DE:
    for Line in DE:
        try:
            PTHR_ID = Line.split()[0]
            # Test if the PTHR ID exists in the Gene Family
            # to GO dictionary
            GeneFamilyToGO[PTHR_ID]
            try:
                LogFC = float(Line.split()[1])
                FDR = float(Line.split()[4])
                if LogFC >= 1 and FDR <= 0.05:
                    UpRegulated[PTHR_ID] = GeneFamilyToGO[PTHR_ID]
                elif LogFC <= -1 and FDR <= 0.05:
                    DownRegulated[PTHR_ID] = GeneFamilyToGO[PTHR_ID]
            except ValueError:
                continue
        except KeyError:
            continue

for PTHR_ID, GO_Terms in UpRegulated.iteritems():
    for Term in GO_Terms:
            sys.stdout.write('%s\t%s\n' % (PTHR_ID, Term))

for PTHR_ID, GO_Terms in DownRegulated.iteritems():
    for Term in GO_Terms:
            sys.stderr.write('%s\t%s\n' % (PTHR_ID, Term))
