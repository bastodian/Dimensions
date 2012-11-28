#!/usr/bin/env python

import sys
import screed

filein = sys.argv[1]
fileout = sys.argv[2]

fw = open(fileout, 'w')

for n, record in enumerate(screed.open(filein)):
    if 'N' in record['annotations']:
        name = record['name'] + ' ' + record['annotations']
        sequence = record['sequence']
        accuracy = record['accuracy']
        fw.write('@%s\n%s\n+\n%s\n' % (name, sequence, accuracy))
    else:
        continue

fw.close()
