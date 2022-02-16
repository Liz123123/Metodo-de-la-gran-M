from gekko import GEKKO

#crear el proyecto
m = GEKKO()

#Declarar variables, con los limites superiores e inferiores
x1 = m.Var(lb=0, ub=100) 
x2 = m.Var(lb=0, ub=100) 

#Funcion a optimizar (Minimizar)
m.Minimize(8*x1+3*x2) 

#Ecuaciones
m.Equation(3*x1+6*x2>=10) 
m.Equation(x1+2*x2<=3)
m.Equation(5*x1+2*x2>=5)

#Resolver
m.solve()

#Imprimir
print ('x1 = ' + str(x1.value[0]))
print ('x2 = ' + str(x2.value[0]))
print ('P = ' + str(8*x1.value[0]+3*x2.value[0]))