#!/usr/bin/env python

'''
'''

import sys
from Bio import SeqIO, Seq
from glob import glob

DEresults = {
        'DC10': glob('./DC*/edgeR_*/*DC10.counts.matrix.condA_vs_condB.edgeR.DE_results'),
        'DC20':glob('./DC*/edgeR_*/*DC20.counts.matrix.condA_vs_condB.edgeR.DE_results'),
        'DC30': glob('./DC*/edgeR_*/*DC30.counts.matrix.condA_vs_condB.edgeR.DE_results'),
        'DC40': glob('./DC*/edgeR_*/*DC40.counts.matrix.condA_vs_condB.edgeR.DE_results'),
        'DC50': glob('./DC*/edgeR_*/*DC50.counts.matrix.condA_vs_condB.edgeR.DE_results'),
        'DC60': glob('./DC*/edgeR_*/*DC60.counts.matrix.condA_vs_condB.edgeR.DE_results'),
        'DC70': glob('./DC*/edgeR_*/*DC70.counts.matrix.condA_vs_condB.edgeR.DE_results'),
        'DC80': glob('./DC*/edgeR_*/*DC80.counts.matrix.condA_vs_condB.edgeR.DE_results')
            }

Assemblies = {
        'DC10': '/home/bastodian/DimensionsData/T6/Assemblies/DC10/Trinity.fasta',
        'DC20': '/home/bastodian/DimensionsData/T6/Assemblies/DC20/Trinity.fasta',
        'DC30': '/home/bastodian/DimensionsData/T6/Assemblies/DC30/Trinity.fasta',
        'DC40': '/home/bastodian/DimensionsData/T6/Assemblies/DC40/Trinity.fasta',
        'DC50': '/home/bastodian/DimensionsData/T6/Assemblies/DC50/Trinity.fasta',
        'DC60': '/home/bastodian/DimensionsData/T6/Assemblies/DC60/Trinity.fasta',
        'DC70': '/home/bastodian/DimensionsData/T6/Assemblies/DC70/Trinity.fasta',
        'DC80': '/home/bastodian/DimensionsData/T6/Assemblies/DC80/Trinity.fasta'
            }


for Species, ResultsFiles in DEresults.iteritems():
    CompIDs = []
    for File in ResultsFiles:
        with open(File, 'r') as InFile:
            for Line in InFile:
                if 'logFC' not in Line:
                    logFC = float(Line.split()[1])
                    FDR = float(Line.split()[-1])
                    if abs(logFC) >= 2 and FDR <= 0.01:
                        CompIDs.append(Line.split()[0])
    CompIDs = frozenset(CompIDs)
    print Species, len(CompIDs)

    FastaFile = './Assemblies/%s.DE.fst' % Species
    print FastaFile
    with open(Assemblies[Species], 'rU') as Assembly:
        with open(FastaFile, 'w') as OutFile:
            for record in SeqIO.parse(Assembly, "fasta"):
                GeneName = '%s_%s' % (record.name.split('_')[0], record.name.split('_')[1])
                if GeneName in CompIDs:
                    OutFile.write('>%s\n%s\n' % (record.name, record.seq))
