#!/usr/bin/env python

import csv, sys
 
def parse_input_csv(in_handle):
    reader = csv.reader(in_handle)
    print reader
    reader.next() # header
    all_genes = dict()
    for (gene_name, _, _, pval) in reader:
        all_genes[gene_name] = float(pval)
    return all_genes

parse_input_csv(sys.argv[1])
