#!/usr/bin/env python

'''
'''

import sys, os, glob, csv

# Where should the output be written to?
OutPutFile = sys.argv[1]

# Which count type should be written out? Options:
# TPM or ExpectedCount
Option = sys.argv[2]

# Create a dictionary of count files to be processed and sort them.
# Assumes that all count files are stored in GeneFamilyCounts
Files = []
for CountFile in glob.glob(os.path.join('./GeneFamilyLevelDE/', 'DC*', 'edgeR*', '*_results')):
    Files.append(CountFile)
Files=sorted(Files)

## Create a dictionary of dictionaries that stores PantherIDs and counts
## for every file to be processed:
##
## FileDict{File1:{PTHR_1: Count; PTHR_2: Count}; File2:{PTHR1: Count; PTHR2: Count}}
FileDict = {}
## Crawl over the count files in GeneFamilyCounts and store PTHR family counts in a 
## dictionary PTHRdict{PTHR_1: Count; PTHR_2: Count}
for File in Files:
    with open(File, 'r') as Counts:
        PTHRdict = {}
        SampleID = File.rstrip().lstrip('./').split('/')[1]
        for Line in Counts:
            if 'PTHR' in Line:
                PTHR = Line.rstrip('\n').split()[0]
                # FDR is in column 5 of the input
                FDR = Line.rstrip('\n').split()[4]
                # FoldChange is in column 2 of the input
                LogFC = Line.rstrip('\n').split()[1]
                # What output was specified? FC or FDR?
                if Option == 'FC':
                    PTHRdict[PTHR] = FC
                elif Option == 'FDR':
                    PTHRdict[PTHR] = FDR
        # Store the PantherID dictionary for this file in a global dictionary
        FileDict[File] = PTHRdict

## Create a list of sorted Filenames so that the header of the output is sorted
Filenames = sorted(FileDict.keys())
# Create a list of PTHR IDs for later use as RowNames
PTHRids = FileDict[Filenames[0]].keys()

## Create a list of dictionaries to be written as rows
## each dict/row contains Label: PTHRid, File1: Count1, File2: Count2...
Rows = []
for PTHR in PTHRids:
    TmpPTHR = {}
    TmpPTHR['Label'] = PTHR
    for File in Filenames:
        SampleID = File.rstrip().lstrip('./').split('/')[2].split('_')[1]
        print SampleID
        TmpPTHR[SampleID] = FileDict[File][PTHR]
    Rows.append(TmpPTHR)

# Create columnNames that are sorted modified filenames
ColumnNames = ['Label']
ColumnNames.extend(sorted(Rows[1].keys())[:-1])

# Here the actual output is written using the CSV writer to write the dictionaries to file
with open(OutPutFile, 'wb') as Output:
    # csvwriter is initiated as a dictionary writer
    csvwriter = csv.DictWriter(Output, delimiter=',', fieldnames=ColumnNames)
    # As opened csvwriter wants dictionaries but ColumnNames is a list;
    # Thus, we trick it by creating a dictionary from the ColumnNames list in the form
    # Label: Label, File1: File1, File2: File2
    csvwriter.writerow(dict((fn,fn) for fn in ColumnNames))
    # now that the header was written we write the gene family counts on every row
    for Row in Rows:
        csvwriter.writerow(Row)
