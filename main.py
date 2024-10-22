
import math
import os
import random
import re
import sys

contadorNegativo = 0
contadorCero = 0
contadorPositivo = 0

def plusMinus(arr):
    global contadorNegativo
    global contadorCero
    global contadorPositivo
    for i in range(0,n):
        if arr[i] < 0:
            contadorNegativo += 1
            #print(contadorNegativo)
        if arr[i] == 0:
            contadorCero += 1
            #print(contadorCero)
        if arr[i] > 0:
            contadorPositivo += 1
            #print(contadorPositivo)
            
    Positivo = contadorPositivo/n
    Negativo = contadorNegativo/n
    cero = contadorCero/n

    Positivo = f"{Positivo:.6f}"
    Negativo = f"{Negativo:.6f}"
    cero = f"{cero:.6f}"

    print(Positivo)
    print(Negativo)
    print(cero)

if __name__ == '__main__':
    n = int(input())
    entrada = input()
    arr = list(map(int,entrada.split()))

    plusMinus(arr)
    