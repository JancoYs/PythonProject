#! /usr/bin/python
def print_menu(fn):
  filename = fn
  
  print """ 
    *****************************************************************************************************
    *													*
    *	MULTIPLE ALIGNMENT ANALYZER									*
    *													*
    *****************************************************************************************************
    *													*
    *		1) Open a Multiple Alignment File		(O)					*
    *													*
    *		2) Alignment Information			(A)					*
    *													*
    *		3) Alignment Explorer				(E)					*
    *													*
    *		4) Information per Sequence			(I)					*
    *													*
    *		5) Analysis of Glycosylaton Signatures 		(S)					*
    *													*
    *		6) Export to Fasta				(F)					*
    *													*
    *		7) Exit						(X)					*
    *													*
    *								File: """,filename,"""			*
    *													*
    *****************************************************************************************************

    """

  option = input('\t Select Option: ')
  option = str(option)
  return option
  
def main(filename):
  while True:
    option = print_menu(filename)
    
    if option1.match(option):
      while filename == "None":
	filename = input ('\t Please enter a valid path for a Multiple Alignment File: ')
	filename = str(filename)
      
	os.system('clear')
	#filename = "test.aln"
	theTuple = optionmod1.checknLoad(filename)
	if (theTuple == -1):
	  print 'Please try again'
	  yesEx = input("Would you like to try a new filename (Y) or Exit (X)? ")
	  yesEx=str(yesEx)
	  if yes.match(yesEx):
	    print_menu("None")
	  else:
	    return -1

	seqTup = theTuple[:len(theTuple)-2]
	alignStar = theTuple[-2]
	alignBin = theTuple[-1]
	#Check whether we are dealing with a Protein or Nucleotide sequence.. (can be done in seperate function .	
	alphabet = ""
      
	for i in range(0,len(seqTup)):
	  if NucAlpha.match(seqTup[i][1]):
	    alphabet = alphabet + "N"
	  elif ProtAlpha.match(seqTup[i][1]):
	    alphabet = alphabet + "P"
	  else:
	    os.system('clear')
	    print "The file that you have specified doesn't use a valid Nucleotide or Protein alphabet."
	    filename = "None"
	    main()
      
	numSeqs = len(seqTup)
	
	if alphabet == "N"*numSeqs:
	  print "Input file is Nucleotide Sequences"
	  alphabet = "N"
	  
	  
	elif alphabet == "P"*numSeqs:
	  print "Input file is Protein Sequences"
	  alphabet = "P"
	 
	  
	elif mixed.match(alphabet):
	  print "Input file could be protein sequences, but certain of the sequences consist only of A,C,G and T..."
	  print "This could be a valid protein sequence, or your file might contain a mixture of protein and nucleotide sequences"
	  cont = raw_input = "Continue with this file read as protein sequence (Y) or input new file (N)? "
	  if yes.match(cont):
	    print "Input file is read as Protein sequences"
	    alphabet = "P"

	  else:
	    filename = "None"
	    os.system('clear')
	    print 'Please input a new alignment filename or exit'   
	  
	  
    elif option2.match(option):
      if (filename != "None"):
	print "\t Option 2"
	optionmod2.AlignmentAnalyser(seqTup, alignBin, filename, alphabet)
      else:
	print "Please open a multiple alignment file (Option 1) first"
    
    elif option3.match(option):
      E = ""
      if (filename != "None"):
	print "\t Option 3"
	x = True
	num = 0
	while x == True:
	  num = optionmod3.AlignmentExplorer(seqTup, alignStar, filename)
	  if num == 0:
	    x = False
      else:
	print  "Please open a multiple alignment file (Option 1) first"
      
    elif option4.match(option):
      print "Option 4"
    
    elif option5.match(option):
      print "Option 5"
    
    elif option6.match(option):
      print "Option 6"
    
    elif option7.match(option):
      print "Option 7"
    
    else:
      print "other"
  
    #case options

  
if __name__ == "__main__":
  
  # 0. IMPORT
  import sys
  import os
  import re
  import optionmod1
  import optionmod2
  import optionmod3
  
  #1. DEFINE REG EXPRESSIONS!	
  #now seems like the best time to define various regular expressions! 
  os.system('clear')
  #1.1 Menu and other options
  option1 = re.compile('[1o]', re.IGNORECASE)
  option2 = re.compile('[2a]', re.IGNORECASE)
  option3 = re.compile('[3e]', re.IGNORECASE)
  option4 = re.compile('[4i]', re.IGNORECASE)
  option5 = re.compile('[5s]', re.IGNORECASE)
  option6 = re.compile('[6f]', re.IGNORECASE)
  option7 = re.compile('[7x]', re.IGNORECASE)
  yes = re.compile('[Yy]*')
  no = re.compile('[Nn]*')
  exit = re.compile('[Xx]*')
  
  #1.2 Neucleotide and Protein alphabet
  NucAlpha = re.compile('[ACGT-]*', re.IGNORECASE)
  ProtAlpha = re.compile('[acdefghiklmnpqrstvwy-]*', re.IGNORECASE)
  mixed = re.compile('[NP]*')
  
  #1.3 WhiteSpace of any length/combination
  WhiteSpaceN = re.compile('[\s]*\n') 
  WhiteSpace = re.compile('[\s]*')
  
  #No file loaded yet... (could make a command line argument to accept a file, but not particularly necessary as it's covered by the menu!
  filename = "None"
  theTuple = []
  exitFlag = False
  seqTup = []
  alignBin = []
 #now Run the main menu... 
  main(filename)
  
  
