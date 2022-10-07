import time
import os
import pandas as pd

def ERROR(): #animacion de error
    for i in range(0,3):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("ERROR")
                time.sleep(0.3)
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(0.3)

#menu ingresos
def mostrar_ingresos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("                       ***INGRESOS***")
    df = pd.read_csv("income.csv")
    if df.shape[0] == 0:
        print("marco de datos vacio.")
    else:
        print(df)
    print("")
    print("R- Regresar")
    seleccion = input().upper()
    if seleccion == "R":
        menu()
    else:
        ERROR()
        mostrar_ingresos()

#menu gastos
def mostrar_gastos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("                       ***GASTOS***")
    df = pd.read_csv("Gastos.csv")
    if df.shape[0] == 0:
        print("marco de datos vacio.")
    else:
        print(df)
    print("")
    print("R- Regresar")
    seleccion = input().upper()
    if seleccion == "R":
        menu()
    else:
        ERROR()
        mostrar_gastos()

def procesar_seleccion(seleccion):
    if seleccion == "1":
        mostrar_gastos()
    elif seleccion == "2":
        mostrar_ingresos()
    else:
        ERROR()
        menu()
        
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1- Gastos")
    print("2- Ingresos")
    seleccion = str(input())
    procesar_seleccion(seleccion)

#opening
def intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    palabra = "Welcome"
    palabra2 = ""
    for i in palabra:
        os.system('cls' if os.name == 'nt' else 'clear')
        palabra2 = palabra2+i
        print (palabra2)
        time.sleep(0.06)
    time.sleep(2)
    for i in palabra:
        os.system('cls' if os.name == 'nt' else 'clear')
        palabra2 = palabra2[:len(palabra2)-1]
        print (palabra2)
        time.sleep(0.06)
    time.sleep(1)
    menu()

#verificar contraseña
def checkPsswd(contraseña_ingresada):
    contraseña = "211021"
    if contraseña_ingresada == contraseña:
        return True

#login
def login():
    os.system('cls' if os.name == 'nt' else 'clear')
    contraseña = "211021"
    contraseña_ingresada = input("Contraseña: ")
    if checkPsswd(contraseña_ingresada)==True:
        intro()
    else:
        ERROR()
        login()
login()
