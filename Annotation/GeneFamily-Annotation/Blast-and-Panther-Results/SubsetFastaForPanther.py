#!/usr/bin/env python

# Retrieve plant genes from all fasta files (*.fst)
# and create a new smaller fasta file in which contaminants
# were removed

import sys, glob, screed

# Retrieve the plantIDs 
Plants = '../plantIDs'

# Read the IDs of plant seqs in Uniprot into
# a dictionary to check Blast hits against
PlantIDs = {}
with open(Plants, 'rU') as IDs:
    for line in IDs:
        PlantIDs[line.rstrip()] = ''

# The folowing routine relies on a simple key-test
CompIDs = {}
for BlastReport in glob.glob('./*out'):
    print BlastReport
    # open each Blast report and store the comp IDs that hit 
    # plant seqs in UniProt
    with open(BlastReport, 'rU') as BLASTout:
        for line in BLASTout:
            try:
                # If the Blast Hit is stored in the PlantsIDs dictionary
                # a key-lookup works and the stored gene ID (compID)
                # is stored in the CompIDs dictionary
                PlantIDs[line.split()[1]]
                PlantHits = line.split()[0]
                CompIDs[PlantHits] = ''
            except KeyError:
                continue
    # Store the original fasta file Species.fst in Fst
    Fst = '.%s.fst' % (BlastReport.split('.')[1])
    # AlgalFst will store those sequences that pass the taxonomic BLAST
    # filter
    AlgalFst = '.%s.algal.fst' % (BlastReport.split('.')[1])

    # Open the output file for writing
    with open(AlgalFst, 'w') as OutFile:
        # Enumerate over the Species.fst file
        #
        # For every sequence ID (record['name'])
        # perform a key-look-up in CompIDs dict
        # If the key-look-up works the sequence hit
        # 'green' taxon in the BLAST search and should
        # be written to the Species.algal.fst
        for n, record in enumerate(screed.open(Fst)):
            try:
                CompIDs[record['name']]
                OutFile.write('>%s\n%s\n' % (record['name'], record['sequence']))
            except KeyError:
                continue
