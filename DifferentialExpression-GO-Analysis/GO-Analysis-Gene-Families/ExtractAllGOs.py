#!/usr/bin/env python

import sys, re

PTHR_Map = sys.argv[1]
GeneFams = sys.argv[2]

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

GO_Terms = {}
with open(GeneFams, 'r') as Families:
    for GeneFamily in Families:
        PTHR_ID = GeneFamily.rstrip()
            # Test if the PTHR ID exists in the Gene Family
            # to GO dictionary
        try:
            GO_Terms[PTHR_ID] = GeneFamilyToGO[PTHR_ID]
        except KeyError:
            continue
            
for PTHR_ID, GO_Terms in GO_Terms.iteritems():
    for Term in GO_Terms:
        sys.stdout.write('%s\t%s\n' % (PTHR_ID, Term))
