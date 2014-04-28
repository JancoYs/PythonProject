#! /usr/bin/python
import re

def checknLoad(filename):
  
  try:
   MAlAFile = open(filename , "r")
  except IOError:
    print "Error, filename \"", filename, "\" not found"
    return -1
  else:
    
      #1.3 WhiteSpace of any length/combination
    WhiteSpaceN = re.compile('\\n') 
    
    # a fairly simple check that the file is a CLUSTAL file. By no means comlete.
    if (MAlAFile.readline()[:7] != "CLUSTAL"):
      print "Error, filename \"", filename, "\"is apparently not a CLUSTAL alignment file!"
      return -1
    
    linesToDelete = [0,1]				#we have zero here, becaues ultimately we want to remove the first line that says "CLUSTAL"
    Rlines = MAlAFile.readlines()
    for n in range(2,len(Rlines)):
      
      #stripping white space
      if (WhiteSpaceN.match(Rlines[n])):	
	linesToDelete = linesToDelete + [n]					   
      
      endR = len(Rlines[n]) - 1
      Rlines[n] = Rlines[n][:endR]				#Strip off trailing '\n's
    
    
    #Delete White Space and first line...
    
    linesToDelete = linesToDelete[::-1]		#Reverse it, so that we delete lines from the tailside, otherwise order would be messed up!
    
    for i in linesToDelete:				#Get rid of white space etc. 
      del Rlines[i]
    
    # find the alignment line of *'s... and hence also the number of sequences. get their names while we're at it
    seqNames = []
    sequences = []
    align = ""
    counter = 0
    

    while (Rlines[counter][:1] != ' '):
      theline = Rlines[counter].split()
      seqNames = seqNames + [theline[0]]
      sequences =sequences + [""]
      counter = counter+1
    
    noSeqs = counter+1
 

    # Now get the sequences, and the alignment line
    for j in range(0,len(Rlines)):
      modul = (j+1)%noSeqs
      if (modul != 0):
	addSeq = Rlines[j].split()
	sequences[(modul-1)] = sequences[(modul -1)] + addSeq[1]
      else:
	pos = Rlines[j-1].find(addSeq[1])
	length = len(addSeq[1])
	plusSeq = Rlines[j][pos:(pos+length)]
	align = align + str(plusSeq)

    # I Don't know why I have to do this!!! It may cause trouble in some cases...	  
    MAlAFile.seek(-1,2)
    endA = MAlAFile.read(1)
    align = align + endA
    
    
    #some CLUSTAL files use symbols other than just " " and "*". While this can be useful, for the sake of this excercise, I'd prefer to strip them
    #+ out. Also, having a "binary" representation for the alignment might come in handy...
    
    align2 =""
    for k in range(0,len(align)):
      if (align[k] == "*"):
	align2 = align2 + "1"
      else:
	align2 = align2 + "0"
    alignBin = [int(align2[i]) for i in range(0,len(align2))] 
	    
	 
    strippedfileList = [(seqNames[0],sequences[0])]
    for l in range(1,len(sequences)):
      strippedfileList = strippedfileList + [(seqNames[l],sequences[l])]
    
    strippedfileList = strippedfileList + [align] + [alignBin]
    strippedfileTuple = tuple(strippedfileList)
    
    print "The file ",filename," has been successfully loaded."
    
    MAlAFile.close()
    
    return strippedfileTuple
