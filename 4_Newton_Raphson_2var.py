# -*- coding: utf-8 -*-
"""
Purpose: finding the Intersection between of the given equation
         using Newton–Raphson method and using sympy.
@author: Ashwin Raju Kharat
Roll No: M220590PH
Date: 28:09:2022
"""

#Importing the sympy,numpy,matploit package
import sympy as sp
import numpy as np
from matplotlib import pyplot as plt

#Defining the Symbols and the Functions 
x=sp.Symbol("x")
y=sp.Symbol("y")
func1=pow(x,2)+pow(y,2)-1
func2=y-pow(x,2)
#Finding the first derivative of given function
func1_dx=sp.diff(func1,x)
func1_dy=sp.diff(func1,y)
func2_dx=sp.diff(func2,x)
func2_dy=sp.diff(func2,y)

#this definition is for plotting easily
def fn(x):
    return np.sqrt(1-pow(x,2))
def gn(x):
    return pow(x,2)

#Defining the Determinant Function
def det(M):
    ans=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    return ans

#Defining the Newton–Raphson method for 2 variable.
def N_R_2(x0,y0,esp):
    
    #initializing with an higher value for x1 and y1
    x1=x0+10*esp
    y1=y0+10*esp
    
    while (abs(x1-x0)>=esp ) and (abs(y1-y0)>=esp ):
    
        x0=x1
        y0=y1
        
        #Creating the Matrix of the D and Solving the determinant 
        Darr =[[func1_dx.evalf(subs={x:x0,y:y0}), func1_dy.evalf(subs={x:x0,y:y0})],
             [func2_dx.evalf(subs={x:x0,y:y0}) , func2_dy.evalf(subs={x:x0,y:y0})]] 
        #print(Darr)
        D=det(Darr)

        #Creating the Matrix of the h and Solving the determinant 
        harr=[[-func1.evalf(subs={x:x0,y:y0}),func1_dy.evalf(subs={x:x0,y:y0})],
                [-func2.evalf(subs={x:x0,y:y0}),func2_dy.evalf(subs={x:x0,y:y0})]]
        h=det(harr)/D
        #print(h)
        
        #Creating the Matrix of the k and Solving the determinant 
        karr=[[func1_dx.evalf(subs={x:x0,y:y0}),-func1.evalf(subs={x:x0,y:y0})],
              [func2_dx.evalf(subs={x:x0,y:y0}),func2.evalf(subs={x:x0,y:y0})]]
        k=det(karr)/D
        #print(k)
        x1=x0+h
        y1=y0+k

    return x1,y1

#Initial condition for first Intersection
x0,y0=0.7,0.7
esp=pow(10,-6)

#solving the intersection by calling the Newton–Raphson method for 2 variable
intx,inty=N_R_2(x0,y0,esp)
print("Intersection Of the Given function is at \n x = {0} ; y = {1}".format(round(intx,4),round(inty,4)))
#Doing same for other root
x0,y0=-0.7,0.7
intx2,inty2=N_R_2(x0,y0,esp)
print("Intersection Of the Given function is at \n x = {0} ; y = {1}".format(round(intx2,4),round(inty2,4)))

#Combining roots for plotting
xroots=[intx,intx2]
yroots=[inty,inty2]

#Bellow is just a plot and Beautification.
a,b,esp=-1,1,pow(10,-4)
#Plot the given function 
xline=np.linspace(a,b,int(abs(a-b)/esp))

plt.plot(xline,fn(xline),'k',label="$Fn(x)=x^2+y^2-1$")
plt.plot(xline,-fn(xline),'k')

plt.plot(xline,gn(xline),label="$Fn(x)=x^2$")
plt.plot(xroots,yroots,"r*",label="Intersection (x,y)=(+{0},{1} \n(x,y)=(-{0},{1})".format(round(intx,4),round(inty,4)))
#plotting the root
#plt.plot(root,func.evalf(subs={x:root}),'k*',label="root at x={0}".format(round(root,4)))

#Making the plot look pretty
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.title("Finding Intersection Using Newton–Raphson Method and SymPY")
plt.legend()
plt.axvline(x=0,color='red',ls="--")
plt.axhline(color='red',ls="--")
plt.ylim(-2,2)
plt.xlim(-2,2)
plt.show()

#--------THE-END-------------------------------------#