#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:52:38 2020

@author: shirzlotnik
"""

import numpy as np

A  = np.array([[1,2],[3,4],[5,6],[7,8]])
B = np.array([[1,2,3],[4,5,6]])

C = A.dot(B)

print (C)


def FindMult(A,B):
    D = np.zeros((len(A),len(B[0])), dtype = int)
    # go through the rows of A
    for t in range(len(A)):
   # go through the torim of B
       for j in range(len(B[0])):
       # go through the rows of B
           for k in range(len(B)):
               D[t][j] += A[t][k] * B[k][j]
    return D

def FindMinimumSum(A,B):
    r = min(len(A),len(B))
    t = min(len(A[0]),len(B[0]))
    E = np.zeros((r,t),dtype = int)
    for i in range(r):
        for j in range(t):
            E[i][j] += A[i][j]+B[i][j]
    return E

def FindMaximumSum(A,B):
    F = FindMinimumSum(A,B) #the minimum sum
    G = np.zeros((max(len(A),len(B)),max(len(A[0]),len(B[0]))),dtype = int)
    for i in range(F.shape[0]):
        for j in range(F.shape[1]):
            G[i][j] += F[i][j]
    return G

print()
print (FindMult(A,B))
print()
print(FindMinimumSum(A,B))
print()
print(FindMaximumSum(A,B))
