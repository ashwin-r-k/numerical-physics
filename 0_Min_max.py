#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aim: Find the minimum of the elemnt from the list
@author: Ashwin Raju Kharat
Roll No: M220590PH
Date: 7 Sep 2022
"""

import random
#Importing the Random Library

list = random.sample(range(100,1000),10)
#Using range to creat a list of numbers
#And randomly selecting 50 numbers from list.
#Alternatively we can also use preedefined list like 
#list = [52,36,-4,36,85665,85,36,8]


print("The Randomly genereted list is \n",list)

#initilizing Min Max
min=list[0]
max=list[0]

#Runing a for loop for a Binary comparision to find min and max.
for i in list:
    if min>=i:
        min=i
    elif max<=i:
        max =i

#Printing the result.
print("\nFrom the Given list the minimum is {0}".format(min))
print("\nFrom the Given list  the maximum is {0}".format(max))

#--------THE-END-------------------------------------#