import os
from Conjunto import conjunto
def menu_opciones():
    print("Menú de opciones:")
    print("1. Unir conjuntos")
    print("2. Diferencia de conjuntos")
    print("3. Verificar si conjuntos son iguales")
    print("4. Salir")

if __name__=='__main__':
    c=conjunto()
    print ("Cargar conjunto 1")
    c.cargar_conjunto()
    otro=conjunto()
    print ("Cargar conjunto 2")
    otro.cargar_conjunto()
    c.mostrar_conjunto()
    otro.mostrar_conjunto()
    aux=input("\nIngrese cualquier tecla para continuar\n")
    while True:
        os.system('cls')
        menu_opciones()
        menu= {
            "1": 'print (c+otro)',
            "2": 'print (c-otro)',
            "3": 'print ("El resultado de la comparación es: "+str(c==otro))',
            "4": "print ('Gracias por usar nuestro sistema')"
        }
        opcion= input("Elija la opción ")
        os.system('cls')
        if opcion in menu:
            if opcion=='4':
                eval(menu[opcion])
                break
            else:
                eval(menu[opcion])
        else:
            print ('La opción que ha ingresado no es válida, por favor, ingrese una opción nuevamente')
        aux=input("\nIngrese cualquier tecla para continuar\n")