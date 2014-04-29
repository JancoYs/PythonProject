#! /usr/bin/python

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import re

def GlycoSig(seqTup):
  
  sigFound = False
  Glycocylate= re.compile("n[^p][st]")
  
  for i in range(0,len(seqTup)):
    sequence = ""
    for j in range (0, len(seqTup[i][1])):
      base=seqTup[i][1][j]
      if base != "-":
	sequence = sequence + base
	
    DNA2Translate = Seq(sequence, IUPAC.unambiguous_dna)
    a = DNA2Translate.translate()
    a = a.lower()
    b = Glycocylate.findall(str(a))
    if b != []:
      sigFound = True
      print seqTup[i][0], "has the signature"
      for item in b:
	spot = a.find(item)
	a=a[0:spot]+a[spot:spot+3].upper()+a[spot+3:len(a)]
      print "Sequence: ", str(a)
    else:	
      print seqTup[i][0], "does not have the signature."
	  
     #spot = a.find(sig)
#	print spot
#      print Translations[0], " has signature: ", a
  if sigFound == False:
    print "No signatures found"
  
  raw_input('Press Enter to Return to the menu")
  return 0
  
