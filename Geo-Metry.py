
#  Description: A program the manipulates given points into geometric shapes
#  Name: Shaomik Sarkar
#  Date Created: 10/16/2015
#  Date Last Modified: 10/16/2015
##############################################################################
#
#
##############################################################################
import math


class Point(object):
 
 def __init__(self, pointlist):
  self.a = pointlist[0]
  self.b = pointlist[1]
   
   
 def dist(self, other):
  self.c = math.sqrt(((self.a - self.b)**2) + ((other.a - other.b)**2)) #distance formula
  return self.c

 def __str__(self):
  return ("(" + str("{0:.3f}".format(self.a)) +","+ str("{0:.3f}".format(self.b)) + ")")


 def __eq__(self, other):
  return(is_equal(self.a,other.a) and is_equal(self.b,other.b))

###############################################################################

class Line(object):
 
  
 def __init__(self,pointA,pointB):
  self.a1 = pointA[0]
  self.a2 = pointA[1]
  self.b1 = pointB[0]
  self.b2 = pointB[1]
  if pointB[0] - pointB[1] == 0 and pointA[0] - pointA[1] != 0:     #check slope to see if its horizontal(numerator is zero)
   self.slope = "Horizontal"
  elif self.a1 - self.a2 == 0:     #check slope to see if its vertical(if denominator is zero)
   self.slope = "Vertical"
  else:
   self.slope = (pointB[0] - pointB[1]) / (pointA[0] - pointA[1])

   

 def isHorizontal(self):
  if self.slope == "Horizontal":
   return True
  else:
   return False

 def isVertical(self):
  if self.slope == "Vertical":
   return True
  else:
   return False

 def xIntercept(self): 
  if self.isVertical:     #if statement checking for every situation the y intercept is NAN or zero
   return (self.a1)
  elif self.isHorizontal:
   return (float("inf"))
  else: 
   return ((-1*(self.a2 - (self.slope * self.a1)))/self.slope) #formula for x- intercept
  
 def yIntercept(self):
  if self.isVertical:
   if self.a1 == 0 or self.b2 == 0:    #if statement checking for every situation the y intercept is NAN or zero
    return(0)
   else:
    return (float("inf"))
  elif self.isHorizontal:
   return (self.a2)
  else:
   return (self.a2 - (self.slope * self.a1))

 
 def isPerpendicular(self,other):
  if self.slope == -1*(1/other.slope):  #formula for perpendicular slopes
   return True
  else:
   return False

 def isParallel(self, other):
  if is_equal(self.slope, other.slope):
   return True
  else:
   return False

 def isOnLine(self, pt):
  self.left =  pt.b - self.b  #left side of line equation
  self.right = self.slope * (pt.a - self.a) #right side of line equation
  return (is_equal(self.left, self.right))

 def perpDist(self,pt):
   return (abs((-1 * self.slope * pt[0]) + pt[1] + (-1 * self.yIntercept()))/(math.sqrt((self.slope * self.slope) + 1)))   #formula for perpendicular distance

 def intersectionPoint(self, other):
  if is_equal((self.slope - other.slope), (other.yIntercept() - self.yIntercept())): #formula for intersection point
   return True
  else:
   return False

 def __str__(self):
  self.m = str("{0:.3f}".format(self.slope))
  self.b = str("{0:.3f}".format(self.yIntercept()))
  self.x = str("{0:.3f}".format(self.xIntercept()))
  if self.isVertical():
   return (self.x)
  elif self.isHorizontal():
   return (self.b)
  else:
   return ("y = " + self.m + "x" + "+" + self.b)

########################################################################################################################

class Circle(object):

 def __init__(self,radius, center):
  self.r = radius
  self.ca = center[0]
  self.cb = center[1]


 def circumference(self):
  return (2 * math.pi * self.r)  #fomula for circumference

 def area(self):
  return (math.pi * self.r * self.r) #fomula for area

 def containsPoint(self, pt):
  if ((pt.a - self.ca)**2) + ((pt.b - self.cb)**2) < (self.r**2): #checks to see how far the point is from center and compares to radius 
   return True
  else:
   return False
 
 def hasTangentLine(self,line):
  if is_equal(line.perpDist([self.ca,self.cb]), self.r): #checks to see if any point of the line is equal in distance to the radius
   return True
  else:
   return False

 def __str__(self):
  return ("The circle has radius " + str("{0:.3f}".format(self.r)) + " and center " + "(" + str("{0:.3f}".format(self.ca)) + "," + str("{0:.3f}".format(self.cb)) + ")")      
  





###################################################################################################################
def is_equal(a, b):
  tolerance = 1.0e-16
  return (abs (a-b) < tolerance)




###################################################################################################################
  
def main():
 inFile = open("geometry.txt", "r")
 line1 = inFile.readline()

 pt = [float(x) for x in line1.split()]
 PointA = Point(pt)
 line2 = inFile.readline()
 linecoord = [float(x) for x in line2.split()]
 linept1 = [linecoord[0],linecoord[1]]
 linept2 = [linecoord[2],linecoord[3]]
 line3 = inFile.readline()
 pt1 = [float(x) for x in line3.split()]
 PointB = Point(pt1)
 line4 = inFile.readline()
 circoord = [float(x) for x in line4.split()]
 circleR = circoord[0]
 circleC = [circoord[1],circoord[2]]
 circle1 = Circle(circleR,circleC)
 LineCD = Line(linept1,linept2)
 LineAB = Line(pt, pt1)
 print (PointA)
 print (PointB)
 print ("{0:.3f}".format(PointA.dist(PointB)))
 print ("{0:.3f}".format(LineAB.slope))
 print ("{0:.3f}".format(LineAB.xIntercept()))
 print ("{0:.3f}".format(LineAB.yIntercept()))
 print (LineAB)
 print (LineCD)
 print (LineAB.isParallel(LineCD))
 if not (LineAB.isParallel(LineCD)):
  print (LineAB.intersectionPoint(LineCD))
 print(LineAB.isPerpendicular(LineCD))
 print(circle1)
 pp = [4.0,8.0]
 P = Point(pp)
 qq = [9.0, 3.4]
 Q = Point(qq)
 circle2 = Circle(10.0, [8.0, 9.0]) 
 print (circle2)
 print (circle1.containsPoint(P))
 print (circle1.containsPoint(Q))
 print (circle2.hasTangentLine(LineCD))
 inFile.close()
 
 
 
  
 
 
 
    


main()
############################################################################################










    
  
