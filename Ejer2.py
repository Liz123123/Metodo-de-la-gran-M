import numpy as np

M = 100
m = [[1.0, 9.0, 1.0, 0.0, 0.0, 8.0],
     [2, 3, 0, 1, 0, 15],
     [5, 2, 0, 0, 1, 5], 
     [3*M-10, 12*M-8, 0, 0, 0, 23*M]]

matriz = np.array(m)

#Primera Iteración
matriz[0, :] = matriz[0,:]*(1/matriz[0, 1])#F1/9
matriz[1, :] = (-1*matriz[1, 1])*matriz[0, :]+matriz[1, :]#-3F1+F2
matriz[2, :] = (-1*matriz[2, 1])*matriz[0, :]+matriz[2, :]#-2F1+F3
matriz[3, :] = (-1*matriz[3, 1])*matriz[0, :]+matriz[3, :]

#Segunda Iteración
matriz[2, :] = matriz[2,:]*(1/matriz[2, 0])#F3
matriz[0, :] = (-1*matriz[0, 0])*matriz[2, :]+matriz[0, :]#-F3/9+F1
matriz[1, :] = (-1*matriz[1, 0])*matriz[2, :]+matriz[1, :]#-2F3/3+F2
matriz[3, :] = (-1*matriz[3, 0])*matriz[2, :]+matriz[3, :]

#Imprimir
print(matriz[0, :])
print(matriz[1, :])
print(matriz[2, :])
print(matriz[3, :])