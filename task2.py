#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:14:52 2020

@author: shirzlotnik
"""

import numpy as np

big = np.array([[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0]])
fil = np.array([[0,1,0],[0,1,0],[0,1,0]])
result = np.zeros((6,6), dtype = int)

def FindMeonah(big,fil,result):
    
    for row in range(len(result)):
        for colm in range(len(result[0])):
            #stam = np.multiply(big[row:row+3,colm:colm+3],fil)
            stam = big[row:row+3,colm:colm+3]*fil
            scalr = ConvertToScalarNumber(stam)
            result[row][colm] += scalr
    print(result)
    
def ConvertToScalarNumber(arr):
    # multiply 2 matrixes make anotehr matrix that the sum of all og its numbers is the multiply result
    summ = 0
    for row in range(len(arr)):
        for colm in range(len(arr[0])):
            summ += arr[row,colm]
    return summ
    

def main():
    FindMeonah(big,fil,result)
    
if __name__ == "__main__":
    main()
    
