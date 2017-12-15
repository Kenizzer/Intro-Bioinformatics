#!/usr/bin/env python

import os, sys, re
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# Given info
# adaptor start = GATGACGGTGT 11 charcaters
# adaptor end = ATAACGCCCAT 11 characters

#online helpful pages
#http://biopython.org/DIST/docs/api/Bio.SeqRecord.SeqRecord-class.html
#http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec22
#http://biopython.org/DIST/docs/api/Bio.Seq.Seq-class.html#startswith

#grab arguments from the commandline
filename = sys.argv[1]
newfile = sys.argv[2]
adaptor_start = sys.argv[3]
adaptor_end = sys.argv[4]
seqlength = sys.argv[5]

seqlength = int(seqlength)
adaptor_start = str(adaptor_start)
adaptor_end = str(adaptor_end)

# print filename
# print newfile
# print adaptor_end
# print adaptor_start
# print seqlength

def main():
	#create list to store the records in
	Filtered_recs = []
	for rec in SeqIO.parse(filename,"fastq"):
		# Must take care to store and trim both quality and sequence
		# Other annotations to each record can be left as is.
		#Store the each sequence in a string
		sequence = rec.seq
		#store the corresponding quality score in a varible
		quality = rec.letter_annotations['phred_quality']
		
		#check for adaptor
		if sequence.endswith(adaptor_end):
			#trim end
			sequence = sequence[:-11]
			quality = quality[:-11]
	
		#check for the primer
		if sequence.startswith(adaptor_start):
			#trim beginning
			sequence = sequence[11:]
			quality = quality[11:]
		
		#Filter by length of seqlength (80)
		if len(sequence) >= seqlength:
			#build fastq file format again id, seq, "+", qual, destcription in list
			Filtered_rec = SeqRecord(seq=sequence, letter_annotations={'phred_quality':quality}, id=rec.id, description=rec.description)
			Filtered_recs += [Filtered_rec]
	
	count = SeqIO.write(Filtered_recs, newfile, "fastq")
	print("Saved %i reads" % count)
	sys.exit()
if __name__ == "__main__":
    main()