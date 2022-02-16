import numpy as np

M = 100
m = [[3.0, 6.0, 1.0, 0.0, -1.0, 0.0, 0.0, 10.0],
     [1, 2, 0, 0, 0, 1, 0, 3],
     [5, 2, 0, 1, 0, 0, -1, 5], 
     [8*M-8, 8*M-3, 0, 0, -1*M, 0, -1*M, 15*M]]

matriz = np.array(m)

#Primera Iteración
matriz[1, :] = matriz[1,:]*(1/matriz[1, 1])#F2/2
matriz[0, :] = (-1*matriz[0, 1])*matriz[1, :]+matriz[0, :]#-6F2+F1
matriz[2, :] = (-1*matriz[2, 1])*matriz[1, :]+matriz[2, :]#-1F2+F3
matriz[3, :] = (-1*matriz[3, 1])*matriz[1, :]+matriz[3, :]

#Segunda Iteración
matriz[2, :] = matriz[2,:]*(1/matriz[2, 0])#F3/4
matriz[0, :] = 1*matriz[0, :]
matriz[1, :] = (-1*matriz[1, 0])*matriz[2, :]+matriz[1, :]#-F3/2+F2
matriz[3, :] = (-1*matriz[3, 0])*matriz[2, :]+matriz[3, :]

resultado = np.round(matriz, decimals = 1)

print(resultado)

