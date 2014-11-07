#!/usr/bin/env python

import os, sys, glob

'''
    RawDataDir is the path to the folders containing the raw read files.
    As of now this needs to be modified by replacing the path.
'''

AssemblyDir = ('/home/bastodian/DimensionsData/T6/Assemblies/')
#AssemblyDir = sys.argv[1]
TrimmedDataDir = ('/home/bastodian/DimensionsData/T6/TrimmedData/')
#TrimmedDataDir = sys.argv[2]
logfile = sys.argv[1]

'''
    Create a list of files to process
'''

#Reference
Refs = [file for file in glob.glob('%s%s' % (AssemblyDir, 'D[CN][1-8]0*/Trinity.fasta'))]
Refs.sort()
#sys.stdout.write('Reference Transcriptomes:\n%s\n\n' % '\n'.join(Refs))

#Competition Treatments
Comp = [file for file in glob.glob('%s%s' % (TrimmedDataDir, 'D[CN]?[1-8]*/*trimmed*'))]
Comp.sort()
#sys.stdout.write('Treatments:\n%s\n\n' % '\n'.join(Comp))

import subprocess

#Create a dictionary of reference assemblies
AssemblyDict = {}
for Assembly in Refs:
    AssemblyDict[Assembly.split('/')[-2]] = Assembly

#Map the monocultures against the reference assemblies    
with open(logfile, 'w') as log:
    for Culture in range(len(Comp)):
        if Culture % 2 == 0:
            Left = Comp[Culture]
            Right = Comp[Culture + 1]
            Ref1 = AssemblyDict['DC%s0' % (Comp[Culture].split('/')[-1][2])]
            Ref2 = AssemblyDict['DC%s0' % (Comp[Culture].split('/')[-1][3])]
            OutDir1 = '%s/RSEM_out_%s' % ('/'.join(Comp[Culture].split('/')[:-1]), Comp[Culture].split('/')[-1][2])
            OutDir2 = '%s/RSEM_out_%s' % ('/'.join(Comp[Culture].split('/')[:-1]), Comp[Culture].split('/')[-1][3])
            if os.path.isdir(OutDir1) is False:
                os.makedirs(OutDir1)
                AlignReads1  = ('cd %s && nice -n 8 /usr/local/src/trinityrnaseq_r2013-02-25/util/RSEM_util/run_RSEM_align_n_estimate.pl \
                                --left %s \
                                --right %s \
                                --seqType fq \
                                --transcripts %s \
                                --thread_count 24' \
                                % (OutDir1, Left, Right, Ref1))
                log.write('Mapping %s and %s against %s...\n' % (Left.split('/')[-1], Right.split('/')[-1], ('/').join(Ref1.split('/')[-2:])))
                os.system(AlignReads1)
            if os.path.isdir(OutDir2) is False:
                os.makedirs(OutDir2)
                AlignReads2  = ('cd %s && nice -n 8 /usr/local/src/trinityrnaseq_r2013-02-25/util/RSEM_util/run_RSEM_align_n_estimate.pl \
                                --left %s \
                                --right %s \
                                --seqType fq \
                                --transcripts %s \
                                --thread_count 24' \
                                % (OutDir2, Left, Right, Ref2))
                log.write('Mapping %s and %s against %s...\n' % (Left.split('/')[-1], Right.split('/')[-1], ('/').join(Ref2.split('/')[-2:])))
                os.system(AlignReads2)
            log.write('Done!\nMoving on...\n\n')
        else:
            continue
