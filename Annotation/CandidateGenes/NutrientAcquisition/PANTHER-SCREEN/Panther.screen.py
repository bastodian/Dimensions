#!/usr/bin/env python

import sys

PANTHERfile = sys.argv[1]


PANTHER = ['PTHR18952', \
        'PTHR11986:SF5', \
        'PTHR31632:SF1', \
        'PTHR21649:SF0', \
        'PTHR21649', \
        'PTHR10283:SF37', \
        'PTHR19370:SF5', \
        'PTHR24003:SF321', \
        'PTHR32439:SF0', \
        'PTHR30520:SF0', \
        'PTHR30224:SF0', \
        'PTHR30115:SF1', \
        'PTHR11101:SF7']

with open(PANTHERfile, 'rU') as infile:
    for line in infile:
        #if line.split[1] in PANTHER:
        print line.split()[1]
