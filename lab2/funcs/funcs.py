#Name:Tarini Srikanth
#Instructor: Turner-05
#Project: Lab 2
import math
def f(x):
    xSquared= x*x
    value = 7*xSquared+ 2*x
    return value
def g(x,y):
    xSquared= x*x
    ySquared = y*y
    value = (xSquared+ySquared)/(3*x)
    return value
def hypotenuse(length1,length2):
    cSquared = (length1*length1)+(length2*length2)
    c = math.sqrt(cSquared)
    return c
def is_positive(num):
    return(num>0)

