# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:40:38 2022

@author: Rubenz
"""

# valor_uno = (int)(input('Ingrese el valor por favor: '))
# valor_dos = (int)(input('Ingrese el valor por favor: '))
 #----------------Forma sin elif---------------

# if(valor_uno > valor_dos):
#   print('Valor uno es mayor')
# else:
#   if(valor_uno == valor_dos):
#     print('Los valores son iguales')
#   else:
#     print('El valor uno es menor')
    
#----------------Forma con elif---------------
# if(valor_uno > valor_dos):
#   print('Valor uno es mayor')
# elif(valor_uno == valor_dos):
#   print('Los valores son iguales')
# else:
#   print('El valor uno es menor')


# edad = (int)(input('Ingrese la edad de la persona: '))

# if(edad < 10 ):
#   print('La edad es menor a 10')
# elif(edad < 20):
#   print('La edad esta entre 10-20')
# elif(edad < 30):
#   print('La edad esta entre 20-30')
# elif(edad < 40):
#   print('La edad esta entre 30-40')
# else:
#   print('La persona es mayor o igual a 40 años')

#--------------Op Logicos-----------------

edad_1 = (int)(input('Ingrese la edad: '))
edad_2 = (int)(input('Ingrese la edad: '))
edad_3 = (int)(input('Ingrese la edad: '))

# if(edad_1 == edad_2 and edad_3 > edad_1):
#   print('La edad de 1 y 2 son iguales, y 3 es mayor')
# else:
#   print('No se cumple la condicion')


if(edad_1 == edad_2 or edad_3 > edad_1):
  print('La edad de 1 y 2 son iguales, y 3 es mayor')
else:
  print('No se cumple la condicion')