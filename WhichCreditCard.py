
#  Description: Reads a credit card number from user and tells the user if the card is valid or not and returns what type of card it is.

#  Name: Shaomik Sarkar	

#  Date Created: 3/6/2015

#  Date Last Modified: 3/7/2015


#######################################################################################################
# Part 1: Functions list - is_valid checks if the credit card is a 15 0r 16 digit card and the cc_type
# functions determines what credit card type it is.
#######################################################################################################
def is_valid (cc_num):
 if len(str(cc_num)) == 16 or len(str(cc_num)) == 15:
   return (True)
 else:
   return (False)  
#######################################################################################################

def cc_type (cc_num):
 if len(str(cc_num)) == 16:
  a = cc_num // 1000000000000
  if a == 6011:
   print ("Valid Discover credit card number")
  a = a // 10
  if a == 644:
   print ("Valid Discover credit card number")
  a = a // 10
  if a == 65:
   print ("Valid Discover credit card number")
  elif a == 34:
   print ("Valid American Express credit card number") 
  elif a == 37:
    print ("Valid American Express credit card number") 
  elif a >= 50 and  a <= 55:
    print ("Valid MasterCard credit card number") 
  a = a // 10
  if a == 4:
    print ("Valid Visa credit card number")
 elif len(str(cc_num)) == 15:
  a = cc_num // 100000000000
  if a == 6011:
   print ("Valid Discover credit card number")
  a = a // 10
  if a == 644:
   print ("Valid Discover credit card number")
  a = a // 10
  if a == 65:
   print ("Valid Discover credit card number")
  elif a == 34:
   print ("Valid American Express credit card number") 
  elif a == 37:
    print ("Valid American Express credit card number") 
  elif a >= 50 and  a <= 55:
    print ("Valid MasterCard credit card number") 
  a = a // 10
  if a == 4:
    print ("Valid Visa credit card number")
  else:
    print ("Valid credit card number")
#########################################################################################
# Part 2: Main functions which performs the Luhn's test by dividing the card into even
# and odd digits and doing the specifified calculations. If the test fails it tells the
# user that the card is invalid.
#########################################################################################
def main():
 creditCard = eval(input ('Enter 15 or 16-digit credit card number:'))
 cc = creditCard
 sumEven = 0
 sumOdd = 0
 sumTotal = -1
 cc_count = 0
 if is_valid(creditCard):
  while cc > 0:
   sumEven = sumEven + (cc%10)
   cc = cc // 100
  cc =  creditCard
  cc = cc // 10
  while cc > 0:
   cc_count = 2* (cc%10)
   sumOdd = sumOdd + ((cc_count%10) + (cc_count//10))
   cc = cc // 100
  sumTotal = sumEven + sumOdd 
  if sumTotal % 10 == 0:
   cc_type(creditCard)
  elif sumTotal != -1:
   print ("Invalid credit card number")
 else:
  print ("Not a 15 or 16-digit number")
###########################################################################################
# Part 3: Calling the main function
#
###########################################################################################
main()  
###########################################################################################
#                                           END                                           #
###########################################################################################  
    
   















 
