# -*- coding: utf-8 -*-
"""
Aim: To solve system of linear equation using Jacobi method.
@author: Ashwin Raju Kharat
Roll No: M220590PH
Date: 26 Oct 2022
"""
#importing the numpy library
import numpy as np

#Initial Values 
#A = np.array([[2,1,0],[3,4,-1],[1,-1,2]])
#B = np.array([[8],[16],[10]])

A= np.array([[-4,1,8],[7,3,2],[-1,5,-2]],float)
B=np.array([[22],[19],[3]],float)

#Other questions which cant be solved with Jacobi
#A= np.array([[2,1,1],[3,2,3],[1,4,9]],float)
#B=np.array([[10],[18],[16]],float)

#A=np.array([[2,1,1],[3,2,3],[1,4,9]],float)
#B=np.array([[10],[18],[16]],float)

##------------code-----------##
#Definition for full pivoting
#It takes and the matrix A,B,X and the element indexes to interchange
def fullpiv(A,B,X,i,j,n,m):
    
    #Row operations
    A[[n,i]] = A[[i,n]]
    B[[n,i]] = B[[i,n]]
   
    #Column operations
    A[:,[j,m]] = A[:,[m,j]]
    #doing corresponding row operation on X
    X[[j,m]] = X[[m,j]]
    
    return A,B,X

#To make a Diagonally dominating matrix
def ddm(A,B,X):
    for i in range(len(A)):
        imax,jmax=np.unravel_index(A[i:,i:].argmax(),A[i:,i:].shape)
        A,B,X=fullpiv(A,B,X,imax+i,jmax+i,i,i)
    return A,B,X

#This is to test diagonally dominating matrix
def ddmtest(A):
    for i in range(len(A)):
        sum=0
        for j in range(len(A[i])):
            sum=sum+A[i][j]
        sum=sum-A[i][i]
        
        if sum>A[i][i]:
            #print("it is not a ddm")
            return False
    #print("It is DDM")
    return True

#Compute X using Jacobi
def jacobi(A,B,x):
    condition=True
    while condition:
        for i in range(len(x)):
            sum=0
            for j in range(len(x)):
                if i!=j:    
                    sum=sum+A[i,j]*x[j]
            x_new[i]=(B[i]-sum)/A[i,i]
        esp_sum=0    
        for i in range(len(x)):
            esp_sum=esp_sum+abs(x_new[i]-x[i])
            x=x_new.copy()
            if esp_sum<esp:
                condition=False
            else:
                condition = True
    return x

def gaussSed(A,B,x):
    condition=True
    while condition:
        for i in range(len(x)):
            sum=0
            for j in range(len(x)):
                x=x_new.copy()
                if i!=j:    
                    sum=sum+A[i,j]*x[j]
            x_new[i]=(B[i]-sum)/A[i,i]
        esp_sum=0    
        for i in range(len(x)):
            esp_sum=esp_sum+abs(x_new[i]-x[i])
            x=x_new.copy()
            if esp_sum<esp:
                condition=False
            else:
                condition = True
    return x


#Variable array to commute during full pivoting        
X = np.array([["x1"],["x2"],["x3"]])

x = np.zeros(len(X))
x_new=np.zeros(len(X))
esp=pow(10,-4)

#Printing The Question
AugM=np.array([[-4,1,8,22],[7,3,2,19],[-1,5,-2,3]],float)
for i in range((len(x))):
    print("Equation {4} : {0} X1 + {1} X2 + {2} X3 = {3}".format(AugM[i][0],AugM[i][1],AugM[i][2],AugM[i][3],i+1 ))

#If the given Matrix is not DDM make it DDM
if ddmtest(A)==False:
    print("Not a Trying To Make it DDM")
    A,B,X = ddm(A,B,X)

#Solve using Jacobi only if matrix is DDM
#else cant solve using DDM
if ddmtest(A):
    x=jacobi(A,B,x)
    print("The Solution using Jacobi")
    for i in range(len(X)):
        print("{0} = {1} ".format(X[i][0],round(x[i]),4))
        
else:
    print("Cant be solved using Jacobi method")
    
#--------THE-END-------------------------------------#
