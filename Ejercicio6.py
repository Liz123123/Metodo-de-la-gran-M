from gekko import GEKKO

#crear el proyecto
m = GEKKO()

#Declarar variables, con los limites superiores e inferiores
x1 = m.Var(lb=0, ub=100) 
x2 = m.Var(lb=0, ub=100) 

#Funcion a optimizar (Minimizar)
m.Minimize(15*x1+30*x2) 

#Ecuaciones
m.Equation(5*x1+x2==35) 
m.Equation(8*x1+3*x2==20)
m.Equation(5*x1+9*x2==45)

#Resolver
m.solve()

#Imprimir
print ('x1 = ' + str(x1.value[0]))
print ('x2 = ' + str(x2.value[0]))
print ('P = ' + str(15*x1.value[0]+30*x2.value[0]))