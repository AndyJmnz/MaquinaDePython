
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def quicksort(arr):
    if(len(arr) < 1):
        return arr
    
    pivote = arr[0]
    izquierda = []
    derecha = []
    
    for i in range(1, len(arr)):
        izquierda.append(arr[i]) if pivote > arr[i] else derecha.append(arr[i])
    return quicksort(izquierda) + [pivote] + quicksort(derecha) 
    
        
def miniMaxSum(arr):
    largo = len(arr)
    largo = largo - 1
    sumMin = 0
    sumMax = 0 
    for i in range(0, largo):
        sumMin = sumMin + arr[i]
    
    for j in range(1, len(arr)):
        sumMax = sumMax + arr[j]
    print(sumMin, sumMax)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    resultado = quicksort(arr)
    miniMaxSum(resultado)
