#!/usr/bin/env python

import os, sys, re


#test seq for practice
#seq = "GATTaca"


def reverse(s):
    """Return the sequence string in reverse order."""

    # make a list of letters from string

    seqList = list(s)
    #print(seqList)

    # reverse the list

    revseqList = seqList[::-1]
    #print(revseqList)

    # join the letters of the list into string and return

    revstring = ""
    for i in revseqList:
        revstring += i
    #print(revstring)
    return revstring

#Test string
#reverse("AAAAAGGGGG")


def complement(s):

    """Return the complementary sequence string."""

    # dictionary setup for complement
    dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # make a list of letters from string
    #print(s)
    slist = list(s)

    # for loop of the letters and call the base_complementary dictionary
    templist = []
    for i in slist:
        templist.append(dict[i])

    # join the letters of the list into string and return
    compstring = ""
    for i in templist:
        compstring += i
    #print(compstring)
    return compstring

#test string
#complement("AATTGGCC")

def main():

    # get input sequence

    dna_seq = raw_input('Type your DNA sequence : ')

    # check DNA letter (only ACGTacgt)

    if re.match("^[ATCGatcg]*$", dna_seq):
    # change it to upper case
        up_dna = dna_seq.upper()

    #print(up_dna)
    # call reverse function

    rev_up_dna_seq = reverse(up_dna)
    #print(rev_up_dna_seq)

    # call complement function

    comp_rev_dna = complement(rev_up_dna_seq)

    # print output

    print "Reverse complement DNA :", comp_rev_dna

    sys.exit()

if __name__ == '__main__':
    main()