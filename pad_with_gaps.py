#!/usr/bin/env python

import argparse
from Bio import SeqIO

__author__ = "Franck Lejzerowicz"
__copyright__ = "Copyright 2017, The Deep-Sea Microbiome Project"
__license__ = "GPL V3"
__version__ = "1.0"
__maintainer__ = "Franck Lejzerowicz"
__email__ = "franck.lejzerowicz@unige.ch"

def pad_with_gaps():
    parser=argparse.ArgumentParser()
    parser.add_argument('-i', nargs = 1, required = True, help = 'Input fasta file (required)')
    parser.add_argument('-o', nargs = 1, required = True, help = 'Output fasta file (required)')
    parse=parser.parse_args()
    args=vars(parse)

    filin = args['i'][0]
    filou = args['o'][0]

    print 'Padding', filin
    try:
        seqs = SeqIO.parse(filin, 'fasta')
    except:
        print "Problem with loading input in Biopython's SeqIO.parse(). Check input. Exiting..."
    seqs = list(seqs)
    maxLen = max([len(x.seq) for x in seqs])

    o=open(filou, 'w')
    for s in seqs:
        curLen = len(s.seq)
        o.write('>%s\n%s%s\n' % (str(s.id), str(s.seq), '-'*(maxLen-curLen)))
    o.close()
    print 'Output'
    print filou
    return 0

pad_with_gaps()
