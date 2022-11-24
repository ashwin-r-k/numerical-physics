# -*- coding: utf-8 -*-
"""
Aim: To Solve system of linear equation using gauss elimination also using pivoting.
@author: Ashwin Raju Kharat
Roll No: M220590PH
Date: 9 Nov.
"""
"""
Given set of equations: 
Equation : 2.0X+1.0Y+1.0Z=10.0
Equation : 3.0X+2.0Y+3.0Z=18.0
Equation : 1.0X+4.0Y+9.0Z=16.0

solution
 x = 7.0 
 y = -9.0 
 z = 5.0 
 
"""

import numpy as np
#importing the numpy packages

#Creating the 2 d array of 
A = np.array([[2.0, 1.0, 1.0],[3.0,2.0,3],[1,4,9]])
B = np.array([10,18,16])

#Writing Augmented matrix for given problem
AugM = np.array([[2.0, 1.0, 1.0,10.0],[3.0,2.0,3.0,18.0],[1.0,4.0,9.0,16.0]])

#Printing given Equation
for i in range((len(AugM))):
    print("Equation {4} : {0} X + {1} Y + {2} Z = {3}".format(AugM[i][0],AugM[i][1],AugM[i][2],AugM[i][3],i+1 ))


# defining pivoting method
def piv(M):
    for i in range(len(M)):
        
        if M[i][i]==0:
            for j in range(i,len(M)):
                if M[j][i]!=0:
                    temp = M[i].copy()
                    M[i]=M[j].copy()
                    M[j]=temp.copy()
    return M

#Defining the gauss method for solving 
def gaussEl(M):
    
    for i in range(len(M)):
        if M[i][i]==0:
            M=piv(M)
        #to get the first element as 1
        M[i]=M[i]/M[i][i]
        #to get all below as zeros
        for k in range(i+1,len(M)):
            M[k]=M[k]-M[k][i]*M[i]
    #to operate on the last equation and get its z component 1        
    M[-1]=M[-1]/M[-1][-2]       
    
    #Backward Substitution
    #initializing x for storing solution
    x=np.zeros(len(M))
    for i in range(len(M)-1,-1,-1):
        sum=0
        for j in range(len(M)-1,i,-1):
            sum+=M[i][j]*x[j]
        x[i]=M[i][-1]-sum
    #Returning the final solution
    return x

#Calling the gauss function
x = gaussEl(AugM)

#Printing Solution
for i in range(len(x)):
    print(" {0} = {1} ".format(chr(ord("x")+i),round(x[i],4) ))

#--------THE-END-------------------------------------#