from gekko import GEKKO

#crear el proyecto
m = GEKKO()

#Declarar variables, con los limites superiores e inferiores
x1 = m.Var(lb=0, ub=100) 
x2 = m.Var(lb=0, ub=100) 

#Funcion a optimizar (Maximizar)
m.Maximize(30*x1+50*x2) 

#Ecuaciones
m.Equation(x1+3*x2==200) 
m.Equation(x1+1*x2==100)
m.Equation(3*x1+5*x2==500)

#Resolver
m.solve()

#Imprimir
print ('x1 = ' + str(x1.value[0]))
print ('x2 = ' + str(x2.value[0]))
print ('P = ' + str(30*x1.value[0]+50*x2.value[0]))