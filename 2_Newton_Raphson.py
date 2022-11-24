# -*- coding: utf-8 -*-
"""
Aim: Finding the root of the given equation using Newton–Raphson method and using sympy
Author: Ashwin Kharat
Roll no: M220590PH
Date: 21 SEP 2022
"""

import sympy as sp
import numpy as np
from matplotlib import pyplot as plt
#Importing the sympy,numpy,matploit package

x=sp.Symbol("x")
func=2*sp.sin(x)+3*sp.exp(-x)+4*pow(x,3)-4
#taking x as a symbol and creating a function
fn=sp.lambdify(x,func)


func_d=sp.diff(func,x)
#Derivative of the function
#this definition is for plotting easily


print("The Given function is $f(x)=$ {0} and \n its derivative is {1}".format(func,func_d))

def Newton_Raphson(x0,esp):
    itter=0
    xi=x0+10*esp
    xip1=x0
    #Defining xi and x(i+1) 
    
    while abs(xip1-xi)>=esp:
        
        xi=xip1
        xip1=xi-func.evalf(subs={x:xi})/func_d.evalf(subs={x:xi})
        #solving the Newton–Raphson method eqn using evalf
        itter+=1
    return xip1,itter


x0=0.5
esp=pow(10,-4)
#that is  0.0001

root,itter=Newton_Raphson(x0,esp)
print("The root for above given equation is {0}  \n found in {1} itter".format(round(root,4),itter))
    
#Following is just for beautifying plot.
a,b=-1,2
#Plot the given function 
xline=np.linspace(a,b,int(abs(a-b)/esp+1))
plt.plot(xline,fn(xline),label="Fn(x)=$2*sin(x)+3e^{-x}+4x^3-4$")


#ploting the root
plt.plot(root,func.evalf(subs={x:root}),'k*',label="root at x={0}".format(round(root,4)))

#Making the plot look pretty
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.title("Finding Root Using Newton–Raphson method Method")
plt.legend()
plt.axvline(x=0,color='red',ls="--")
plt.axhline(color='red',ls="--")
#--------THE-END-------------------------------------#