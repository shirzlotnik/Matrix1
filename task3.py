#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:01:42 2020

@author: shirzlotnik
"""

import numpy as np

big = np.array([[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0]])
fil = np.random.rand(3,3)
#print(fil)
        
        
def FindMeonah(big,fil):
    result = np.zeros((len(big)-2,len(big[0])-2))
    for row in range(len(result)):
        for colm in range(len(result[0])):
            #stam = np.multiply(big[row:row+3,colm:colm+3],fil)
            stam = big[row:row+3,colm:colm+3]*fil
            scalr = ConvertToScalarNumber(stam)
            result[row][colm] += scalr
    return result
    
def ConvertToScalarNumber(arr):
    # multiply 2 matrixes make anotehr matrix that the sum of all og its numbers is the multiply result
    summ = 0
    for row in range(len(arr)):
        for colm in range(len(arr[0])):
            summ += arr[row,colm]
    return summ


def main():
    mat_res = FindMeonah(big,fil)
    print(mat_res)
    while len(mat_res) > len(fil):
        mat_res = FindMeonah(mat_res,fil)
        print(mat_res)
if __name__ == "__main__":
    main()