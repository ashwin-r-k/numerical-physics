"""
Aim : Numerical Integration using Simpson method.
@author: Ashwin Raju Kharat
Roll no: M220590PH
Date: 23 Nov 2022
"""

#Importing necessary Dependencies.
import numpy as np

#Initial Values
#Limits for integrations.
xmin=0
xmax=4
step_size=0.0001
divisons = int((xmax-xmin)/step_size)
#Please select an step which divides xmax-xmin .  

#Function to integration over.
def fn(x):
    return np.sin(x)

#-------code--------#
#Function to solve the integrations
def simpson_Int(func,xmin,xmax,step_size):    
    
    #summing the integral values for each stapes in sum
    sum=func(xmin)+func(xmax)
    n=int((xmax-xmin)/step_size)
    
    for i in range(1,n):
        x=xmin+i*step_size
        if i%2==0:
            sum+=  4*func(x)
        else:
            sum+= 2*func(x)
            
    Integral=round(step_size/3*sum,4)
    
    return Integral

#Printing the solution.
integral_ans=simpson_Int(fn,xmin,xmax,step_size)
print("Numerical Integration using Simpson method for given function = {0}".format(integral_ans))

#---------------The-END--------------------------------------# 
