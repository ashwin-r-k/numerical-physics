#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aim = Implicit and Explicit Euler Method.
@author: Ashwin Raju Kharat
Roll no: M220590PH
Date: 23 Nov 2022

dy/dx=f(x,y) ;
y(x0)=y0

y'=x+y ;y(0)=0
answer: y(x) = -x + e^x - 1
"""

#--Initial Conditions--for dy/dx=x+y ; y(0)=0 #
x=0
y=0

xmin=0
xmax=7
#step size
h=0.5

#Defination of the function and solution for exact.
def func(x,y):
    return x+y
def exact(x):
    return pow(np.e,x)-x-1

##--------Code----#
#Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#Defination for solving the Euler method implicitly.
def euler_imp(func,x,y,xmin,xmax,h):
    
    x=[x]
    y=[y]
    for i in np.arange(xmin, xmax+h,h):
        
        x.append( i )
        y.append(  y[-1] + h*func(i,y[-1]) )
    return x,y

#Defination for solving the Euler method Explicitly.
def euler_exp(func,x,y,xmin,xmax,h):
    
    x=[x]
    y=[y]
    for i in np.arange(xmin, xmax+h,h):
        
        x.append( i )
        y.append(  y[-1] + h*func(i,y[-1]) )
        y[-1] = y[-2] + h*(func(x[-1],y[-2]) + func(x[-1],y[-1]))/2
    return x,y

#Solving using Euler method
Xs,Ys=euler_imp(func,x,y,xmin,xmax,h)
Xs_exp,Ys_exp=euler_exp(func,x,y,xmin,xmax,h)

#Ploting the solutions
plt.plot(Xs,Ys,':',label="Implicit method")
plt.plot(Xs_exp,Ys_exp,"-.",label="Explicit method")

xline=np.linspace(xmin,xmax)
plt.plot(xline,exact(np.array(xline)),label="exact solution ")

#Making plot look good
plt.xlabel("x")
plt.ylabel("y")
plt.title("Euler Method solution of $dy/dx=x+y$ \n $y(x) = -x + e^x - 1$")
plt.axhline(color="black")
plt.axvline(color="black")
plt.grid(True)
plt.legend()
plt.show()
#--------THE-END-------------------------------------#
