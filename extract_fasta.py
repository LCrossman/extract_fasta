#!/usr/bin/python

from Bio import SeqIO
import sys

handle = open(sys.argv[1], 'r')

records = list(SeqIO.parse(handle, "fasta"))

infile = open(sys.argv[2], 'r')

keep = [line.rstrip() for line in infile]

seqs = []

for rec in records:
    if rec.id in keep:
        seqs.append(rec)


outfile = open("result.fasta", 'w')

SeqIO.write(seqs, outfile, "fasta")
