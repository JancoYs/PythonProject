#! /usr/bin/python
import sys
import os

def AlignmentExplorer(sexTup, alignS, filename):
  
  print
  start = input('Enter the start of segment: ')
  print
  end = input('Enter the start of segment: ')
  print "\n\n\n"
  print "Clustal segment [",start,"-",end,"] of the ",filename," alignment."
  print "\n"
  

  if (end-start)<61:
    for i in range(0,len(sexTup)):
      print sexTup[i][0], "\t", sexTup[i][1][start:end]
      print '\t', alignS[start:end] 
  raw_input('Press E to enter another section or Enter to return to menu: ')
  if str(input) == "E":
    AlignmentExplorer(sexTup, alignS, filename)
  else:
    os.system('clear')
    return 0 
  
  if (end-start)>60:
    while (end-start)>60:
      for i in range(0,len(sexTup)):
	print sexTup[i][0], "\t", sexTup[i][1][start:+60]
	print '\t', alignS[start:start+60]
	print "\n"
	start = start+60
  print sexTup[i][0], "\t", sexTup[i][1][start:end]
  print '\t', alignS[start:end]
  raw_input('Press E to enter another section or Enter to return to menu: ')
  if str(input) == "E":
    AlignmentExplorer(sexTup, alignS, filename)
  else:
    os.system('clear')
    return 0 
