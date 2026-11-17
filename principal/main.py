import os
import sqlite3
import string
import datetime
import time
import math
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DB = os.path.join(BASE_DIR, "..", "strings", "users.db")


# LOGIN 

# conexio de la base de dades
def conectar():
    return sqlite3.connect(RUTA_DB)


# funcio per netejar els textos
def limpiar_texto(texto):
    return texto.strip()


# longituds
def validar_longitud(texto, maximo):
    return 0 < len(texto) <= maximo


# caracters
def validar_caracteres(texto):
    permitidos = string.ascii_letters + string.digits + "_"
    return all(c in permitidos for c in texto)


# consultar users.db
def buscar_usuario(cursor, usuario, password):
    cursor.execute(
        "SELECT * FROM usuarios WHERE username = ? AND password = ?",
        (usuario, password)
    )

    return cursor.fetchone()


# login (retorna True si es correcte)
def login():
    usuario = limpiar_texto(input("Usuario: "))
    password = limpiar_texto(input("Contraseña: "))

    if not validar_longitud(usuario, 30):
        print("Usuario massa llarg o vuit")
        return False

    if not validar_longitud(password, 100):
        print("Contraseña massa larga o vuida")
        return False

    if not validar_caracteres(usuario):
        print("Caracteres no permesos")
        return False

    conexion = conectar()
    cursor = conexion.cursor()
    resultado = buscar_usuario(cursor, usuario, password)
    conexion.close()

    if resultado:
        print("Acces correcte!")
        return True

    print("Credenciales incorrectes")
    return False


# MULTI-RELLOTGE 

# mostrar hora actual
def mostrar_hora_actual():
    ara = datetime.datetime.now()

    print("L'hora actual es:", ara.strftime("%H:%M:%S"))
    print("Data d'avui:", ara.strftime("%d/%m/%Y"))

    # de dia o de nit
    if 6 <= ara.hour < 21:
        print("Estat: Es de dia")
    else:
        print("Estat: Es de nit")


# hora mundial
def hora_mundial():
    ara = datetime.datetime.now()

    print("1. Londres (+0h)")
    print("2. Nova York (-5h)")
    print("3. Toquio (+9h)")
    print("4. Sydney (+11h)")
    print("5. Buenos Aires (-3h)")

    opcio = int(input("Tria una opcio: "))

    # sumar o restar hores segons la ciutat
    if opcio == 1:
        canvi = ara + datetime.timedelta(hours=0)
        print("Hora a Londres:", canvi.strftime("%H:%M:%S"))
    elif opcio == 2:
        canvi = ara + datetime.timedelta(hours=-5)
        print("Hora a Nova York:", canvi.strftime("%H:%M:%S"))
    elif opcio == 3:
        canvi = ara + datetime.timedelta(hours=9)
        print("Hora a Toquio:", canvi.strftime("%H:%M:%S"))
    elif opcio == 4:
        canvi = ara + datetime.timedelta(hours=11)
        print("Hora a Sydney:", canvi.strftime("%H:%M:%S"))
    elif opcio == 5:
        canvi = ara + datetime.timedelta(hours=-3)
        print("Hora a Buenos Aires:", canvi.strftime("%H:%M:%S"))
    else:
        print("Opcio incorrecta")


# temporitzador
def temporitzador():
    segons = int(input("Quants segons vols? "))
    print("Comenca el compte enrere...")

    # compte enrere
    for i in range(segons, 0, -1):
        print(i, "segons...")
        time.sleep(1)

    print("Temps exhaurit!")


