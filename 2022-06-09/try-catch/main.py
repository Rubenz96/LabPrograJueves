
# try:
#     print(x)
# except:
#     print('Error en la ejecución')
######################################################

n_datos = (int)(input('Ingrese el numero de datos: '))
sumador = 0
cont = 0

while(cont < n_datos):
    try:
        dato = (int)(input('Ingrese el numero: '))
        sumador = sumador + dato
        cont = cont + 1
    except:
        print('Intente nuevamente')
print('------------------------------')
print(sumador)









