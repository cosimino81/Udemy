# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 16:35:57 2018

@author: Cosimo
"""
# read the file

dna_infile = 'C:\Users\Cosimo\Desktop\Python_Research\dna_case_study\dna.txt'
prot_infile = 'C:\Users\Cosimo\Desktop\Python_Research\dna_case_study\protein.txt'

def read_sequence(inputfile):
    """Read and return the sequence with the special character removed"""
    with open(inputfile, 'r') as f:
        seq = f.read()
        seq = seq.replace("\n", "").replace("\r","")
        return seq
    
    
read_sequence(dna_infile)


def translate(sequ):
    """This function takes a dna sequence in input and return"
       the corrispective aa codificated"""
    table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',}
    
    # check that the sequence is divisible by 3
    protein =""
    
    if len(sequ) % 3 == 0:
        for i in range(0, len(sequ), 3):
            codon = sequ[i : i+3]
            protein += table[codon]
  
    return protein


dna = read_sequence(dna_infile) 
prot = read_sequence(prot_infile)
# real sequence on ncbi is 21:938
# the sequences on ncbi start from 1
translate(dna[20:938])

# compare the prot sequence with the dna sequence
# in this case is false because there is the stop codon 
prot == translate(dna[20:938])


# In thi case is true (-3 nucleotide)
prot == translate(dna[20:935])



