from gekko import GEKKO

#crear el proyecto
m = GEKKO()

#Declarar variables, con los limites superiores e inferiores
x1 = m.Var(lb=0, ub=100) 
x2 = m.Var(lb=0, ub=100) 

#Funcion a optimizar (Maximizar)
m.Maximize(x1+3*x2) 

#Ecuaciones
m.Equation(15*x1+10*x2>=30) 
m.Equation(7*x1+9*x2>=25)
m.Equation(5*x1+20*x2<=5)

#Resolver
m.solve()

#Imprimir
print ('x1 = ' + str(x1.value[0]))
print ('x2 = ' + str(x2.value[0]))
print ('P = ' + str(x1.value[0]+3*x2.value[0]))