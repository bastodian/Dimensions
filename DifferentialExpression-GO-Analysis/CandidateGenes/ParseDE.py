#!/usr/bin/env python

'''
    Parses gene level counts DE results from edgeR analysis and writes them to 
    a new file. IMPORTANT: Files Sp1.Key-SpN.Key need to be present so that 
    gene IDs can be linked to Panther IDs
'''

import sys

DEresults = sys.argv[1]

InFile = DEresults.split('/')[-1].split('.')
DEout = '%s.%s' % (InFile[0], InFile[-1])
if DEout[2] == DEout[7]:
    DEout = '%s_A' % DEout
elif DEout[2] != DEout[7]:
    DEout = '%s_B' % DEout
GeneIDs = 'Sp%s.Key' % (InFile[0][-2])

# First set up a dictionary that looks as follows:
# {CompID:[PantherID]}
GeneDict = {}
with open(GeneIDs, 'rU') as GeneFile:
    for Line in GeneFile:
        CompID = Line.split()[0]
        PantherID = Line.split()[1]
        GeneDict[CompID] = []
        GeneDict[CompID].append(PantherID)

# Then add DE results:
# {CompID:[PantherID, logFC, logCPM, FDR]}
with open(DEresults, 'rU') as EdgeR:
    for Line in EdgeR:
        if 'logFC' not in Line:
            try:
                CompID = Line.split()[0]
                logFC = Line.split()[1]
                logCPM = Line.split()[2]
                FDR = Line.split()[-1]
                for i in logFC, logCPM, FDR:
                    GeneDict[CompID].append(i)
            except KeyError:
                continue
## The gene dictionary makes it difficult to write sorted output. Let's
## transform it to:
## {PantherID:[[CompID, logFC, logCPM, FDR],[CompID, logFC, logCPM, FDR]]}
NewGeneDict = {}
for CompID, Values in GeneDict.iteritems():
    PantherID = Values[0]
    DE = Values[1:]
    NewList = []
    NewList.append(CompID)
    NewList.extend(DE)
    try:
        NewGeneDict[PantherID].append(NewList)
    except KeyError:
        NewGeneDict[PantherID] = []
        NewGeneDict[PantherID].append(NewList)

# Extract all PantherIDs from the NewGeneDict and sort the list
# so that it can be used to write ordered output
PantherList = []
for PantherID, Values in NewGeneDict.iteritems():
    PantherList.append(PantherID)
PantherList = sorted(PantherList)

# Now for writing the output
# In essende use the sorted keys dict (PantherList) to access
# the NewGeneDict in a sorted manner
with open(DEout, 'w') as DEoutfile:
    DEoutfile.write('%s,%s,%s,%s,%s\n' % ('Function', 'GeneID', 'logFC', 'logCPM', 'FDR'))
    for Panther in PantherList:
        for DEresults in NewGeneDict[Panther]:
            # in some cases count values were zero for a gene, which led edgeR to filter the
            # gene out; hard set the counts to zero and FDR to 1
            if len(DEresults) == 1:
                DEoutfile.write('%s,%s,0,0,1\n' % (Panther, ','.join(DEresults)))
            # if all data are present the DEresults list is 4 items long
            elif len(DEresults) == 4:
                DEoutfile.write('%s,%s\n' % (Panther, ','.join(DEresults)))