# cronometre
def cronometre():
    input("Prem Intro per comencar...")
    inici = time.time()

    input("Prem Intro per aturar...")
    fi = time.time()

    # calcular el temps
    temps = round(fi - inici, 2)
    minuts = int(temps // 60)
    segons = round(temps % 60, 2)

    print("Temps transcorregut:", minuts, "minuts i", segons, "segons")


# dies per a cap d'any
def comptar_enrera_dies():
    avui = datetime.date.today()
    cap_d_any = datetime.date(avui.year + 1, 1, 1)

    dies = (cap_d_any - avui).days

    print("Falten", dies, "dies per a Cap d'Any")


# menu del rellotge
def menu_rellotge():
    opcio = 0

    while opcio != 6:
        print("\n--- MULTI-RELLOTGE DIGITAL ---")
        print("1. Hora actual i dia/nit")
        print("2. Hora mundial")
        print("3. Temporitzador")
        print("4. Cronometre")
        print("5. Dies per a Cap d'Any")
        print("6. Sortir")

        opcio = int(input("Tria una opcio (1-6): "))

        if opcio == 1:
            mostrar_hora_actual()
        elif opcio == 2:
            hora_mundial()
        elif opcio == 3:
            temporitzador()
        elif opcio == 4:
            cronometre()
        elif opcio == 5:
            comptar_enrera_dies()
        elif opcio == 6:
            print("Adeu!")
        else:
            print("Opcio incorrecta")


#  CALCULADORA MATEMATICA 

#Calculadora basica
def calculadora_basica(): 
    """Mostra exemples de les funcions matemàtiques natives de python"""
    print("---FUNCIONS NATIVES---")

    #Valor absolut i arrodoniment
    numero = float(input("Introdueix un número: "))

    print("Valor absolut:", abs(numero))
    print("Arrodoniment:", round(numero, 2))

    #Funcions amb una llista
    numeros = input("Introdueix diversos números separats per espais: ")
    numeros = [float(n) for n in numeros.split()]
    if len(numeros) == 0:
        print("Has d'introduir almenys un número")
        return

    print("Número mínim:", min(numeros))
    print("Número màxim:", max(numeros))
    print("Potència del primer número elevat a 2:", pow(numeros[0], 2))
    print("Suma de tots els números:", sum(numeros))


#Modul math
def calculadora_math():
    """Mostra exemples de funcions del mòdul math"""

    print("---MÒDUL MATH---")

    numero = float(input("Introdueix un número: "))

    #Arrels i arrodoniments
    if numero >= 0:
        print("Arrel quadrada:", math.sqrt(numero))
    else:
        print("No es pot calcular l'arrel quadrada d'un número negatiu")

    print("Arrodoniment cap amunt:", math.ceil(numero))
    print("Arrodoniment cap avall:", math.floor(numero))

    #Potències i constants
    print("Potència elevada a 2:", math.pow(numero, 2))
    print("Número PI:", math.pi)

    #Factorial
    factorial = int(input("Introdueix un número enter per calcular el factorial: "))

    if factorial >= 0:
        print("Factorial:", math.factorial(factorial))
    else:
        print("El factorial no pot ser negatiu")

    #Logaritme
    if numero > 0:
        print("Logaritme natural:", math.log(numero))
    else:
        print("El logaritme només accepta números positius")

    #Funcions trigonomètriques
    graus = float(input("Introdueix un angle en graus: "))
    radians = math.radians(graus)

    print("Sinus:", math.sin(radians))
    print("Cosinus:", math.cos(radians))

    if math.isclose(math.cos(radians), 0, abs_tol=1e-10):
        print("La tangent no està definida per aquest angle")
    else:
        print("Tangent:", math.tan(radians))


#Modul random
def calculadora_random():
    """Mostra exemples de funcions del mòdul random"""

    print("---MÒDUL RANDOM---")

    entrada = input("Introdueix diversos números separats per espais: ")

    try:
        numeros = [float(n) for n in entrada.split()]

        if len(numeros) == 0:
            print("Has d'introduir almenys un número")
            return

        #Número aleatori entre dos valors
        minim = float(input("Introdueix el valor mínim: "))
        maxim = float(input("Introdueix el valor màxim: "))

        if minim > maxim:
            print("El valor mínim no pot ser més gran que el màxim")
            return

        if math.ceil(minim) > math.floor(maxim):
            print("No hi ha cap número enter dins d'aquest interval")
            return

        print("Número aleatori:", random.randint(
            math.ceil(minim), math.floor(maxim)
        ))

        #Element aleatori de la llista
        print("Element aleatori de la llista:",
              random.choice(numeros))

        #Barrejar la llista
        random.shuffle(numeros)
        print("Llista barrejada:", numeros)

        #Número decimal aleatori
        print("Número decimal aleatori:", random.random())

        #Seleccionar elements sense repetir
        quantitat = int(input("Quants números aleatoris vols seleccionar? "))

        if 1 <= quantitat <= len(numeros):
            print("Selecció aleatòria:",
                  random.sample(numeros, quantitat))
        else:
            print("La quantitat no és vàlida")

    except ValueError:
        print("Error: introdueix valors vàlids")


#Menu principal
def menu():
    """Mostra el menú principal i permet escollir les calculadores"""

    while True:
        print("===== CALCULADORA MATEMÀTICA =====")
        print("1. Funcions natives de Python")
        print("2. Mòdul math")
        print("3. Mòdul random")
        print("4. Sortir")

        opcio = input("Escull una opció: ")

        if opcio == "1":
            calculadora_basica()
        elif opcio == "2":
            calculadora_math()
        elif opcio == "3":
            calculadora_random()
        elif opcio == "4":
            print("Gràcies per utilitzar la calculadora, adeu!")
            break
        else:
            print("Opció incorrecta, torna-ho a provar")


# ================= MENU GENERAL =================

# menu que uneix tots els programes
def menu_general():
    while True:
        print("\n===== MENU GENERAL =====")
        print("1. Multi-rellotge digital")
        print("2. Calculadora matematica")
        print("0. Sortir")

        opcio = input("Tria una opcio: ")

        if opcio == "1":
            menu_rellotge()
        elif opcio == "2":
            menu()
        elif opcio == "0":
            print("Fins aviat!")
            break
        else:
            print("Opcio incorrecta")


# main
if login():
    menu_general()