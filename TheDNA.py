

#  Description: Checks for the longest DNA sequence common to two strings of DNA.

#  Name: Shaomik Sarkar


#  Date Created: 3/28/2015

#  Date Last Modified:3/28/2015

def main():
##########################################################################
#Part 1: Reading no.of DNA pairs and the pair themselves. Ordering the 
#pairs by size as the longest substring has to be in smaller sequence.
##########################################################################
  # open the file for reading
  in_file = open ("dna.txt", "r")

  # read file for total number of pairs
  pairs = in_file.readline()
  pairs = pairs.strip()
  pairs = int (pairs)
  LongestDNA = "A"
  SeqList = []
  PairNum=0
  # read pairs of dna strands
  for i in range (pairs):
    del SeqList[:]
    PairNum = i + 1
    StringA = in_file.readline()
    StringB = in_file.readline()

    StringA = StringA.strip()
    StringB = StringB.strip()

    # make the strings uppercase
    StringA = StringA.upper()
    StringB = StringB.upper()

    # order the strands by size
    if (len(StringA) > len(StringB)):
      dnaA = StringA
      dnaB = StringB
    else:
      dnaA = StringB
      dnaB = StringA
##############################################################################
#Part 2: Loops to control the size of substring to check for all possible ones
#Add the longest sequences found to the SeqList list.
##############################################################################
    # get all substrings of dnaB
    Window = len (dnaB)
    while (Window > 1):
      Start = 0
      while ((Start + Window) <= len (dnaB)):
        DNA_Sub = dnaB[Start: Start + Window]
  
	# check if it exists in dna1
        if DNA_Sub in dnaA:
         if len(LongestDNA) == len(DNA_Sub):
           LongestDNA = DNA_Sub
           SeqList.append(DNA_Sub)
         elif len(LongestDNA) < len(DNA_Sub):
           del SeqList[:]
           LongestDNA = DNA_Sub
           SeqList.append(DNA_Sub)
        Start = Start + 1
      # make the window smaller
      Window = Window - 1
################################################################################
#Part3: Print every item in the list of matching sequences individually.
# If list is empty then there was no matching sequence.
################################################################################
    if SeqList == []:
     print ("Pair",PairNum,":","No Common Sequence Found")
    else:
     print ("Pair",PairNum,":", SeqList[0])
     for k in range (len(SeqList)-1):
       print ("        ",SeqList[k+1])
  # close file
  in_file.close()

################################################################################
main()
################################################################################
#                                  END                                         #
################################################################################
