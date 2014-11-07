#!/usr/bin/env python

'''
    Script to interleave two fastq files. Can be imported as a module.
    
    In addition, the number of sequences in the input file are returned.
    
    import interleave.py

    takes 3 arguments: inFile1, inFile2, outFile
'''

import sys, gzip

def interleave(fname1, fname2, fout):
    f1 = gzip.open(fname1, 'r')
    f2 = gzip.open(fname2, 'r')
    seqs = 0
    with open(fout, 'w') as outfile:
        while True:
            try:
                header1 = f1.next()
                seq1 = f1.next()
                junk1 = f1.next()
                qual1 = f1.next()
                
                header2 = f2.next()
                seq2 = f2.next()
                junk2 = f2.next()
                qual2 = f2.next()

                outfile.write('%s%s%s%s%s%s%s%s' % \
                        (header1, seq1, junk1, qual1, \
                        header2, seq2, junk2, qual2))

                seqs += 2
            except Exception:
                break
    
    f1.close()
    f2.close()
    return int(seqs)

if __name__ == '__main__':
    interleave(sys.argv[1], sys.argv[2], sys.argv[3])
