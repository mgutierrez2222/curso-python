from os import system
system("cls")


while True:
    op=int(input("Ingresa una opción 1-3 - 0 para salir: "))
    if op==1:
        print("Selecciono opción 1")
    elif op==2:
        print("Selecciono opción 2")
    elif op==3:
        print("Selecciono opción 3")
    elif op==0:
        print("Fin del programa....")
        break
    else:
        print("Opción no válida")
        