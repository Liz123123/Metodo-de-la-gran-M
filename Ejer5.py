import numpy as np

M = 100
m = [[1.0, 3.0, 1.0, 0.0, 0.0, 200],
     [1, 1, 0, 1, 0, 100],
     [3, 5, 0, 0, 1, 500], 
     [5*M-30, 9*M-50, 0, 0, 0, 800*M]]

matriz = np.array(m)

#Primera Iteración
matriz[0, :] = matriz[0,:]*(1/matriz[0, 1])#F1/3
matriz[1, :] = (-1*matriz[1, 1])*matriz[0, :]+matriz[1, :]#-F1+F2
matriz[2, :] = (-1*matriz[2, 1])*matriz[0, :]+matriz[2, :]#-5F1+F3
matriz[3, :] = (-1*matriz[3, 1])*matriz[0, :]+matriz[3, :]

#Segunda Iteración
matriz[1, :] = matriz[1,:]*(1/matriz[1, 0])#F3
matriz[2, :] = (-1*matriz[2, 0])*matriz[1, :]+matriz[2, :]#-4F2/3+F3
matriz[0, :] = (-1*matriz[0, 0])*matriz[1, :]+matriz[0, :]#-F2/3+F1
matriz[3, :] = (-1*matriz[3, 0])*matriz[1, :]+matriz[3, :]

print(matriz[0, :])
print(matriz[1, :])
print(matriz[2, :])
print(matriz[3, :])