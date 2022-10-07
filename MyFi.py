import time
import os
import pandas as pd
import pwinput

def ERROR(): #animacion de error
    for i in range(0,3):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("ERROR")
                time.sleep(0.3)
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(0.3)


def mostrar_ingresos(): #menu ingresos
    os.system('cls' if os.name == 'nt' else 'clear')
    print("                       ***INGRESOS***")
    df = pd.read_csv("income.csv")

    if df.shape[0] == 0:  #check if dataFrame is empty
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


def mostrar_gastos(): #menu gastos
    os.system('cls' if os.name == 'nt' else 'clear')
    print("                       ***GASTOS***")
    df = pd.read_csv("Gastos.csv")

    if df.shape[0] == 0: #check if empty
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
        

def menu():      #menu Display
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1- Gastos")
    print("2- Ingresos")
    seleccion = str(input())
    procesar_seleccion(seleccion)


def intro():        #opening/greeting
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


def checkPsswd(contraseña_ingresada):   #verificar contraseña
    contraseña = "12345"
    if contraseña_ingresada == contraseña:
        return True


def login():    #login
    os.system('cls' if os.name == 'nt' else 'clear')
    contraseña = "211021"
    contraseña_ingresada = pwinput.pwinput(prompt="Contraseña: ", mask="*")
    if checkPsswd(contraseña_ingresada)==True:
        intro()
    else:
        ERROR()
        login()
login()
