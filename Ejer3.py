import numpy as np

M = 100
m = [[15.0, 10.0, 1.0, 0.0, -1.0, 0.0, 0.0, 30],
     [7, 9, 0, 1, 0, -1, 0, 25],
     [5, 20, 0, 0, 0, 0, 1, 15], 
     [22*M-1, 19*M-3, 0, 0, -M, -M, 0, 55*M]]

matriz = np.array(m)

#Primera Iteración
matriz[0, :] = matriz[0,:]*(1/matriz[0, 0])#F1/15
matriz[1, :] = (-1*matriz[1, 0])*matriz[0, :]+matriz[1, :]#-7F1+F2
matriz[2, :] = (-1*matriz[2, 0])*matriz[0, :]+matriz[2, :]#-5F1+F3
matriz[3, :] = (-1*matriz[3, 0])*matriz[0, :]+matriz[3, :]

#Segunda Iteración
matriz[2, :] = matriz[2,:]*(1/matriz[2, 1])#F3
matriz[1, :] = (-1*matriz[1, 1])*matriz[2, :]+matriz[1, :]#-2F3/3+F2
matriz[0, :] = (-1*matriz[0, 1])*matriz[2, :]+matriz[0, :]#-F3/9+F1
matriz[3, :] = (-1*matriz[3, 1])*matriz[2, :]+matriz[3, :]#-2F3/3+F2

print(matriz[0, :])
print(matriz[1, :])
print(matriz[2, :])
print(matriz[3, :])