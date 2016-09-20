
#  Description: Checks to see if the tags in an html file all close.
#  Name: Shaomik Sarkar
#  Date Created: 10/23/2015
#  Date Last Modified: 10/23/2015

###################################################################################################################
#stack operations

class Stack(object):
 
 def __init__(self):
  self.items = []
 
 def push(self, item):
  self.items.append(item)

 def pop(self):
  return self.items.pop()

 def peek(self):
  return self.items[-1]

 def isEmpty(self):
  return self.items == []

 def size(self):
  return len(self.items)

####################################################################################################################

def getTag(inpFile):
 
 inFile = open(inpFile, "r")
 tag = ""
 listTags = [] #holds temporary tags till appended to the final lis
 brloop = True
 brloop1 = True
 while brloop1 == True: #reads characters until it finds the opening of a tag
  char = inFile.read(1)   
  if (char == "<"):
   char = inFile.read(1)
   while brloop == True:
    if char == ">" or char == " ":   
     break
    else:
     tag += char #puts characters into a string till it reaches > to complete tag
     char = inFile.read(1) 
  if tag == "/html":   #ends when it reaches the last tag for all html files
    listTags.append(tag)  
    break
  elif tag != "":
   listTags.append(tag) #appends tag to our return list if its not an empty tag and between <>
   tag = ""
 return listTags  
 inFile.close()    
 

####################################################################################################################

def main():
 exceptionList = ["area","base","br","col","command","embed","hr","img","input","link","meta","param","source"]   
 MyTagList = getTag("htmlfile.txt")
 MyStack = Stack()
 NoError = True
 while NoError == True:
  for element in MyTagList:
   if element in exceptionList: #checks for all exceptions
    #MyStack.pop()   
    print ("Tag is ", element, ": does not need to match:  stack is now ", MyStack.items)
   elif element[0] == "/" : #if its an end tag we see if there is a start tag of it on top of the stack and takes it off the stack if it matches
    if MyStack.peek() == element[1:]: #compare the two tags without the "/" on the closing tag to check if they are equal
     MyStack.pop()
     print("Tag is ", element,": matches:  stack is now ", MyStack.items)  
    else:
     print ("Error:  tag is ", element, "but top of stack is", MyStack.peek()) #if tags don't match then there is an error in the ordering of tags
     NoError = False
   else:
    MyStack.push(element)
    print("Tag is ", element, " : pushed:  stack is now ", MyStack.items)
  if MyStack.isEmpty() and NoError == True: #if the stack is empty and has no errors then all the tags close and are good
   print ("Processing complete.  No mismatches found.")
  elif MyStack.items != [] and NoError == True: #if there are items left then their pairs were not found so the tags are incorrect
   print ("Processing complete.  Unmatched tags remain on stack: ", MyStack.items)   
  break  

###################################################################################################################
main()
 









