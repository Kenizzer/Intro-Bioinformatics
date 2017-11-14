#!/usr/bin/env python

import os, sys, re
from Bio.Seq import Seq
from Bio import SeqIO
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", help="Please enter your fasta file name", action="store", type="string", dest="filename")
parser.add_option("-x", help="This will use my own rev complement program; default is biopython", action="store_true", dest="prog")
parser.add_option("-o", help="define the output file name ", action="store", type="string", dest="outname")
(options, args) = parser.parse_args()

def name():
	global file
	if options.outname is None:
		#Generating required chunks of the file output name
		output_name = options.filename[:options.filename.rfind(".")]
		output_suffix = os.path.splitext(options.filename)[1]
		newname = output_name + "_reverse" + output_suffix
		file = open(newname,"w")
	else:
		#Use the user defined name
		file = open(options.outname, "w")
def parsefasta():
	for seq_record in SeqIO.parse(options.filename, "fasta"):
		#revcomplementing the seqeunces
		rev_dna_seq = complement(reverse(seq_record.seq))
		#writing sequence descript then rev seq to file
		file.write( ">" + str(seq_record.description) + " REVERSED" + "\n")
		file.write(str(rev_dna_seq) + "\n")
def reverse(s):
	# make a list of letters from string
	seqList = list(s)
	# reverse the list
	seqList.reverse()
	# join the letters of the list into string and return
	return ''.join(seqList)
def complement(s):
	"""Return the complementary sequence string."""
	# dictionary setup for complement
	dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
	# make a list of letters from string
	slist = list(s)
	# for loop of the letters and call the base_complementary dictionary
	templist = [dict[base] for base in slist]
	# join the letters of the list into string and return
	return ''.join(templist)

# this will control the flow of the program inputting -x in the command line selects 
# own rev complement program.
def main():
	if options.prog == True:
		# get input sequence
		if options.filename is None:
			dna_seq = raw_input('Type your DNA sequence : ')
			# check DNA letter (only ACGTacgt)
			if re.match("^[ATCGatcg]*$", dna_seq):
			# change it to upper case
				up_dna = dna_seq.upper()
			else:
				print("** ERROR: This is not a DNA sequence")
				return None
			# call reverse function
			rev_up_dna_seq = reverse(up_dna)
			# call complement function
			comp_rev_dna = complement(rev_up_dna_seq)
			# print output
			print "Reverse complement DNA, my program:", comp_rev_dna
			sys.exit()
		elif os.path.splitext(options.filename)[1] == ".fasta":
			name()
			#parsing the fasta file, one set of records at a time
			parsefasta()
		else:
			file1 = open(options.filename, "r")
			dna_seq = str(file1.read())
			dna_seq = [x.strip() for x in dna_seq]
			rev_dna_seq = complement(reverse(dna_seq))
			rev_dna_seq = re.sub("(.{64})", "\\1\n", rev_dna_seq, 0, re.DOTALL)
			name()
			file.write(rev_dna_seq)
			file1.close()
		file.close()
		sys.exit()
	else:
		##Biopython reverse complement 
			# get input sequence
		if options.filename is None:
			dna_seq = raw_input('Type your DNA sequence : ')
			# Seq object call
			dna_seq = Seq(dna_seq)
			# call reverse_complement function in Bio.Seq
			rev_dna_seq = dna_seq.reverse_complement()
			# print output
			print "Reverse complement DNA, biopython:", rev_dna_seq
			sys.exit()
		elif os.path.splitext(options.filename)[1] == ".fasta":
			name()
			#parsing the fasta file, one set of records at a time
			parsefasta()
		else:
			file1 = open(options.filename, "r")
			dna_seq = Seq(str(file1.read()))
			rev_dna_seq = str(dna_seq.reverse_complement())
			name()
			file.write(rev_dna_seq)
			file1.close()
		file.close()
		sys.exit()
if __name__ == '__main__':
	main()	