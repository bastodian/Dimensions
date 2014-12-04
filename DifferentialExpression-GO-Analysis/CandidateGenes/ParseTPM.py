#!/usr/bin/env python

'''
    Parses gene level counts from RSEM count matrices (input file) and writes 
    summary to a new file. IMPORTANT: Files Sp1.Key-SpN.Key need to be present so that 
    gene IDs can be linked to Panther IDs
'''

import sys

TPMcounts = sys.argv[1]

InFile = TPMcounts.split('/')[-1].split('.')
TPMout = '%s.%s_%s' % (InFile[0], InFile[1], InFile[-1])
GeneIDs = 'Sp%s.Key' % (TPMcounts.split('.')[-1])

# First set up a dictionary that looks as follows:
# {CompID:[PantherID]}
GeneDict = {}
with open(GeneIDs, 'rU') as GeneFile:
    for Line in GeneFile:
        CompID = Line.split()[0]
        PantherID = Line.split()[1]
        GeneDict[CompID] = []
        GeneDict[CompID].append(PantherID)

# Then add TPM counts:
# {CompID:[PantherID, TPM]}
with open(TPMcounts, 'rU') as TPMfile:
    for Line in TPMfile:
        if'TPM' not in Line:
            try:
                GeneDict[Line.split()[0]].append(Line.split()[-2])
            except KeyError:
                continue

# The gene dictionary makes it difficult to write sorted output. Let's
# transform it to:
# {PantherID:[[CompID, TPM],[CompID, TPM]]}
NewGeneDict = {}
for CompID, Values in GeneDict.iteritems():
    PantherID = Values[0]
    TPM = Values[1]
    try:
        NewGeneDict[PantherID].append([CompID, TPM])
    except KeyError:
        NewGeneDict[PantherID] = []
        NewGeneDict[PantherID].append([CompID, TPM])

# Extract all PantherIDs from the NewGeneDict and sort the list
# so that it can be used to write ordered output
PantherList = []
for PantherID, Values in NewGeneDict.iteritems():
    PantherList.append(PantherID)
PantherList = sorted(PantherList)

# Now for writing the output
# In essende use the sorted keys dict (PantherList) to access
# the NewGeneDict in a sorted manner
with open(TPMout, 'w') as TPMoutfile:
    TPMoutfile.write('%s,%s,%s\n' % ('Function', 'GeneID', 'TPM'))
    for Panther in PantherList:
        for CompCount in NewGeneDict[Panther]:
            TPMoutfile.write('%s,%s\n' % (Panther, '\t'.join(CompCount)))
