# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '102'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda
if (texto_1 > texto_2):
    print("La mayor de ambas palabras es: ", texto_1)
elif(texto_1 == texto_2):
    print("Ambos textos son iguales")
else:
    print("La mayor de ambas palabras es: ",texto_2)
# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
texto_1_int = int(texto_1)
texto_2_int = int(texto_2)
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
if (texto_1_int > texto_2_int):
    print("La mayor de ambas palabras es: ", texto_1)
elif(texto_1_int == texto_2_int):
    print("Ambos textos son iguales")
else:
    print("La mayor de ambas palabras es: ",texto_2_int)
# Imprima en pantalla según corresponda

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
print("Yo creo que es por la ubicacion en la que estan odenados los numeros dentro de python en formato string")