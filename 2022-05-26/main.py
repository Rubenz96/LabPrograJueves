
from funciones import calcularPromedio
from funciones import calcularPromedioDos

# promedio = calcularPromedio(b=3,a=6)
# print(promedio)
########################################
# promedio = calcularPromedioDos(a=6,b=3)
# print(promedio)

# promedio = calcularPromedioDos(a=6)
# print(promedio)

# promedio = calcularPromedioDos(b=4)
# print(promedio)

# promedio = calcularPromedioDos()
# print(promedio)
############################################

from funciones import sumaCompras

a = 10000
b = 30000
c = 60000

total = sumaCompras(compra_uno = a , compra_dos = b , compra_tres = c)
print(total)

total = sumaCompras(compra_uno = a , compra_dos = b)
print(total)

total = sumaCompras(compra_uno = a , compra_tres = c)
print(total)

total = sumaCompras(compra_uno = a )
print(total)

total = sumaCompras(compra_dos = b , compra_tres = c)
print(total)

total = sumaCompras(compra_dos = b)
print(total)

total = sumaCompras(compra_tres = c)
print(total)

total = sumaCompras()
print(total)



















