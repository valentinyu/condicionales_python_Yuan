# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
from itertools import tee


texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if (texto_1 > texto_2):
    print("La mayor de ambas palabras es: ", texto_1)
elif(texto_1==texto_2):
    print("Ambos textos son iguales")
else:
    print("La mayor de ambas palabras es: ",texto_2)
# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1) > len(texto_2):
    print("La palabra con mayor cantidad de caracteres es: ",texto_1,"  ", len(texto_1))
elif len(texto_1) == len(texto_2):
     print("AMBAS PALABRAS TIENEN: ", len(texto_1)," CARACTERES")
else:
    print("La palabra con mayor cantidad de caracteres es: ",texto_2,"  ", len(texto_2))
# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
if(texto_1[0] > texto_2[0]):
    print("La primer letra de la primer palabra: ",texto_1[0], " es mayor a la primera de la segunda: ",texto_2[0])
else: print("No se cumple la condicion")

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if(copia_texto_1 == texto_1):
    print("La copia es igual al texto 1 ")
else: print("No son iguales")
# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if(copia_texto_1 != texto_2):
    print("La compia del texto 1 es distinta a la palabra 2 ")