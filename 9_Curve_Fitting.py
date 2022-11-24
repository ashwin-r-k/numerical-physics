# -*- coding: utf-8 -*-
"""
Aim: To Find a curve of given degree polynomial to a set of data.
@author: Ashwin Raju Kharat
Roll no: M220590PH
Date: 16 November 2022
"""
#using this to clear all variables and resetting Environment.
from IPython import get_ipython
get_ipython().magic('reset -sf')

"""
##Sample data points for linear
point_x=[1,3,5,8]
point_y=[5,8,12,20]
dep=1
"""

##Sample data points for 2 deg poly
point_x=[1,2,3,3.9,5,6.1,7,8]
point_y=[1,4,8,15.5,24,49,49,64]
dep=2
#dep= degree of polynomial

#Importing required libraries
import numpy as np
from matplotlib import pyplot as plt
import sympy as sp

#Defining the curve fitting method 
def curve_fitting(point_x,point_y,dep):
    
    a=np.zeros((dep+1,dep+1))
    b=np.zeros((dep+1,1))
    
    for i in range(dep+1):
        
        for j in range(dep+1):
            sum_a=0
            for k in range(len(point_x)):
                sum_a=sum_a+pow(point_x[k],i+j)
            a[i][j]=sum_a
        
        sum_b=0
        for j in range(len(point_x)):
            sum_b+=point_y[j]*pow(point_x[j],i)
        b[i]=sum_b
            
    X=np.linalg.solve(a,b)
    
    poly=0
    for i in range(dep+1):
        poly+=round(X[i][0],4)*pow(x,i)

    return poly
#It return a polynomial as an sympy object.


#defining x solving and calling 
x=sp.Symbol("x")
poly=curve_fitting(point_x,point_y,dep)

#taking few variables to be used in plot
ext=abs(max(point_x)-min(point_x))/3
axis_x=np.linspace(-ext+min(point_x) ,ext+max(point_x))
axis_y=sp.lambdify(x,poly)

#printing Answer
print("Equation found using curve fitting for given data points: \n degree of polynomial={0} \n y={1}".format(dep,poly))

#plotting solution
plt.figure()
plt.plot(point_x,point_y,"*r",label="Input Data Points")
plt.plot(axis_x,axis_y(axis_x),"--g",label="Solved using curve fitting")

#Making the plot look good
plt.legend()
plt.grid(True)
plt.title("$y={0}$".format(poly))
plt.axvline(x=0,color='black')
plt.axhline(color='black')
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#---------------The-END--------------------------------------#
"""
#Extra 

print("Fun with polynomial")
ext=abs(max(point_x)-min(point_x))/3
axis_x=np.linspace(-ext+min(point_x) ,ext+max(point_x))
plt.figure()
plt.title("Fun with Curve fitting")
plt.plot(point_x,point_y,"*r",label="Input Data Points")

for dep in range(1,4):
    
    poly=curve_fitting(point_x,point_y,dep)
    axis_y=sp.lambdify(x,poly)


    print("Equation found using curve fitting for given data points: \n degree of polynomial={0} \n y={1}".format(dep,poly,4))

    plt.plot(axis_x,axis_y(axis_x),"--",label="degree = {0}".format(dep))
    
plt.legend()
plt.grid(True)
plt.axvline(x=0,color='black')
plt.axhline(color='black')
plt.show()
"""
#---------------The-END--------------------------------------#

