#!/usr/bin/env python

'''
    Parse all count files and summarize them into a csv
'''

import sys, os, glob, csv

OutPutFile = sys.argv[1]

# Which count type should be written out? Options:
# TPM
# ExpectedCount
CountType = sys.argv[2]

# Create a dictionary of count files to be processed and sort them
Files = []
for CountFile in glob.glob(os.path.join('./GeneFamilyCounts/', 'D[CN]*')):
    if '.log' not in CountFile:
        Files.append(CountFile)
Files=sorted(Files)

# I need a dictionary for file and PTHR ID counts
# The latter will be stored as a dictionary in a dictionary
FileDict = {}
SampleID = []
# Crawl over the Count Files and store counts in Dict
for File in Files:
    with open(File, 'r') as Counts:
        PTHRdict = {}
        SampleID.append(File.rstrip().lstrip('./'))
        for Line in Counts:
            if 'PTHR' in Line:
                PTHR = Line.rstrip('\n').split()[0]
                # Expected counts are in column 3 of the input
                ExpectedCount = Line.rstrip('\n').split()[3]
                # TPM value are in column 5 of the input
                TPM = Line.rstrip('\n').split()[4]
                if CountType == 'TPM':
                    PTHRdict[PTHR] = TPM
                elif CountType == 'ExpectedCount':
                    PTHRdict[PTHR] = ExpectedCount
        FileDict[File] = PTHRdict

# Create a list of sorted Filenames for use
Filenames = sorted(FileDict.keys())
# Create a list of PTHR IDs for later use as RowNames
PTHRids = FileDict[Filenames[0]].keys()

# Create a list of dictionaries to be written as rows
# later; each dict/row contains Label: PTHRid, File1: Count1,
# File2: Count2...
Rows = []
for PTHR in PTHRids:
    TmpPTHR = {}
    TmpPTHR['Label'] = PTHR
    for File in Filenames:
        SampleID = File.rstrip('.pruned').lstrip('./')
        TmpPTHR[SampleID] = FileDict[File][PTHR]
    Rows.append(TmpPTHR)

# Create columnNames that are sorted modded filenames
ColumnNames = ['Label']
ColumnNames.extend(sorted(Rows[1].keys())[:-1])

# Here I write the actual outpt
with open(OutPutFile, 'wb') as Output:
    csvwriter = csv.DictWriter(Output, delimiter=',', fieldnames=ColumnNames)
    # As opened csvwriter wants dicts but ColumnNames is a list;
    # Thus, we trick it by creating a dict Label: Label, File1: File1, File2: File2
    csvwriter.writerow(dict((fn,fn) for fn in ColumnNames))
    for Row in Rows:
        csvwriter.writerow(Row)
