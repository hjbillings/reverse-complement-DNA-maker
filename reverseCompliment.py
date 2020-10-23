#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 21:05:19 2020

@author: hanabillings
"""

sequence = "AGACGTACGTAAACCCGGG"

def complement(sequence):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} # replaces each NU with its complement
    NU = list(sequence)                                   # converts string to list so we can iterate through it
    NU = [complement[i] for i in NU]                      # replaces each base with its complement
    return "".join(NU)                                    # joins each separate string with no separator
    def reverseComplement(seq):
        sequenceComplement = sequence[::-1]               #reverses the complementary sequence
        return sequenceComplement

print("sequence:", sequence)
print("reverse complement:", complement(sequence))
    
            

