# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda
if (numero_1 > numero_2):
    print("El mayor de ambos números es: ", numero_1)
elif(numero_1==numero_2):
    print("Ambos numeros son iguales ")
else:
    print("El mayor de ambos números es: ",numero_2)
# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
if(numero_1 > 0):
    print("El primer número ingresado es positivo")
elif(numero_1 < 0):
    print("El primer número ingresado es negativo")
else:
    print("El primer numero ingresado es un 0")
# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición
if(0 < numero_1 < 100):
    print("El primer numero ingresado es mayor a 0 y menor a 100")
else:
    print("El primer numero no cumple con la condicion")
# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición
if(numero_1 < 10 or numero_2 > -2):
    print("Se cumple la condicion" , numero_1,"\n",numero_2)
else: 
    print("No se cumple la condicion")