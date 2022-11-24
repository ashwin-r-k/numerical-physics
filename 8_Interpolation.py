# -*- coding: utf-8 -*-
"""
Aim : To Find Polynomial of for the given data points 
        using Newtons Forward Interpolation Method.
@author: Ashwin Raju Kharat
Roll no: M220590PH
Date: 9 Nov 2022
"""
#Resetting the Environment clearing all values
from IPython import get_ipython
get_ipython().magic('reset -sf')

#Initial Values

points_x=[0,2,4,6]
points_y=[2,6,18,38]
point=2


#-----------code--------#
#Importing the necessary libraries.
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#Function to make the Matrix of deltas 
def delta(x,y):
    dels=np.zeros((len(x),len(x)))
    dels[:,0]=y[:].copy()

    for i in range(1,len(dels)):
        for j in range(0,len(dels[i])-i):
            dels[j,i]=dels[j+1,i-1,]-dels[j,i-1]
    return dels

#Function is definition of Newtons Forward Difference method.
def Newtons_fd(points_x,points_y,point):
    dels=delta(points_x,points_y)
    #print(dels)
    h=points_x[1]-points_x[0]
    
    sum=0
    
    x=sp.Symbol("x")
    p=(x-points_x[0])/h
    
    for k in range(0,len(points_x)):
        mult=1
        for i in range(0,k):
            mult=mult*(p-i)/(i+1)
        #print("mult {0} : {1} ".format(k,mult))
        sum=sum+mult*dels[0,k]
    #print("sum=",sum)
    #print("Equation for given points: \n y={0}".format(sp.simplify(sum)))
    
    val=sp.lambdify(x,sum)
    return val(point),sp.simplify(sum)

#Calling and solving storing value in a.
a=Newtons_fd(points_x,points_y,point)
print("Equation  using Interpolation for given data points: \n y={0}".format(a[1]))
print("Solution  using Interpolation at x={0} is y={1}  ".format(point,a[0]))

#Plotting the solution.
plt.plot(points_x,points_y,"*r",label="Input Data Points")
plt.plot(np.linspace(min(points_x),max(points_x),100),
         Newtons_fd(points_x,points_y,np.linspace(min(points_x),max(points_x),100))[0]
         ,"g",label="Solved using Interpolation ")

#Making the plot look good.
plt.legend()
plt.grid(True)
plt.title("$y={0}$".format(a[1]))
plt.axvline(x=0,color='black')
plt.axhline(color='black')
plt.show()
#---------------The-END--------------------------------------#
