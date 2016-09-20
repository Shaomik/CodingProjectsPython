
#  Description: Simulates an emergency room environment using queues
#  Name: Shaomik Sarkar
#  Date Created: 10/30/2015
#  Date Last Modified: 10/30/2015
########################################################################
import sys     #for the exit command
########################################################################

class Queue(object):     #our queue with all its methods

 def __init__(self):
  self.items = []

 def isEmpty(self):
  return (self.items == [])

 def enqueue(self, item):   #adds item to the front of the list
  self.items.insert(0,item)

 def dequeue(self):        #removes item from end of the list
  return (self.items.pop())

 def size(self):
  return(len(self.items))

 def peek(self):          #shows the first queued item
   return (self.items[-1])
#########################################################################

def treatNext(criticalQ, seriousQ, fairQ): 
 noPatient = False 
 if not criticalQ.isEmpty():    #if statement removes the first queued item from the highest pritoty list that has someone queued
  removed = criticalQ.peek() #removed and removeQ are counters for ease of using print statements in the end instead of in every if,elif,else statements
  removeQ = "Critical"
  criticalQ.dequeue()
 elif not seriousQ.isEmpty():
  removed = seriousQ.peek()
  removeQ = "Serious"
  seriousQ.dequeue()
 elif not fairQ.isEmpty():
  removed = fairQ.peek()
  removeQ = "Fair"
  fairQ.dequeue()
 else:
  noPatient = True               #if all lists are empty 
  print ("No patients in queues")
  print(" ")
 if noPatient == False:
  print("Treating", removed, "from", removeQ, "queue")
  print ("Queues are: ")
  print ("Critical: ", criticalQ.items)
  print ("Serious: ", seriousQ.items)
  print ("Fair: ", fairQ.items)
  print (" ")

#########################################################################

def main():
    
 inFile = open("ERsim.txt", "r")
 
 criticalQ = Queue()   #create three queues for the three priority levels of Critical, Serious and Fair respectively
 seriousQ = Queue()
 fairQ = Queue()


 for line in inFile:
  line = line.strip()
  line = line.split()
  if line[0] == "add":    #we check what queue and add the item to our queue
   if line[2] == "Critical":
    criticalQ.enqueue(line[1])
   elif line[2] == "Serious":
    seriousQ.enqueue(line[1])
   else:
    fairQ.enqueue(line[1])
   print("Add patient", str(line[1]), "to", str(line[2]), "queue")
   print ("Queues are: ")               #prints out all the queues
   print ("Critical: ", criticalQ.items)
   print ("Serious: ", seriousQ.items)
   print ("Fair: ", fairQ.items)
   print (" ")

  elif line[0] == "treat" and line[1] == "next":   #use the treatNext function for this command
   print("Treat next patient")
   print(" ")
   treatNext(criticalQ, seriousQ, fairQ)

  elif line[0] == "treat" and line[1] == "all":  #loops the treatNext function till everyone is treated,with critical queue first, and so on
   print("Treat all patients")
   while not criticalQ.isEmpty():
    treatNext(criticalQ, seriousQ, fairQ)    
   while not seriousQ.isEmpty():
    treatNext(criticalQ, seriousQ, fairQ)
   while not fairQ.isEmpty():
    treatNext(criticalQ, seriousQ, fairQ)
  
  elif line[0] == "exit": #exits the program
   print ("Exit")   
   sys.exit() 

####################################################################

main()

####################################################################
















