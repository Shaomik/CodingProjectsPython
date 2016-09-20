
#  Description: Using the turtle graphics to plot graphs on a plot.
#  Name: Shaomik Sarkar
#  Date Created: 9/18/2015
#  Date Last Modified: 9/18/2015

######################################################################################################
#Part1: Setting axis
#
######################################################################################################

import math
import turtle
def main():
 wind = turtle.Screen()
 wind.screensize(900,900)

 turt = turtle.Turtle()
 # forming axis
 turt.goto(400,0)
 turt.goto(-400,0)
 turt.goto(0,0)
 turt.goto(0,400)
 turt.goto(0,-400)
######################################################################################################
# Part 2: Setting axis markers 
#
######################################################################################################
 x = 400
 y = 400
 ticks = -400
 count = -4
 while ticks <= x:
  turt.penup()
  turt.goto(ticks,0)
  turt.pendown()
  turt.goto(ticks,5)
  turt.goto(ticks,-5)
  turt.penup()
  turt.goto(ticks - 5, -20)
  turt.write(count)
  count += 1
  turt.penup()
  ticks += 100
 ticks = -400
 count = -4
 while ticks <= y:
  turt.penup()
  turt.goto(0,ticks)
  turt.pendown()
  turt.goto(5,ticks)
  turt.goto(-5,ticks)
  turt.penup()
  turt.goto(-15, ticks - 8)
  if count != 0:
   turt.write(count)
  count += 1
  ticks += 100
###############################################################################################################
# Part 3: The sine curve
#
###############################################################################################################
 a = -100 * (math.pi)
 b = 100*(math.sin(a/100))
 turt.penup()
 turt.goto(a,b)
 turt.pencolor("red")
 turt.pendown()
 while a <= (100*math.pi):
  b = 100*(math.sin(a/100))
  turt.goto(a,b)
  a += 1
##############################################################################################################
# Part 4: The cosine curve
#
##############################################################################################################
 c = -100 * (math.pi)
 d = 100*(math.cos(c/100))
 turt.penup()
 turt.goto(c,d)
 turt.pencolor("purple")
 turt.pendown()
 while c <= (100*math.pi):
  d = 100*(math.cos(c/100))
  turt.goto(c,d)
  c += 1
##############################################################################################################
# Part 5: The parabola curve
#
##############################################################################################################
 e = -100 * (math.pi)
 f = 100*(((e/100)**2) - 4)
 turt.penup()
 turt.goto(e,f)
 turt.pencolor("yellow")
 turt.pendown()
 while e <= (100*math.pi):
  f = 100*(((e/100)**2) - 4)
  turt.goto(e,f)
  e += 1
##############################################################################################################
# Part 5: The cube function
#
##############################################################################################################
 g = -100 * (math.pi)
 h = 100*(((g/100)**3))
 turt.penup()
 turt.goto(g,h)
 turt.pencolor("green")
 turt.pendown()
 while g <= (100*math.pi):
  h = 100*(((g/100)**3))
  turt.goto(g,h)
  g += 1
################################################################################################################
main() 
#################################################################################################################
#                                   END
#
#################################################################################################################

 



















