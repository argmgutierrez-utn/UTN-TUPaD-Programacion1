## TP Integrador - Repetitivas, Condicionales y Secuenciales
## Marcelo Gutierrez DNI 28.750.147


# Ejercicio 1 — "Caja del Kiosco"
## Objetivo: Simular una compra con validaciones y cálculo de total.


# =============================================================
# BLOQUE 1: Pedir y validar el nombre del cliente
# =============================================================

# Pedimos el nombre y con .strip() eliminamos espacios sobrantes al inicio y al final
nombre = input("Cliente: ").strip()

 # Validamos que no esté vacío y que contenga solo letras
while not nombre.isalpha():
    print("Error: solo letras, sin números ni espacios.")
    nombre = input("Cliente: ").strip()


# =============================================================
# BLOQUE 2: Pedir y validar la cantidad de productos
# =============================================================

cantidad = input("Cantidad de productos: ").strip()

# Validamos que sea un número entero positivo mayor a 0
while not cantidad.isdigit() or cantidad == "0":
    print("Error: ingresá un número entero positivo.")
    cantidad = input("Cantidad de productos: ").strip()

# Recién acá, cuando ya sabemos que es válido, lo convertimos a entero
cantidad = int(cantidad)


# =============================================================
# BLOQUE 3: Recorrer cada producto y acumular totales
# =============================================================

# Inicializamos acumuladores. Estas variables arrancan en 0 y van sumando el precio de cada producto
total_sin_descuento = 0
total_con_descuento = 0

# Recorremos cada producto desde 1 hasta la cantidad ingresada (inclusive)
for i in range(1, cantidad + 1):

    # Pedimos el precio del producto y validamos que sea un número entero
    precio = input(f"Producto {i} - Precio: ").strip()

    while not precio.isdigit():
        print("Error: ingresá un número entero.")
        precio = input(f"Producto {i} - Precio: ").strip()

    # Convertimos a entero una vez validado
    precio = int(precio)

    # Pedimos si tiene descuento y validamos que sea "s" o "n" (sí o no)
    descuento = input("Descuento (S/N): ").strip().lower()

    while descuento != "s" and descuento != "n":
        print("Error: ingresá S o N.")
        descuento = input("Descuento (S/N): ").strip().lower()

    # Sumamos el precio al total sin descuentos
    total_sin_descuento = total_sin_descuento + precio

    # Si tiene descuento, aplicamos 10% de descuento al precio
    if descuento == "s":
        precio_final = precio * 0.90
    else:
        # Sin descuento, el precio final es el mismo que el original
        precio_final = precio

    # Sumamos el precio final al total con descuentos
    total_con_descuento = total_con_descuento + precio_final


# =============================================================
# BLOQUE 4: Calcular y mostrar los resultados finales
# =============================================================


# Calculamos ahorro y promedio
ahorro = total_sin_descuento - total_con_descuento

promedio = total_con_descuento / cantidad

