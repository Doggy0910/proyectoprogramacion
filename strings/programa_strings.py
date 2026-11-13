import os
import sqlite3
import string

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DB = os.path.join(BASE_DIR, "users.db")


# conexio de la base de dades
def conectar():
    return sqlite3.connect(RUTA_DB)


conexion = conectar()
cursor = conexion.cursor()


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
def buscar_usuario(usuario, password):
    cursor.execute(
        "SELECT * FROM usuarios WHERE username = ? AND password = ?",
        (usuario, password)
    )

    return cursor.fetchone()


# main
usuario = limpiar_texto(input("Usuario: "))
password = limpiar_texto(input("Contraseña: "))


if not validar_longitud(usuario, 30):
    print("Usuario massa llarg o vuit")

elif not validar_longitud(password, 100):
    print("Contraseña massa larga o vuida")

elif not validar_caracteres(usuario):
    print("Caracteres no permesos")

else:
    resultado = buscar_usuario(usuario, password)

    if resultado:
        print("Acces correcte!")
    else:
        print("Credenciales incorrectes")


conexion.close()