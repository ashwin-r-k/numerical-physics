# -*- coding: utf-8 -*-
"""
Aim: Solving function using Secant method
@author: Ashwin Raju Kharat
Roll No: M220590PH
Date: 21:09:2022
"""

import numpy as np
from matplotlib import pyplot as plt
#Importing the numpy,matploit package

#this definition is for plotting easily
def fn(x):
    y=2*np.sin(x)+3*pow(np.e,-x)+4*pow(x,3)-4
    #This denotes the given function 
    return y

#Initialization of the Values
x0=-1
x1=2
esp=pow(10,-4)
#that is  0.0001



#Below definition is the implication of secant method
def secant(x0,x1,esp):
    itter=0
    x=[]
    x.append(x0)
    x.append(x1)
    
    while abs(x[-1]-x[-2])>=esp:
        
        temp= x[-2]-fn(x[-2])*(x[-2]-x[-1])/(fn(x[-2]-fn(x[-1])))
        x.append(temp)
        itter+=1
        
    return x[-1],itter

#Calling Secant method to solve
root,itter=secant(x0,x1,esp)
print("The root for above given equation is {0} \nfound in {1} itter".format(round(root,4),itter))

#Bellow is just a beautifying plot.
a,b=-1,2
#Plot the given function 
xline=np.linspace(a,b,int(abs(a-b)/esp+1))
plt.plot(xline,fn(xline),label="$Fn(x)=2*sin(x)+3e^{-x}+4x^3-4$")

#plotting the root
plt.plot(root,fn(root),'k*',label="root at x={0}".format(round(root,4)))

#Making the plot look pretty
plt.xlabel("x")
plt.ylabel("y")
plt.title("Finding Root Using Secant Method")
plt.grid(True)
plt.legend()
plt.axvline(x=0,color='red',ls="--")
plt.axhline(color='red',ls="--")

#--------THE-END-------------------------------------#