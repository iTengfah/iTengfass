# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 19:06:02 2023

@author: ALIENWARE
"""
import numpy as np
L = 12
w = 10

# Question a
# Computing the shear force and bending moment at x = 0
x1 = 0
M1 = (w*(-6*x1**2 + 6*L*x1 - L**2))/12
V1 = w*(L/2 - x1)


moment1 = "The bending moment at the start of span, i.e, x=0 is "
shear1 = "The shear force at the start of the span, i.e. x=0 is "
print()
print("a.i." + moment1 + str(M1) + "KNm")
print("and " + shear1 + str(V1) + "KN")

# Computing the shear force and bending moment at x = L
x = L
M2 = (w*(-6*x**2 + 6*L*x - L**2))/12
V2 = w*(L/2 - x)
moment2 = "The bending moment at the end of span, i.e, x=L is "
shear2 = "The shear force at the end of the span, i.e. x=L is "
print()
print("a.ii." + moment2 + str(M2) + "KNm")
print("and " + shear2 + str(V2) + "KN")



#Question b
 #When the bending moment is zero, we get an expression x**2 - Lx + L**2/6 = 0
#from this
a = 1
b = -(L)
c = (L**2)/6
# as compared to ax^2+bx+c = 0
#finding the discriminant

discriminant = b**2 - 4*a*c
#computing the roots
root1 = (-b + np.sqrt(discriminant))/2*a
root2 = (-b - np.sqrt(discriminant))/2*a
print()
print("b."+"The points of contraflexure are "+str(root1)+" and " +str(root2))


#Question c
# When the shear force is zero, x = L/2

x3 = L/2
print("c."+"Shear force is zero when x=" + str(x3))


#Question d
#By applying an initialized variable, the bending moment at 10mm interval can be acquired by

e = 0       #initial variable
f = 0.01    #interval
g = L + f       #final step
x3 = np.arange(e,g,f) 
M = (w*(-6*x3**2 + 6*L*x3-L**2))/12
print()
print("d. Using the initialized variable,the bending moment at each step in the array is"+ str(M))

#Question e
#For shear force at 10mm interval
V = w *(L/2 *x3)
print()
print("e. Using the initialized variable,the shear force at each step in the array is"+ str(V))

#Question f
"""
Let the absolute value of the bending moment array be AM_value
Also let the minimum AM be min_AM_value
"""
AM_value = abs(M)
m_AM_value = min(AM_value)
""" 
When the bending moment is minimum, we get an expression x**2 - Lx + (L**2/6)+(2*m_AM)/w = 0
"""
#from the above expression 
a = 1
b = -L
c = (L**2/6)+(2*m_AM_value)/w
#By applying the almighty formula to find the roots
discriminant = b**2 - 4*a*c
root_3= (-b + np.sqrt(discriminant))/2*a
root_4 = (-b - np.sqrt(discriminant))/2*a
print()
print("f. The points along the Length of the beam at which the absolute values of the bending moment array is minimum are "+ str(root_3) +" and "+str(root_4))

#Question g
# Computing for relative errors
r_e1 = ((root_3 - root1)/root1*100) 
r_e2 = ((root_4 - root2)/root_4*100)
print()
print("g. The relative errors between the estimated points of contraflexure are "+ str(r_e1)+"% and " + str(r_e2)+"%")


#Question h
#Computing for the maximum and minimum bending moments
#for the maximum
max_moment = max(M)
 
#When the bending moment is max_moment, we get an expression x**2 - Lx + (L**2/6)+(2*max_moment)/w = 0

p = 1
q = -L
r = (L**2/6)+(2*max_moment)/w
#Using the Almighty formula the two roots are;
discriminant2 = q**2 - 4*p*r
root_5 = (-b + np.sqrt(discriminant2))/2*a
root_6 = (-b - np.sqrt(discriminant2))/2*a
print()
print("h.i. The points at which the maximum bending moment occur are "+str(root_5)+" and "+str(root_6))


#for the minimum bending moment
min_moment = min(M)

# When the bending moment is min_moment, we get an expression x**2 - Lx + (L**2//6)+(2*min_moment)/w = 0

k= 1
l = -L
m = (L**2//6)+(2*min_moment)/w
#Using the Almighty formula the two roots are;
discriminant3 = b**2 - 4*a*c
root_7 = (-b - np.sqrt(discriminant))/2*a
root_8 = (-b + np.sqrt(discriminant))/2*a
print()
print("h.ii. The points at which the minimum bending moment occur are "+  str(root_7) + " and " + str(root_8))



