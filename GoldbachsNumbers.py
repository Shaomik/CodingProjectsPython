

#  Description: Finds the prime pairs of an even number in a range and gives the maximum number of pairs of prime in that range.

#  Name: Shaomik Sarkar

#  Date Created: 3/14/2015

#  Date Last Modified: 3/14/2015

########################################################################
# Part 1: Function list is_prime and main function
#
########################################################################

def is_prime (n):
  limit = int (n ** 0.5) + 1
  div = 2
  if n == 1:
    return (False)
  while (div < limit):
    if (n % div == 0):
      return False
    div = div + 1
  return True

def main():
##############################################################################
#Part 2: Setting loop to check if the limit range and numbers entered are
# valid. Also set counters for calculating number of pairs and maximum no. of
# pairs.
##############################################################################
 LowL = int(input("Enter Lower Limit: "))
 UppL = int(input("Enter upper limit: "))
 while LowL < 4 or LowL % 2 != 0 or UppL % 2 != 0 or LowL > UppL:
  LowL = int(input("Enter Lower Limit: "))
  UppL = int(input("Enter upper limit: "))
 
 counter = LowL
 p2 = 0
 pairCounter = 0
 maxPairs = 0
###############################################################################
#Part 3: Main loop that checks the prime number pair combination of each even 
#number in the range given. For loop checks for every prime number possible
#to make a pair with.
###############################################################################
 
 while counter <= UppL:
  print ("\n", counter, end ="")
  for i in range (2, counter + 1):
   if is_prime(i):
    p2 = counter - i
    if is_prime(p2)and p2 >= i:
     print (" =", i, "+", p2, end="")
     pairCounter = pairCounter + 1
  if pairCounter > maxPairs:
   maxPairs = pairCounter
  pairCounter = 0
  counter = counter + 2
 print ("\n","The maximum number of pairs = ", maxPairs)

main()

   






