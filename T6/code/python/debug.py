#!/us/bin/env python

from PhredTools import EndTrim

a = '012345678901'
#b = """!"#$!!!$%&'$"""
b = """$$$$!$!$!!!$"""
c = 3

trim = EndTrim(a,b,c)
#trim.FivePrime(5)
#trim.IntraTrim(2)
#trim.MinLength(2)
trim.ThreePrime(5)

if None in trim.Retrieve():
    print trim.Retrieve()
else:
    print '\n'.join(trim.Retrieve())
