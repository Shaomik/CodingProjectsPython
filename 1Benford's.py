

#  Description: Checks to see if approx. 30 percent of the population data start with a 1.

#  Name: Shaomik Sarkar 

#  Date Created: 4/25/2015

#  Date Last Modified: 4/25/2015


##################################################################################
#Part 1: Reads the lines in the file and stores population data in a list
##################################################################################
def main():
  pop_num = []
  inFile = open ("./Census_2009.txt", "r")
  count = 0
  for line in inFile:
   if (count == 0):
    count += 1
    continue
   else:
    count += 1
    line = line.strip()
    word_list = line.split()
    pop_num.append (word_list[-1])
  inFile.close()
##################################################################################
#Part 2: Form a output table
##################################################################################
  print("Digit   Count   %")
##################################################################################
#Part 3: Create a dictionary and check first digit of each population entry
#        and keep count in the dictionary
##################################################################################
  Freq = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
  for i in range(len(pop_num)):
    popstring = pop_num[i]
    Freq[popstring[0]] += 1
#############################################################################################################
#Part 4: Print statement for table and alignment for values from 1 to 9
#############################################################################################################
  for i in range(1,10):
   print (i, "     ", Freq[str(i)], (6-len(str(Freq[str(i)])))*" ", round(((Freq[str(i)]/(count-1))*100),1)) 
    
   

main()
