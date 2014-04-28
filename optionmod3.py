#! /usr/bin/python

def AlignmentExplorer(sexTup, alignS, filename):
  
  print
  start = input('Enter the start of segment: ')
  print
  end = input('Enter the end of the segment: ')
  print "\n\n"
  print "Clustal segment [",start,"-",end,"] of the ",filename," alignment."
  print "\n"
  
  
  if (end-start)<61:
    for i in range(0,len(sexTup)):
      print sexTup[i][0], "\t", sexTup[i][1][start:end]
    print '\t', alignS[start:end] 
    E = raw_input('Press E to explore another sequence, or Enter to return to menu: ')
    if str(E)=="E":
      return 1
    else:
      return 0
  
  while (end-start)>60:
    endfornow = start+60
    for i in range(0,len(sexTup)):
      print sexTup[i][0], "\t", sexTup[i][1][start:endfornow]
    print '\t', alignS[start:endfornow]
    print "\n"
    start = start+60
  for i in range(0,len(sexTup)):  
    print sexTup[i][0], "\t", sexTup[i][1][start:end]
  print '\t', alignS[start:end]
  E = raw_input('Press E to explore another sequence, or Enter to return to menu: ')
  if str(E)=="E":
    return 1
  else:
    return 0
