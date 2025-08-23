#Ejercicio 1
#Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola mundo!")

#Ejercicio 2
#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, 
#el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”.
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingresa tu nombre: ")
apellido = input("Ahora ingresa tu apellido: ")
edad = input("Cual es tu edad?: ")
residencia = input("Donde vives?: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Ejercicio 4
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Ingresa el radio del círculo: "))
area = 3.14159265358979 * radio ** 2
perimetro = 2 * 3.14159265358979 * radio

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#Ejercicio 5
#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Ingresar cantidad de segundos: "))
horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas:.2f} horas")

#Ejercicio 6
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingresar un número: "))
i = 1

# Imprimir resultados (usando bucle)
print(f"Tabla de multiplicar del {numero}:")
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1  # Incrementar el contador en 1

#Ejercicio 7
#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingresar el primer número entero (distinto de 0): "))
num2 = int(input("Ingresar el segundo número entero (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

# Imprimir los resultados
print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} menos {num2} es: {resta}")
print(f"La multiplicación de {num1} por {num2} es: {multiplicacion}")
print(f"La división de {num1} entre {num2} es: {division:.2f}")



#Ejercicio 8
#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: peso en Kg / (altura en m) ** 2 

altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kilogramos: "))

# Calculo IMC
imc = peso / (altura ** 2)

# Imprimir resultado
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")


#Ejercicio 9
#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

temp_celsius = float(input("Ingresar la temperatura en grados Celsius: "))


temp_fahrenheit = (temp_celsius * 9/5) + 32

# Imprimir el resultado
print(f"{temp_celsius} grados Celsius equivalen a {temp_fahrenheit:.2f} grados Fahrenheit.")


#Ejercicio 10
#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

promedio = (num1 + num2 + num3) / 3

# Imprimir resultado
print(f"El promedio de los números ingresados es: {promedio:.2f}")

