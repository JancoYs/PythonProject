#! /usr/bin/python
import sys
import os

def AlignmentAnalyser(seqTup, alignBin, filename, alphabet):

  print '\n'
  print 'Filename \t\t', filename,
  print '\n'
  print 'Sequences: \t\t',
  for i in range(0,(len(seqTup)-1)):
    print seqTup[i][0],
  print " and", seqTup[-1][0]
  print "\n"
  print "Length: \t\t", (len(seqTup[0][0])+1)
  print "\n"
  
  #Length calculations: put in seperate module?
  lengths = []
  for i in range(0, len(seqTup)):
    lengths = lengths + [float(0)]
    for j in range(0, len(seqTup[0][1])):
      if seqTup[i][1][j] != "-":
	lengths[i] = lengths[i] + 1
    print seqTup[i][0], "has a length of", lengths[i]
  print "\n"
  avLength = sum(lengths)/len(lengths)
  print "Average length = \t", avLength 
  print "\n"
  percentage = sum(alignBin)
  print "Percentage of Matches %d2"
  print
  print "Number of X matches:"
  print
  noXmatches = []
  if alphabet == "N":
    noXmatches = nucMatches(seqTup,alignBin)
  if alphabet == "P":
    noXmatches = protMatches(seqTup,alignBin)

  for i in range(len(seqTup),1,-1):
    counter = 0
    for j in range(0,len(alignBin)):
      if int(noXmatches[j]) == int(i):
	counter = counter + 1
    print "\t [", i,"] = ",counter
  raw_input('Press Enter to return to menu')
  os.system('clear')
  return 0
