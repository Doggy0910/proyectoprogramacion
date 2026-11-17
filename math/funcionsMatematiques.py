
import math
import random

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


if __name__ == "__main__":
    menu()
