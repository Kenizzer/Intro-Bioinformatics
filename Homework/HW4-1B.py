#!/usr/bin/env python

import os, sys, re
from Bio.Seq import Seq

def main():

	# get input sequence
	dna_seq = raw_input('Type your DNA sequence : ')

	# Seq object call
	dna_seq = Seq(dna_seq)
	# call reverse_complement function in Bio.Seq
	rev_dna_seq = dna_seq.reverse_complement()

	# print output
	print "Reverse complement DNA :", rev_dna_seq

# exit the program
	sys.exit()

if __name__ == '__main__':
	main()
