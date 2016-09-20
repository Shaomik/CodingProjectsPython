

#  Description: Compares and contrasts two authors' use of vocabulary in their books. 

# Name: Shaomik Sarkar

#  Date Created: 05/06/2015

#  Date Last Modified: 05/06/2015

###############################################################################################
word_dict = {}
def create_word_dict ():
  infile = open ("words.txt", "r")
  for line in infile:
    word = line.strip
    word_dict[word] = 1
  infile.close()
###############################################################################################   

def parseString (line):
  
  line_string  = ""
  line.replace("'s","")
  line.replace("' ", " ")
  line.replace(" '", " ")
  for ch in line:   
    if ((ch >= "a" and ch <= "z") or ch == "'"):
      line_string += ch
    else:
      line_string += " "
  return line_string
################################################################################
def main():
  total_words = 0
  total_words1 = 0
  cap_words = []
  cap_words1 = []
  book_dict = {}
  book1_dict ={}
  word_set = set()
  word_set1 = set()
  #
  create_word_dict()
  # Enter names of the two books in electronic form
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()

  # Enter names of the two authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  print() 
  
  TheBook = open (book1, "r")
  for line in TheBook:
    line = line.strip()
    line = parseString (line)
 # split the line into individual words
    word_list = line.split()

    # add words to the set of words and dictionary
    for word in word_list:
      word_set.add (word)
      total_words += 1

      if word[0] >= "A" and word[0] <= "Z":
        cap_words.append(word)

      # add words to the book dictionary
      if word in book_dict:
        book_dict[word] = book_dict[word] + 1
      else:
        book_dict[word] = 1
    for word in cap_words:
      if (word.lower()) in book_dict:
        book_dict[word.lower()] = book_dict[word.lower()] +1
      elif (word.lower()) in word_dict:
        book_dict[word.lower()] = 1
      del book_dict[word]
###################################################################################################
  #frequency of unique words
  dist_word1 = list(book_dict.keys())
  distinctWords = len(dist_word1)
  print (author1)
  print("Total distinct words = ", distinctWords)
  print("Total words (including duplicates) = ", total_words)
  print("Ratio(% of total distinct words to total words) = ", ((distinctWords/total_words)*100))
  TheBook.close()
  setA = set(book_dict.keys())
#####################################################################################################
  TheBook1 = open (book2, "r")
  for line in TheBook1:
    line = line.strip()
    line = parseString (line)
 #split the line into individual words
    word_list = line.split()

    # add words to the set of words and dictionary
    for word in word_list:
      word_set1.add (word)
      total_words1 += 1

      if word[0] >= "A" and word[0] <= "Z":
        cap_words1.append(word)

      # add words to the book dictionary
      if word in book1_dict:
        book1_dict[word] = book1_dict[word] + 1
      else:
        book1_dict[word] = 1
    for word in cap_words1:
      if (word.lower()) in book1_dict:
        book1_dict[word.lower()] = book1_dict[word.lower()] +1
      elif (word.lower()) in word_dict:
        book1_dict[word.lower()] = 1
      del book1_dict[word]
#########################################################################################################################################
  dist_word2 = list(book1_dict.keys())
  distinctWords = len(dist_word2)
  print()
  print (author2)
  print("Total distinct words = ", distinctWords)
  print("Total words (including duplicates) = ", total_words1)
  print("Ratio(% of total distinct words to total words) = ", ((distinctWords/total_words1)*100))
  TheBook1.close()
  setB = set(book1_dict.keys())
##########################################################################################################################################  
  DtoH = list(setA-setB)
  HtoD = list(setB -setA)
  Dtotal = 0
  for k in range (len (DtoH)):
   Dtotal +=  book_dict[DtoH[k]]
  Htotal = 0
  for i in range (len (HtoD)):
   Htotal +=  book1_dict[HtoD[i]]
#########################################################################################################################################
  print()
  print (author1, 'used', len(DtoH), 'words that', author2, 'did not use.')
  print ('Relative frequency of words used by', author1, 'not in common with', author2, '=', ((Dtotal/total_words)*100))
  print ()
  print (author2, 'used', len(HtoD), 'words that', author1, 'did not use.')
  print ('Relative frequency of words used by', author2, 'not in common with', author1, '=', ((Htotal/total_words1)*100))      

#########################################################################################################################################  
  
 
main()
