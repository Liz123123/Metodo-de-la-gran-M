import numpy as np

M = 100
m = [[5.0, 1.0, 1.0, 0.0, 0.0, 35],
     [8, 3, 0, 1, 0, 20],
     [5, 9, 0, 0, 1, 45], 
     [18*M-15, 13*M-30, 0, 0, 0, 100*M]]

matriz = np.array(m)

#Primera Iteración
matriz[1, :] = matriz[1,:]*(1/matriz[1, 0])#F2/8
matriz[0, :] = (-1*matriz[0, 0])*matriz[1, :]+matriz[0, :]#-5F2+F1
matriz[2, :] = (-1*matriz[2, 0])*matriz[1, :]+matriz[2, :]#-5F2+F3
matriz[3, :] = (-1*matriz[3, 0])*matriz[1, :]+matriz[3, :]

#Segunda Iteración
matriz[2, :] = matriz[2,:]*(1/matriz[2, 1])#F3
matriz[1, :] = (-1*matriz[1, 1])*matriz[2, :]+matriz[1, :]#-4F2/3+F3
matriz[0, :] = (-1*matriz[0, 1])*matriz[2, :]+matriz[0, :]#-F2/3+F1
matriz[3, :] = (-1*matriz[3, 1])*matriz[2, :]+matriz[3, :]

print(matriz[0, :])
print(matriz[1, :])
print(matriz[2, :])
print(matriz[3, :])