import os

def funcion1():
    # limpia la pantalla
    os.system("cls")
    print("Dame dos numeros:")
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    print("La suma de los dos numeros es: ", num1+num2)
    print("¿Desea continuar con las operaciones? s/n")
    respuesta = input()
    if respuesta == "s":
        input(run())
    if respuesta == "n":
        print("Adios")
        exit()
    
def funcion2():
    os.system("cls")
    print("Dame dos numeros:")
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    print("La resta de los dos numeros es: ", num1-num2)
    print("¿Desea continuar con las operaciones? s/n")
    respuesta = input()
    if respuesta == "s":
        input(run())
    if respuesta == "n":
        print("Adios")
        exit()
    
def funcion3():
    os.system("cls")
    print("Dame dos numeros:")
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    print("La multiplicación de los dos numeros es: ", num1*num2)
    print("¿Desea continuar con las operaciones? s/n")
    respuesta = input()
    if respuesta == "s":
        input(run())
    if respuesta == "n":
        print("Adios")
        exit()
    
def funcion4():
    os.system("cls")
    print("Dame dos numeros:")
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    print("La división de los dos numeros es: ", num1/num2)
    print("¿Desea continuar con las operaciones? s/n")
    respuesta = input()
    if respuesta == "s":
        input(run())
    if respuesta == "n":
        print("Adios")
        exit()


def run():
    while True:
        os.system("cls")
        print("Menú de opciones: ")
        print("1.- Suma")
        print("2.- Resta") 
        print("3.- Multiplicación")
        print("4.- División")
        print("5.- Salir")
        opcion = int(input("Dame una opcion: "))
        if opcion == 1:
            funcion1()
        if opcion == 2:
            funcion2()
        if opcion == 3:
            funcion3()
        if opcion == 4:
            funcion4()
        if opcion == 5:
            os.system("cls")
            print("Adios")
            exit()

# esta es para que se ejecute la función run como principal
if __name__ == "__main__":
    run()