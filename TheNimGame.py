
#  Description: Uses an algorithm to check if the move will decide a win or loss in the game, and uses the best move according to the algorithm

#  Name: Shaomik Sarkar

#  Date Created: 9/11/2015

#  Date Last Modified: 9/11/2015

#########################################################################################################################
# The Nim Game
#
#########################################################################################################################
def main():
#################################################################################
 # Part 1: Open and read file to check the number of heaps seperate the 3 heaps
 #
 ################################################################################
 in_File = open ("nim.txt", "r")
 line1 = in_File.readline()
 line1 = line1.strip()
 num_sets = int (line1)
 i = 0
 while i != num_sets:
  set = in_File.readline()
  set = set.strip()
  set = [int(i) for i in set.split()]
  a = set[0]
  b = set[1]
  c = set [2]
##############################################################################
# Part 2: Finding the total and individual nim sums
#
##############################################################################
  nimsum = a ^ b ^ c
  if nimsum == 0:
   print("Heaps:" , a , b, c,  ":", "You lose")
  else:
   p = a ^ nimsum
   q = b ^ nimsum
   r = c ^ nimsum
##############################################################################
# Part 3: Find which heap has lower individual nim sum than heap and calculate
#         the number to remove from that heap  
##############################################################################
   if p < a:
    move = a - p
    print("Heaps:" , a , b, c,  ":", "remove", move, "from Heap 1")
   elif q < b:
    move = b - q
    print("Heaps:" , a , b, c,  ":", "remove", move, "from Heap 2")
   elif r < c:
    move = c - r
    print("Heaps:" , a , b, c,  ":", "remove", move, "from Heap 3")
  i += 1
###############################################################################
 in_File.close()
main()
###############################################################################
#                                END
##############################################################################
   











