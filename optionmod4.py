#! /usr/bin/python
from Bio.Seq import Seq

def sequenceExplorer(seqTup):

  print "\nPossible Sequences are: ",
  for i in range (0, len(seqTup)):
    print seqTup[i][0],
  seq=raw_input("\n\nPlease enter a sequence Id: ")
  found = False
  while found == False:
    for i in range (0, len(seqTup)):
      if str(seq) == seqTup[i][0]:
	found = True
	seqNum = i;
    if found == False:
      print'That sequence Id could not be found. Please try again'
  
  # again shortening sequences (should have made a seperate function!
  sequence = ""
  ACGT = [0,0,0,0]
  for j in range (0, len(seqTup[seqNum][1])):
    base=seqTup[seqNum][1][j]
    if base != "-":
      sequence = sequence + base
      

  print "Length = ", len(sequence), "\n"
  print "Frequency per base:"
  print "\t\t [A]: ", sequence.count('A')
  print "\t\t [C]: ", sequence.count('C')
  print "\t\t [G]: ", sequence.count('G')
  print "\t\t [T]: ", sequence.count('T')
  
  print "Sequence: "
  if len(sequence)<60:
    print sequence
  else:
    start = 0
    while (len(sequence) - start)>60:
      print sequence[start:start+60]
      start = start+60	
    print sequence[start:len(sequence)]

  I = raw_input('Press [enter] to display the menu again or I to select another sequence:')
  if str(I) == "I":
    return 1
  else:    
    return 0
