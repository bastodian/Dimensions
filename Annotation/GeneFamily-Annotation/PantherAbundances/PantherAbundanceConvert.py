#!/usr/bin/env python

'''
    Links Trinity gene IDs to gene family (PANTHER) IDs summing all values
    for genes that fall within the same gene family.

    This script links Panther IDs to gene IDs using the relationships
    described in the files linking PANTHER gene family IDs to gene IDs
    (../*algal.panther). Only family IDs (PTHRXXX) are considered but not subfamilies 
    (PTHRXXX:SFXXX). The script uses the gene id (compX_cX) rather than 
    transcript ID (compX_cX_seqX) to retrieve gene-level counts from RSEM
    mapping files stored in ../RSEM. FPKM counts of the same gene family (PTHR)
    ID are summed. If a gene cannot be placed into a single gene family (ie, annotations
    confict between different contigs/transcripts) belonging to the same gene the
    gene is omitted from consideration.
'''

import sys, os, glob, itertools

# Gene ID to PTHR ID maps are stored in the following files
GeneIDs = {
        '1': '../FastaFiles-BlastResults/Chl.algal.panther',
        '2': '../FastaFiles-BlastResults/Clo.algal.panther',
        '3': '../FastaFiles-BlastResults/Cos.algal.panther',
        '4': '../FastaFiles-BlastResults/Pan.algal.panther',
        '5': '../FastaFiles-BlastResults/Sce.algal.panther',
        '6': '../FastaFiles-BlastResults/Sel.algal.panther',
        '7': '../FastaFiles-BlastResults/Sta.algal.panther',
        '8': '../FastaFiles-BlastResults/Tet.algal.panther'
        }

# Counts are stored in the following directory
RSEMcounts = '../RSEM'

# Use glob to iterate through all RSEM count files
for RSEMfile in glob.glob(os.path.join(RSEMcounts, '*')):
    # ID of the experimental bottle to be used as filename
    BottleID = '_'.join(['_'.join(RSEMfile.split('/')[2].split('.')[0:2]), str(RSEMfile.split('/')[2].split('.')[-1])])
    # Logfile will be BottleID.log
    LogFile = ('./GeneFamilyCounts/logs/%s.log' % (BottleID))
    sys.stdout.write('Processing %s\n' % (BottleID))
    with open(LogFile, 'w') as LOG:
        LOG.write('RSEM file is %s\n' % (RSEMfile))
        # What is the reference to retreieve gene ID PANTHER mapping?
        Reference = GeneIDs[RSEMfile.split('.')[-1]]
        LOG.write('Reference to retrieve gene ID-PTHR mapping is %s\n' % (Reference))
        LOG.write('The ID of the experimental bottle is %s\n' % (BottleID))

        # Read Gene Panther annotations contained in *algal.panther
        # create a dictionary of gene-Panther mapping
        GeneDict = {}
        with open(Reference, 'rU') as GeneFile:
            for Line in GeneFile:
                CompID = '_'.join(Line.split()[0].split('|')[1].split('_')[0:2])
                PantherID = Line.split()[1].split(':')[0]
                LOG.write('Component ID: %s <--> PantherID: %s\n' % (CompID, PantherID))
                # Populate the dictionary that establishes the gene (CompID) to PANTHER 
                # relationships
                try:
                    # Without try the if statement will throw a KeyError since
                    # the GeneDict[KEY] may not exist; if the combination exists
                    # creates a list entry for the geneID PantherID combination
                    if PantherID not in GeneDict[CompID]:
                        GeneDict[CompID].append(PantherID)
                except KeyError:
                    GeneDict[CompID] = []
                    GeneDict[CompID].append(PantherID)

        # Add length estimates and count values to the GeneDict that contains the link
        # between gene ID (CompID) and gene family ID (PantherID). All values added as
        # a list, so that the Dictionary has the following form:
        # GeneDict{CompID1: PantherID, [Length, EffectiveLength, ExpectedCount, TPM, FPKM]}
        with open(RSEMfile, 'rU') as CountData:
            for Line in CountData:
                if 'FPKM' not in Line:
                    CompID = Line.split()[0]
                    Length = float(Line.split()[2])
                    EffectiveLength = float(Line.split()[3])
                    ExpectedCount = float(Line.split()[4])
                    TPM = float(Line.split()[5])
                    FPKM = float(Line.split()[6])
                    try:
                        GeneDict[CompID].append([Length, EffectiveLength, ExpectedCount, TPM, FPKM])
                    except KeyError:
                        continue
                
        # Transforms the dictionary of form
        # GeneDict{CompID1: PantherID, [Length, EffectiveLength, ExpectedCount, TPM, FPKM]}
        # into
        # PantherDict{PantherID1: [Length, EffectiveLength, ExpectedCount, TPM, FPKM]}
        # 
        # Genes (CompIDs) belonging to the same gene family (PantherID) in GeneDict are summed
        # using itertools' map function to sum the lengths and counts lists
        PantherDict = {}
        for CompID, j in GeneDict.iteritems():
            # if j > 2 the CompID was assigned to multiple PantherIDs; these are ignored since
            # they cannot be placed with certainty into a single gene family
            if len(j) == 2:
                # If the PantherID (j[0]) already exists in the PantherDict sum the lengths and counts
                # already in PantherDict[j[0]] with the ones stored in j[1]
                try:
                    CombinedLines = map(sum, itertools.izip(PantherDict[j[0]], j[1]))
                    LOG.write('%s, %s: %s + %s = %s\n' % (j[0], CompID, PantherDict[j[0]], j[1], CombinedLines))
                    PantherDict[j[0]] = CombinedLines
                # If the PantherID is not in the dictionary yet create the key and add the lengths and counts
                # list j[1] to the PantherDict[PantherID]
                except KeyError:
                    LOG.write('Key: %s is empty; value %s: %s will be added... \n' % (j[0], CompID, j[1]))
                    PantherDict[j[0]] = j[1]
            else:
                continue
        
        # This python script was run once without the following with loop that generates the PantherSet. Without this routine the script
        # generates 187 mapping files with varying numbers of gene families. Since I am only interested in those gene families 
        # that are shared by all 187 mapping files I ran the following bash command to generate a constraint file from this initial
        # set of files - cludgy but works. The problem: it is unknown which gene family IDs make it through until the files are written.
        #
        # grep PTHR D* | awk '{print $1}' | awk -F ':' '{ print $2}' | sort | uniq -c | sort | grep '187 ' | awk '{ print $2}' > SharedPantherIDs
        #
        # I use the SharedPantherIDs file to create a set of PTHR IDs to keep while the rest is ignored
        PantherSet = []
        with open('SharedPantherIDs', 'r') as Shared:
            for PTHR in Shared:
                PantherSet.append(PTHR.rstrip())
        PantherSet = set(PantherSet)

        # Now write the actual output
        Outfile = ('./GeneFamilyCounts/%s' % (BottleID))
        with open(Outfile, 'w') as Out:
            LOG.write('Writing %s...\n\n' % (Outfile))
            # First he header
            Out.write('%s\n' % '\t'.join([x for x in ('GeneFamily', 'length', 'effective_length', 'expected_count', 'TPM', 'FPKM')]))
            # Now iterate through the PantherDictioary and write every entry on a new line to the output
            for PantherID, Line in PantherDict.iteritems():
                if PantherID in PantherSet:
                    Out.write('%s\t%s\n' % (PantherID, '\t'.join([str(x) for x in Line])))
                else:
                    continue
