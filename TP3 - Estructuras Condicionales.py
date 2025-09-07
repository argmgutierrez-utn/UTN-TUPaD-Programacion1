#Ejercicio 1
#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

#Solicita al usuario que ingrese su edad y almacena su respuesta en la variable "edad"
edad = int(input("Ingrese su edad: "))
#Si la variable es mayor a 18 imprime "Es mayor de edad"
if edad > 18:
    print("Es mayor de edad")


#Ejercicio 2
#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. 

#Solicita al usuario que ingrese su nota y almacena su respuesta en la variable "nota"
nota = int(input("Ingrese su nota: "))
#Si la variable es mayor o igual a 6, imprime "Aprobado"
if nota >= 6:
    print("Aprobado")
#Si la variable es menor a 6, imprime "Desaprobado"
else:
    print("Desaprobado")


#Ejercicio 3
#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por pantalla el mensaje "Ha ingresado un número par"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".

#Solicita al usuario que ingrese un número y almacena su respuesta en la variable "numero"
numero = int(input("Ingrese un número: "))

#Repite hasta que el usuario ingrese un número par
while numero % 2 != 0:
    print("Por favor, ingrese un número par")
    numero = int(input("Ingrese un número: "))

#Si el número ingresado es par, imprime "Ha ingresado un número par"
print("Ha ingresado un número par")


#Ejercicio 4
#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

#Solicita al usuario que ingrese su edad y almacena su respuesta en la variable "edad"
edad = int(input("Ingrese su edad: "))

#Verifica si la edad es menor a 12
if edad < 12:
    print("Niño/a")
#Verifica si la edad es mayor o igual a 12 y menor que 18, imprime "Adolecente"
elif edad >= 12 and edad < 18:
    print("Adolescente")
#Verifica si la edad es mayor o igual a 18 y menor que 30, imprime "Adulto joven"
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
#Si no se cumple ninguna de las condiciones anteriores, entonces es mayor o igual a 30, imprime "Adulto"
else:
    print("Adulto/a")


#Ejercicio 5
#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
#Si el usuario ingresa una contraseña de longitud adecuada, imprimir por pantalla el mensaje "Ha ingresado una contraseña correcta"; 
# en caso contrario, imprimir "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

#Solicita al usuario que ingrese una contraseña y la almacena en la variable "contraseña"
contraseña = input("Ingrese una contraseña: ")

#Verifica si la longitud de la contraseña está entre 8 y 14 caracteres, imprime el mensaje de confirmación
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    #Si la longitud no está dentro del rango, imprime el mensaje de advertencia
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Ejercicio 6
#Escribir un programa que tome una lista de 50 números aleatorios entre 1 y 100,
#calcule su moda, mediana y media, y determine si hay sesgo positivo, negativo o no hay sesgo
#Importo el modulo random para generar números aleatorios y las funciones mode, median y mean del modulo statistics para calcular estadísticas

#Importos los módulos necesarios
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
from statistics import mode, median, mean

#Se genera una lista de 50 números aleatorios entre 1 y 100, la consigna no lo pide pero los imprimo en pantalla
print("Numeros aleatorios:", numeros_aleatorios)

#Calcula la media, mediana y moda de la lista
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

#Imprime los valores calculados
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

#Evalúa el tipo de sesgo
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda ")
elif media == mediana and mediana == moda:
    print("Sin sesgo")


#Ejercicio 7
#Escribir un programa que solicite una frase o palabra al usuario.
#Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
#en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

#Solicita una frase o palabra al usuario
texto = input("Ingresá una frase o palabra: ")

#Verifica si el último carácter es una vocal
if texto[-1].lower() in "aeiou":
    texto += "!"  # → añade signo de exclamación si termina en vocal

#Imprime el resultado final
print("Resultado:", texto)


#Ejercicio 8
#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
#Nota: investigar uso de las funciones upper(), lower() y title() de Python.

#Solicita el nombre al usuario
nombre = input("Ingresá tu nombre: ")

#Solicita la opción de formato
print("Seleccioná la opción en la que quieres tu nombre:")
print("1 - MAYÚSCULAS")
print("2 - minúsculas")
print("3 - Primera letra mayúscula")
opcion = input("Ingresá el número de opción (1, 2 o 3): ")

#Transforma el nombre según la opción seleccionada
if opcion == "1":
    resultado = nombre.upper()
elif opcion == "2":
    resultado = nombre.lower()
elif opcion == "3":
    resultado = nombre.title()

#Imprime el resultado
print("Resultado:", resultado)


#Ejercicio 9
#Escribir un programa que pida al usuario la magnitud de un terremoto,
#clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# Menor que 3: "Muy leve" (imperceptible).
# Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)

#Solicita al usuario que ingrese la magnitud del terremoto
magnitud = float(input("Ingresá la magnitud del terremoto: "))

#Clasifica la magnitud según la escala de Richter
if magnitud < 3:
    resultado = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    resultado = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    resultado = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    resultado = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    resultado = "Muy Fuerte (puede causar daños significativos)"
else:
    resultado = "Extremo (puede causar graves daños a gran escala)"

#Imprime el resultado
print("Clasificación:", resultado)


#Ejercicio 10
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (Norte/Sur),qué mes del año es y qué día es.
#El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

#Solicita al usuario el hemisferio, el mes y el día
hemisferio = input("¿Ingresá en qué hemisferio te encontrás? (N/S): ").upper()
mes = int(input("Ingresá el número del mes (1 a 12): "))
día = int(input("Ingresá el día del mes: "))

#Convierte mes y día en un número de referencia para comparar rangos
fecha = (mes, día)

#Determina la estación según el hemisferio y la fecha
if hemisferio == "N":
    if (mes == 12 and día >= 21) or (mes in [1, 2]) or (mes == 3 and día <= 20):  # Invierno: desde el 21 de diciembre hasta el 20 de marzo
        estacion = "Invierno"
    elif (mes == 3 and día >= 21) or (mes in [4, 5]) or (mes == 6 and día <= 20): # Primavera: desde el 21 de marzo hasta el 20 de junio
        estacion = "Primavera"
    elif (mes == 6 and día >= 21) or (mes in [7, 8]) or (mes == 9 and día <= 20): # Verano: desde el 21 de junio hasta el 20 de septiembre
        estacion = "Verano"
    elif (mes == 9 and día >= 21) or (mes in [10, 11]) or (mes == 12 and día <= 20): # Otoño: desde el 21 de septiembre hasta el 20 de diciembre
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and día >= 21) or (mes in [1, 2]) or (mes == 3 and día <= 20): # Verano: desde el 21 de diciembre hasta el 20 de marzo
        estacion = "Verano"
    elif (mes == 3 and día >= 21) or (mes in [4, 5]) or (mes == 6 and día <= 20): # Otoño: desde el 21 de marzo hasta el 20 de junio
        estacion = "Otoño"
    elif (mes == 6 and día >= 21) or (mes in [7, 8]) or (mes == 9 and día <= 20): # Invierno: desde el 21 de junio hasta el 20 de septiembre
        estacion = "Invierno"
    elif (mes == 9 and día >= 21) or (mes in [10, 11]) or (mes == 12 and día <= 20): # Primavera: desde el 21 de septiembre hasta el 20 de diciembre
        estacion = "Primavera"

#Imprime la estación correspondiente
print("Estación actual:", estacion)