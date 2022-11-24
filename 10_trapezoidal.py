#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aim : Numerical Integration using Trapezoidal method.
@author: Ashwin Raju Kharat
Roll no: M220590PH
Date: 23 Nov 2022
"""

#Importing necessary Dependencies.
import numpy as np
import matplotlib.pyplot as plt

#Initial Values
#Limits for integrations.
xmin=0
xmax=4
step_size=1
#Please select an step which divides xmax-xmin .  

#Function to integration over.
def fn(x):
    return np.sin(x)

#-------code--------#
#Function to solve the integration.
def trapezoidal_Int(func,xmin,xmax,step_size):    
    sum=0
    for i in np.arange(xmin+step_size,xmax+step_size,step_size):
        sum+=step_size/2*(func(i-step_size)+func(i))
    Integral=round(sum,4)
    
    return Integral

#Calling and solving the integral
Integral=trapezoidal_Int(fn,xmin,xmax,step_size)
#Printing the solution
print("Numerical Integration using Trapezoidal method = {0}".format(Integral))

#Below is just plot of the solution.
def trapezoidal_plot(func,xmin,xmax,step_size):
      
    plotx=[xmin]
    ploty=[func(xmin)]
    for i in np.arange(xmin+step_size,xmax+step_size,step_size):
        
        plotx.append(i-step_size)
        ploty.append(func(i-step_size))
        
        plotx.append(i)
        ploty.append(func(i))

        plotx.append(i)
        ploty.append(0)
    return plotx,ploty
plotx,ploty=trapezoidal_plot(fn,xmin,xmax,step_size)
xline=np.linspace(xmin,xmax)
plt.plot(xline,fn(xline),label="Given Function ") 
plt.plot(plotx,ploty)
plt.fill_between(plotx,ploty,color= "r",alpha= 0.1,label="trapezoidal area = {0}".format(Integral))
plt.legend()
plt.grid(True)
plt.show()

#---------------The-END--------------------------------------# 
