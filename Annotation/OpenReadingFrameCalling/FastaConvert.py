#!/usr/bin/env python

import screed, sys

#outfile = sys.argv[1]
infile = sys.argv[1]
tag = sys.argv[2]

#with open(outfile, 'w') as out:
for n, record in enumerate(screed.open(infile)):
    sys.stdout.write('>%s|%s\n%s\n' % (tag, record['description'].split()[7], record['sequence']))
