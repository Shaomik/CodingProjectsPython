
#  Description:Checks if provided isbn's in file are valid and writes results in out file.

#  Name:Shaomik Sarkar

#  Date Created: 4/4/2015

#  Date Last Modified:4/4/2015

def main():
#####################################################################################
#Part1: Setting up empty Lists and variables, as well as opening input and output
#files.
#####################################################################################
 st1=[]
 s1=[]
 s2=[]
 a=0
 psum1 = 0
 psum2 = 0
 in_file = open("isbn.txt","r")
 in2_file = open("isbnOut.txt","w")
####################################################################################
#Part2: Main loop- reads lines of isbn, replaces hyphens, and changes X to 10 if it
#is the last digit.
####################################################################################
 for f in range(sum(1 for line in open('isbn.txt'))):
  st1=[]
  s1=[]
  s2=[]
  psum1=0
  psum2 =0
  isbn1 = in_file.readline()
  isbn = isbn1.strip()
  for i in range(len(isbn)):
   if isbn[i] != "-":
    st1.append (isbn[i])
  if st1[-1].upper() =="X":
    st1[-1] = "10"
###################################################################################
#Part3: Checks validity of the isbn and does partial sums to st1 forming s1 and 
#partial summing that to get s2. Writes the results in output file.
###################################################################################
  for j in range (len(st1)):
   if (st1[j]).upper() == "X" or int(st1[j]) < 0 or int(st1[j]) > 10:
     in2_file.write(isbn + " " + "invalid\n")
     break
   else:
      psum1=psum1 + int(st1[j])
      s1.append(psum1)
  if len(s1) == 10:
    for l in s1:
      psum2 = psum2 + int(l)
      s2.append(psum2)
    if s2[-1] % 11==0:
     in2_file.write(isbn + " " + "valid\n")
    else:
     in2_file.write(isbn + " " + "invalid\n")
##################################################################################
#Part4: Emptying lists. When loop is finished, closes files.
#
##################################################################################
  del s1[:]
  del s2[:]
 in_file.close()
 in2_file.close()
##################################################################################

main()  

##################################################################################
#                                   END                                          #
##################################################################################

 








 
 
