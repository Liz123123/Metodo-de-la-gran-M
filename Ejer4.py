import numpy as np

M = 100
m = [[10.0, 2.0, 1.0, 0.0, -1.0, 0.0, 3.0],
     [4, 4, 0, 0, 0, 1, 10],
     [7, 4, 0, 1, 0, 0, 5], 
     [17*M-2, 6*M-4, 0, 0, M, 0, 23*M]]

matriz = np.array(m)

#Primera Iteración
matriz[0, :] = matriz[0,:]*(1/matriz[0, 0])#F1/10
matriz[1, :] = (-1*matriz[1, 0])*matriz[0, :]+matriz[1, :]#-3F1+F2
matriz[2, :] = (-1*matriz[2, 0])*matriz[0, :]+matriz[2, :]#-2F1+F3
matriz[3, :] = (-1*matriz[3, 0])*matriz[0, :]+matriz[3, :]

#Segunda Iteración
matriz[2, :] = matriz[2,:]*(1/matriz[2, 1])#5F3/13
matriz[1, :] = (-1*matriz[1, 1])*matriz[2, :]+matriz[1, :]#-2F3/3+F2
matriz[0, :] = (-1*matriz[0, 1])*matriz[2, :]+matriz[0, :]#-F3/9+F1

print(matriz[0, :])
print(matriz[1, :])
print(matriz[2, :])
print(matriz[3, :])