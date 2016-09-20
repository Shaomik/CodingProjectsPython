

#  Description: Given a range of numbers finds the number with the largest hailstone sequence

#  Name: Shaomik Sarkar

#  Date Created: 2/28/2015

#  Date Last Modified: 2/28/2015
##############################################################################################
# Part 1: Checking if the inputs are positive and the range makes sense
#
##############################################################################################
def main(): 
 n1 = int(input("Enter starting number of the range: "))
 n2 = int(input("Enter ending number of the range: "))

 while n1<=0:
  n1 = int(input("Enter starting number of the range: "))
  n2 = int(input("Enter ending number of the range: "))
 while n2<=0:
  n1 = int(input("Enter starting number of the range: "))
  n2 = int(input("Enter ending number of the range: "))
 while n1 > n2:
  n1 = int(input("Enter starting number of the range: "))
  n2 = int(input("Enter ending number of the range: "))     
##############################################################################################
# Part 2: Setting up counters for counting number of sequences, maximum number of sequences
# and number with the maximum sequence
##############################################################################################
 n = n1
 count =0
 maxcount = 0
 maxnum= n1
##############################################################################################
# Part 3: nested loops with outer loop going till the range is exhausted and inner loop going
# on till the sequence hits 1
##############################################################################################
 
 while n1 <= n2:
  n = n1
  count = 0
  while n != 1:
   if n%2 == 0:
    n = n//2
    count = count + 1
   else:
    n = (n*3) + 1
    count = count +1
  if count > maxcount:
   maxcount = count
   maxnum = n1
  n1= n1+1
##############################################################################################
# Part 4:  Printing the number with the largest hailstone sequence
#
##############################################################################################
 print("The number", maxnum, "has the longest cycle length of",maxcount,".") 
main()  
##############################################################################################
#                                       END                                                  #
#                                                                                            #
############################################################################################## 
 
