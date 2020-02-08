#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 00:59:52 2020

@author: typhoon93

This program gets an input N, and returns an MM logo which has thickness of "N".


Prerequisites:
    2<N<1000
    N is an ODD number

output:

-----*****-----*****-----
----*******---*******----
---*********-*********---
--*****-*********-*****--
-*****---*******---*****-
*****-----*****-----*****

Variables used:

    height - the number of lines in the which make up N
    width - the length of the characters in each line, which we need to generate manually.
    
The program treats the challange like a puzzle.

1. The program first generates one part of M, given  N, height and width (createStrings function).
2. Then we map that into a 2 dimensional matrix list:
    
*******----
-*******---
--*******--
---*******-
----*******
-----******
------*****
-------****

3. We subsequently transform the matrix and create 4 different versions of it:
    matrixStart
    matrixMidReversed
    matrixMid
    matrixEnd.  
4. We create a final matrix out of all parts: matrixFinished and print it.
"""



def createStrings(N, width, height):
    '''
    Takes N, width, height - all integers as input
    returns a list of strings        
    '''
    
    strings = []
    for i in range(1,width):
    
        if i <= N:
            strings.append((i)*'*' + (height-i)*'-')
        else:
            strings.append((i-N)*'-' + (height -(i-N))*'*')
    
    strings.append(height//2*'-' + height//2*'*')
    
    return strings

def initialMatrix(height, width, strings):
    '''
    takes int - height, width, a list of strings'
    generates and fills the matrix with values
    returns the matrix
    '''
    
    matrix = []    
    
    #generate an empty 2D matrix
    for i in range(height):
        matrix.append([])
        for j in range(width):
            matrix[i].append([])
    
    #populate the 2D matrix with the values from strings
    for i in range(width):
        for j in range(height):
            matrix[j][i] = strings[i][j]
            
    return matrix
            


#We begin to transform the matrix and create 4 different parts 
#which we will fit together in the end


def matrixFlip(matrix):
    '''
    takes a 2D list 
    returns the 180 mirror version of it
    '''
    matrixFlipped = []
    
    for i in range(len(matrix)-1,-1,-1):
        matrixFlipped.append(matrix[i])
        
    return matrixFlipped



def matrixMid(matrixStart):
    '''
    takes a 2D list:
        1.makes a deepcopy of the list.
        2.removes x amount of columns from the beginning of the new list
    returns the new list
    '''
    matrixMid = copy.deepcopy(matrixStart)    
    
    x = height//2
    
    for j in range(x):
        for i in range (len(matrixMid)):
            matrixMid[i].pop(0)
    return matrixMid

def matrixEnd(matrixStart):
    '''
    takes a 2D list:
        1.Makes a deepcopy of the matrix
        2.reverses each sublist in the matrix
        3.Pops the last column in the matrix    
    returns the new list
    '''
    
    matrixEnd = copy.deepcopy(matrixStart) 
    for i in range(len(matrixEnd)):
        matrixEnd[i].reverse()
        
    for i in range (len(matrixEnd)):
            matrixEnd[i].pop(0)
     
    return matrixEnd    

def matrixFinished(matrixStart,matrixMidReversed,matrixMid,matrixEnd):
    '''
    takes four 2D lists
    returns a new 2D list which appends all of them together
    '''
    
    matrixFinished =[]
    for i in range(height):
        matrixFinished.append([])
        #M1
        matrixFinished[i].extend(matrixStart[i])
        matrixFinished[i].extend(matrixMidReversed[i])
        matrixFinished[i].extend(matrixMid[i])
        matrixFinished[i].extend(matrixEnd[i])
        #M2
        matrixFinished[i].extend(matrixStart[i])
        matrixFinished[i].extend(matrixMidReversed[i])
        matrixFinished[i].extend(matrixMid[i])
        matrixFinished[i].extend(matrixEnd[i])
    
    return matrixFinished

import copy

while True:
    N = int(input('Please input N, such that 2<N<10 000 and N is an odd number:'))
    if (N>2 and N<10000) and N%2 != 0:
        break
    else:
        print('Please input N that fits the requirements')


height = N+1
width = N + (N+1)//2
    
strings =createStrings(N, width, height)
    
matrix = initialMatrix(height, width, strings)
    
matrixStart = matrixFlip(matrix)
    
matrixMid = matrixMid(matrixStart)
    
matrixMidReversed = matrixFlip(matrixMid)
    
matrixEnd = matrixEnd(matrixStart)        
    
matrixFinished = matrixFinished(matrixStart,matrixMidReversed,matrixMid,matrixEnd)
    
        
    
for line in matrixFinished:
    print(''.join(line))    