# Mostramos los resultados
print(f"\nTotal sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


# Ejercicio 2 — "Acceso al Campus y Menú Seguro"
## Objetivo: Login con intentos limitados + menú de acciones con validación estricta.


# =============================================================
# BLOQUE 1: Definir credenciales y variables de control
# =============================================================


# Definimos credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"

# Inicializamos variables de control
acceso_concedido = False
intentos = 0


# =============================================================
# BLOQUE 2: Login con máximo 3 intentos
# =============================================================


# Permitimos hasta 3 intentos para ingresar las credenciales correctas
while intentos < 3 and not acceso_concedido:

    # Sumamos 1 al contador antes de mostrar el mensaje
    intentos = intentos + 1
    print(f"Intento {intentos}/3 - Usuario: ", end="")

    # Pedimos usuario y clave
    usuario = input("").strip()
    clave = input("Clave: ").strip()

    # Verificamos si ambas credenciales son correctas al mismo tiempo
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso_concedido = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")


# =============================================================
# BLOQUE 3: Resultado del login
# =============================================================

# Si falla 3 veces, la cuenta queda bloqueada
if not acceso_concedido:
    print("Cuenta bloqueada.")

else:
    # La clave puede cambiar durante la sesión, la guardamos en una variable mutable
    clave_actual = clave_correcta
    opcion = ""

    # =============================================================
    # BLOQUE 4: Menú principal (se repite hasta que el usuario elija salir)
    # =============================================================

    # Menú repetitivo hasta elegir salir
    while opcion != "4":

        # Mostramos las opciones del menú
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ").strip()

        # Validamos que la opción sea un número entre 1 y 4
        while not opcion.isdigit() or opcion not in ("1", "2", "3", "4"):
            if not opcion.isdigit():
                print("Error: ingrese un número válido.")
            else:
                print("Error: opción fuera de rango.")
            opcion = input("Opción: ").strip()

        # --- Opción 1: Ver estado de inscripción ---
        if opcion == "1":
            print("Inscripto")

        # --- Opción 2: Cambiar clave ---
        elif opcion == "2":

            # Pedimos la nueva clave y validamos longitud mínima de 6 caracteres
            # len() cuenta la cantidad de caracteres de un string
            nueva_clave = input("Nueva clave: ").strip()
            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ").strip()

            # Pedimos confirmación y verificamos que ambas claves coincidan
            confirmacion = input("Confirmá la clave: ").strip()
            while confirmacion != nueva_clave:
                print("Error: las claves no coinciden. Intentá de nuevo.")
                confirmacion = input("Confirmá la clave: ").strip()

            # Actualizamos la clave actual con la nueva
            clave_actual = nueva_clave
            print("Clave actualizada correctamente.")

        # --- Opción 3: Mostrar mensaje motivacional ---
        elif opcion == "3":
            print("¡El esfuerzo de hoy es el éxito de mañana. Vamos que se puede!!!")

        # --- Opción 4: Salir del sistema ---
        elif opcion == "4":
            print("Sesión cerrada. ¡Hasta pronto!")

           


# Ejercicio 3 — "Agenda de Turnos con Nombres (sin listas)"
## Objetivo: Gestionar turnos de dos días usando únicamente variables individuales.
## Restricción: No se pueden usar listas, diccionarios, sets ni tuplas.


# =============================================================
# BLOQUE 1: Pedir y validar el nombre del operador
# =============================================================

operador = input("Nombre del operador: ").strip()
while not operador.isalpha():
    print("Error: solo letras.")
    operador = input("Nombre del operador: ").strip()

print(f"\nBienvenido/a, {operador}. Sistema de agenda iniciado.")


# =============================================================
# BLOQUE 2: Inicializamos los turnos como variables individuales vacías
# =============================================================

# Lunes tiene 4 cupos y Martes tiene 3 cupos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


# =============================================================
# BLOQUE 3: Menú principal (se repite hasta elegir cerrar)
# =============================================================

opcion = ""

while opcion != "5":

    print("\n1) Reservar  2) Cancelar  3) Ver agenda  4) Resumen  5) Cerrar")
    opcion = input("Opción: ").strip()

    # Validamos que la opción sea un número entre 1 y 5
    while not opcion.isdigit() or opcion not in ("1", "2", "3", "4", "5"):
        print("Error: opción inválida. Ingresá un número del 1 al 5.")
        opcion = input("Opción: ").strip()


    # -------------------------------------------------------
    # Opción 1: Reservar turno
    # -------------------------------------------------------
    if opcion == "1":

        # Elegimos el día
        dia = input("Día (1=Lunes, 2=Martes): ").strip()
        while dia not in ("1", "2"):
            print("Error: ingresá 1 para Lunes o 2 para Martes.")
            dia = input("Día (1=Lunes, 2=Martes): ").strip()

        # Pedimos y validamos el nombre del paciente
        paciente = input("Nombre del paciente: ").strip()
        while not paciente.isalpha():
            print("Error: solo letras.")
            paciente = input("Nombre del paciente: ").strip()

        if dia == "1":
            # Verificamos que el paciente no tenga un turno ya reservado en Lunes
            # Comparamos el nombre contra cada variable de turno
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print(f"Error: {paciente} ya tiene turno el Lunes.")

            # Guardamos en el primer espacio libre que encontremos
            elif lunes1 == "":
                lunes1 = paciente
                print(f"Turno reservado: {paciente} → Lunes Turno 1")
            elif lunes2 == "":
                lunes2 = paciente
                print(f"Turno reservado: {paciente} → Lunes Turno 2")
            elif lunes3 == "":
                lunes3 = paciente
                print(f"Turno reservado: {paciente} → Lunes Turno 3")
            elif lunes4 == "":
                lunes4 = paciente
                print(f"Turno reservado: {paciente} → Lunes Turno 4")
            else:
                print("No hay cupos disponibles el Lunes.")

        else:  # dia == "2" → Martes
            # Verificamos que el paciente no tenga un turno ya reservado en Martes
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print(f"Error: {paciente} ya tiene turno el Martes.")

            elif martes1 == "":
                martes1 = paciente
                print(f"Turno reservado: {paciente} → Martes Turno 1")
            elif martes2 == "":
                martes2 = paciente
                print(f"Turno reservado: {paciente} → Martes Turno 2")
            elif martes3 == "":
                martes3 = paciente
                print(f"Turno reservado: {paciente} → Martes Turno 3")
            else:
                print("No hay cupos disponibles el Martes.")


    # -------------------------------------------------------
    # Opción 2: Cancelar turno
    # -------------------------------------------------------
    elif opcion == "2":

        dia = input("Día (1=Lunes, 2=Martes): ").strip()
        while dia not in ("1", "2"):
            print("Error: ingresá 1 o 2.")
            dia = input("Día (1=Lunes, 2=Martes): ").strip()

        paciente = input("Nombre del paciente a cancelar: ").strip()
        while not paciente.isalpha():
            print("Error: solo letras.")
            paciente = input("Nombre del paciente a cancelar: ").strip()

        # Variable booleana para saber si encontramos el turno
        cancelado = False

        if dia == "1":
            # Buscamos el nombre en cada variable de Lunes y lo dejamos vacío si lo encontramos
            if lunes1 == paciente:
                lunes1 = ""
                cancelado = True
            elif lunes2 == paciente:
                lunes2 = ""
                cancelado = True
            elif lunes3 == paciente:
                lunes3 = ""
                cancelado = True
            elif lunes4 == paciente:
                lunes4 = ""
                cancelado = True

        else:  # Martes
            if martes1 == paciente:
                martes1 = ""
                cancelado = True
            elif martes2 == paciente:
                martes2 = ""
                cancelado = True
            elif martes3 == paciente:
                martes3 = ""
                cancelado = True

        # Informamos el resultado de la operación
        if cancelado:
            print(f"Turno de {paciente} cancelado exitosamente.")
        else:
            print(f"No se encontró turno para {paciente} en ese día.")


    # -------------------------------------------------------
    # Opción 3: Ver agenda del día
    # -------------------------------------------------------
    elif opcion == "3":

        dia = input("Día (1=Lunes, 2=Martes): ").strip()
        while dia not in ("1", "2"):
            print("Error: ingresá 1 o 2.")
            dia = input("Día (1=Lunes, 2=Martes): ").strip()

        if dia == "1":
            print("\n--- Agenda del Lunes ---")
            # Para cada turno: si tiene nombre lo mostramos, sino indicamos "(libre)"
            if lunes1 != "":
                print(f"Turno 1: {lunes1}")
            else:
                print("Turno 1: (libre)")

            if lunes2 != "":
                print(f"Turno 2: {lunes2}")
            else:
                print("Turno 2: (libre)")

            if lunes3 != "":
                print(f"Turno 3: {lunes3}")
            else:
                print("Turno 3: (libre)")

            if lunes4 != "":
                print(f"Turno 4: {lunes4}")
            else:
                print("Turno 4: (libre)")

        else:  # Martes
            print("\n--- Agenda del Martes ---")
            if martes1 != "":
                print(f"Turno 1: {martes1}")
            else:
                print("Turno 1: (libre)")

            if martes2 != "":
                print(f"Turno 2: {martes2}")
            else:
                print("Turno 2: (libre)")

            if martes3 != "":
                print(f"Turno 3: {martes3}")
            else:
                print("Turno 3: (libre)")


    # -------------------------------------------------------
    # Opción 4: Resumen general
    # -------------------------------------------------------
    elif opcion == "4":

        # Contamos los turnos ocupados de Lunes
        # (comparamos cada variable con "" para saber si está ocupada)
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes = ocupados_lunes + 1
        if lunes2 != "":
            ocupados_lunes = ocupados_lunes + 1
        if lunes3 != "":
            ocupados_lunes = ocupados_lunes + 1
        if lunes4 != "":
            ocupados_lunes = ocupados_lunes + 1

        # Contamos los turnos ocupados de Martes
        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes = ocupados_martes + 1
        if martes2 != "":
            ocupados_martes = ocupados_martes + 1
        if martes3 != "":
            ocupados_martes = ocupados_martes + 1

        # Calculamos los disponibles restando de los cupos totales
        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print(f"\n--- Resumen General ---")
        print(f"Lunes  → Ocupados: {ocupados_lunes} | Disponibles: {disponibles_lunes}")
        print(f"Martes → Ocupados: {ocupados_martes} | Disponibles: {disponibles_martes}")

        # Determinamos el día con más turnos ocupados
        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos ocupados: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos ocupados: Martes")
        else:
            print("Empate: ambos días tienen la misma cantidad de turnos ocupados.")


    # -------------------------------------------------------
    # Opción 5: Cerrar sistema
    # -------------------------------------------------------
    elif opcion == "5":
        print(f"\nSistema cerrado. Hasta luego, {operador}.")





# Ejercicio 4 — "Escape Room: La Bóveda"
## Objetivo: Juego de escape con energía, tiempo y cerraduras limitadas.
## Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.


# =============================================================
# BLOQUE 1: Variables iniciales (NO se piden al usuario)
# =============================================================

energia = 100               # Energía disponible del agente
tiempo = 12                 # Tiempo restante para abrir la bóveda
cerraduras_abiertas = 0     # Contador de cerraduras abiertas (objetivo: llegar a 3)
alarma = False              # Estado de la alarma (False = apagada, True = activa)
codigo_parcial = ""         # Código que se va construyendo al hackear el panel

forzar_seguidas = 0         # Variable propia para la regla anti-spam


# =============================================================
# BLOQUE 2: Pedir y validar el nombre del agente
# =============================================================

print("=== ESCAPE ROOM: LA BÓVEDA ===")
agente = input("Nombre del agente: ").strip()
while not agente.isalpha():
    print("Error: solo letras.")
    agente = input("Nombre del agente: ").strip()

print(f"\nBienvenido, Agente {agente}. Comienza la mision. La bóveda tiene 3 cerraduras. ¡Buena suerte!")


# =============================================================
# BLOQUE 3: Ciclo principal del juego
# =============================================================

# Variable booleana que controla si el juego sigue activo
juego_activo = True

# El juego continúa mientras haya energía, tiempo y no esté bloqueado por la alarma, y no se hayan abierto las 3 cerraduras
while juego_activo and energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    # --- Verificar regla de bloqueo por alarma ---
    # Si la alarma está activa Y el tiempo restante es 3 o menos → DERROTA por bloqueo
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\n⛔ SISTEMA BLOQUEADO: alarma activa con tiempo crítico. Acceso denegado.")
        juego_activo = False
        break  # Salimos del ciclo principal porque el juego terminó por bloqueo

    # --- Mostramos el estado actual del juego ---
    print("--- ESTADO ACTUAL ---")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {'ON' if alarma else 'OFF'}")
    print(f"Código parcial: {codigo_parcial}")

    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    # Pedimos y validamos la acción del jugador
    opcion = input("Acción: ").strip()
    while not opcion.isdigit() or opcion not in ("1", "2", "3"):
        print("Error: ingresá 1, 2 o 3.")
        opcion = input("Acción: ").strip()


    # -------------------------------------------------------
    # Opción 1: Forzar cerradura
    # Costo: -20 energía, -2 tiempo
    # -------------------------------------------------------
    if opcion == "1":

        # Descontamos el costo siempre, independientemente del resultado
        energia = energia - 20
        tiempo = tiempo - 2

        # Sumamos 1 al contador de forzar seguidas
        forzar_seguidas = forzar_seguidas + 1

        # --- Regla anti-spam ---
        # Si eligió Forzar 3 veces SEGUIDAS, la cerradura se traba y se activa la alarma
        if forzar_seguidas >= 3:
            print("¡La cerradura se trabó de tanto forzarla! ALARMA ACTIVADA.")
            alarma = True
            # No se abre ninguna cerradura en este caso

        # --- Riesgo de alarma por energía baja ---
        # Si la energía cayó por debajo de 40, hay riesgo adicional
        elif energia < 40:
            print("⚠ Energía crítica: riesgo de activar la alarma.")
            numero_riesgo = input("Elegí un número del 1 al 3: ").strip()
            # Validamos que sea un número entre 1 y 3
            while not numero_riesgo.isdigit() or numero_riesgo not in ("1", "2", "3"):
                print("Error: ingresá 1, 2 o 3.")
                numero_riesgo = input("Elegí un número del 1 al 3: ").strip()

            # Si eligió el 3, mala suerte: se activa la alarma
            if numero_riesgo == "3":
                alarma = True
                print("¡Elegiste el número fatal! Alarma activada.")
            else:
                # Si no eligió el 3, la cerradura se abre normalmente
                cerraduras_abiertas = cerraduras_abiertas + 1
                print(f"¡Cerradura {cerraduras_abiertas} abierta!")

        else:
            # Sin riesgos: abrimos la cerradura sin problema
            cerraduras_abiertas = cerraduras_abiertas + 1
            print(f"¡Cerradura {cerraduras_abiertas} abierta!")


    # -------------------------------------------------------
    # Opción 2: Hackear panel
    # Costo: -10 energía, -3 tiempo
    # -------------------------------------------------------
    elif opcion == "2":

        energia = energia - 10
        tiempo = tiempo - 3

        # Al elegir hackear, se corta la racha de "forzar seguidas"
        forzar_seguidas = 0

        print("Iniciando secuencia de hackeo...")

        # Simulamos 4 pasos de hackeo con un for
        # En cada paso agregamos una letra "A" al código parcial
        for paso in range(1, 5):
            codigo_parcial = codigo_parcial + "A"
            print(f"  Paso {paso}/4 → Código parcial: {codigo_parcial}")

        # Si el código acumulado tiene 8 o más letras Y todavía faltan cerraduras,
        # se abre automáticamente una cerradura
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas = cerraduras_abiertas + 1
            print(f"¡Código completo! Cerradura {cerraduras_abiertas} abierta automáticamente.")


    # -------------------------------------------------------
    # Opción 3: Descansar
    # Costo: +15 energía (máximo 100), -1 tiempo
    # Si la alarma está activa: cuesta 10 energía extra
    # -------------------------------------------------------
    elif opcion == "3":

        tiempo = tiempo - 1

        # Al elegir descansar, se corta la racha de "forzar seguidas"
        forzar_seguidas = 0

        if alarma:
            # La alarma consume energía extra mientras descansás
            energia = energia - 10
            print(f"Alarma activa: perdiste 10 de energía extra. Energía: {energia}")
        else:
            # Sin alarma, recuperamos 15 de energía
            energia = energia + 15

            # La energía no puede superar el máximo de 100
            if energia > 100:
                energia = 100

            print(f"Descansaste y recuperaste energía. Energía actual: {energia}")


# =============================================================
# BLOQUE 4: Condiciones de fin del juego
# =============================================================

# Victoria: se abrieron las 3 cerraduras
if cerraduras_abiertas == 3:
    print(f"\n🏆 ¡VICTORIA! Agente {agente}, abriste la bóveda exitosamente.")

# Derrota por bloqueo de alarma (juego_activo se puso en False dentro del while)
elif not juego_activo:
    print(f"\n💀 DERROTA (bloqueo). La alarma selló la bóveda permanentemente.")

# Derrota por falta de energía
elif energia <= 0:
    print(f"\n💀 DERROTA. Sin energía para continuar.")

# Derrota por falta de tiempo
elif tiempo <= 0:
    print(f"\n💀 DERROTA. Se acabó el tiempo.")




# Ejercicio 5 — "Escape Room: La Arena del Gladiador"
## Objetivo: Simulador de batalla por turnos. El jugador (Gladiador) lucha contra un enemigo controlado por la computadora. Ganás si reducís la vida del enemigo 0 antes de que él lo haga con vos.


# =============================================================
# BLOQUE 1: Configuración del personaje
# =============================================================

print("--- BIENVENIDO A LA ARENA ---")

# Pedimos y validamos el nombre del gladiador (solo letras)
nombre_gladiador = input("Nombre del Gladiador: ").strip()
while not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_gladiador = input("Nombre del Gladiador: ").strip()


# =============================================================
# BLOQUE 2: Inicializamos variables pedidas por la consigna
# =============================================================

vida_jugador = 100          # int: puntos de vida del gladiador
vida_enemigo = 100          # int: puntos de vida del enemigo
pociones = 3                # int: cantidad de pociones de vida disponibles
danio_base = 15             # int: daño base del ataque pesado del jugador
danio_enemigo = 12          # int: daño base del enemigo por turno
turno_gladiador = True      # bool: indica si es el turno del jugador (siempre empieza él)

print(f"\n=== INICIO DEL COMBATE ===")


# =============================================================
# BLOQUE 3: Ciclo de combate
# =============================================================

# El combate sigue mientras ambos tengan vida por encima de 0
while vida_jugador > 0 and vida_enemigo > 0:

    # --- Mostramos el estado actual del turno ---
    print(f"\n{nombre_gladiador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    # Pedimos y validamos la opción del menú
    opcion = input("Opción: ").strip()
    while not opcion.isdigit() or opcion not in ("1", "2", "3"):
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
        else:
            print("Error: Ingrese 1, 2 o 3.")
        opcion = input("Opción: ").strip()


    # -------------------------------------------------------
    # Acción A: Ataque Pesado (Opción 1)
    # -------------------------------------------------------
    if opcion == "1":

        # Si la vida del enemigo es menor a 20, el golpe es crítico
        if vida_enemigo < 20:
            danio_final = danio_base * 1.5  
            print(f"¡GOLPE CRÍTICO! ¡Atacaste al enemigo por {danio_final} puntos de daño!")
        else:
            danio_final = danio_base        # int: daño normal
            print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

        # Usamos int() para convertir el resultado a entero al restar la vida
        vida_enemigo = vida_enemigo - int(danio_final)


    # -------------------------------------------------------
    # Acción B: Ráfaga Veloz (Opción 2)
    # -------------------------------------------------------
    elif opcion == "2":

        print(f">> ¡Iniciás una ráfaga de golpes!")

        # El for se repite 3 veces (range(3) genera 0, 1, 2 → 3 repeticiones)
        for golpe in range(3):
            vida_enemigo = vida_enemigo - 5
            print("> Golpe conectado por 5 de daño")


    # -------------------------------------------------------
    # Acción C: Curar (Opción 3)
    # -------------------------------------------------------
    elif opcion == "3":

        # Solo podemos curar si tenemos pociones disponibles
        if pociones > 0:
            vida_jugador = vida_jugador + 30
            pociones = pociones - 1

            # La vida no puede superar el máximo de 100
            if vida_jugador > 100:
                vida_jugador = 100

            print(f"Usaste una poción. Vida: {vida_jugador} | Pociones restantes: {pociones}")
        else:
            # Sin pociones: mostramos el mensaje y el turno se pierde igual
            print("¡No quedan pociones!")


    # -------------------------------------------------------
    # Turno del enemigo
    # El enemigo ataca SIEMPRE después de la acción del jugador, pero solo si todavía tiene vida (podría haber muerto en el turno del jugador)
    # -------------------------------------------------------
    if vida_enemigo > 0:
        vida_jugador = vida_jugador - danio_enemigo
        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

    print("=== NUEVO TURNO ===")


# =============================================================
# BLOQUE 4: Fin del juego
# =============================================================

# Cuando el while termina, evaluamos quién ganó
if vida_jugador > 0:
    # El jugador sigue con vida → ganó
    print(f"\n¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    # El jugador llegó a 0 o menos → perdió
    print(f"\nDERROTA. {nombre_gladiador} ha caído en combate.")