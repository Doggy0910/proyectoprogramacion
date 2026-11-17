import datetime
import time


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


# main
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