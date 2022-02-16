from gekko import GEKKO

#crear el proyecto
m = GEKKO()

#Declarar variables, con los limites superiores e inferiores
x1 = m.Var(lb=0, ub=100) 
x2 = m.Var(lb=0, ub=100) 

#Funcion a optimizar (Maximizar)
m.Maximize(2*x1+4*x2) 

#Ecuaciones
m.Equation(10*x1+2*x2>=3) 
m.Equation(4*x1+4*x2<=10)
m.Equation(7*x1+4*x2==5)

#Resolver
m.solve()

#Imprimir
print ('x1 = ' + str(x1.value[0]))
print ('x2 = ' + str(x2.value[0]))
print ('P = ' + str(2*x1.value[0]+4*x2.value[0]))