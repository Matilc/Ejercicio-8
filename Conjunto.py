import os
class conjunto:
    def __init__(self):
        self.__conj=set()
    
    def cargar_conjunto(self):
        aux=''
        while aux.upper()!='N':
            num=int(input("Ingrese un elemento del conjunto:\n"))
            self.__conj.add(num)
            os.system('cls')
            aux=input("Ingrese cualquier tecla para agregar un número, o N para terminar de añadir elementos al conjunto:\n")
    
    def mostrar_conjunto(self):
        print(self.__conj)

    def get_conj(self):
        return self.__conj

    def __add__(self,otro):
        return self.__conj.union(otro.get_conj())
    
    def __radd__(self,otro):
        return self.__conj.union(otro.get_conj())
    
    def __sub__ (self,otro):
        return self.__conj.difference(otro.get_conj())
    
    def __rsub__ (self,otro):
        return self.__conj.difference(otro.get_conj())
    
    def __eq__ (self,otro):
        if self.__conj==otro.get_conj():
            return "Verdadero"
        else: 
            return "Falso"
    
    def __req__ (self,otro):
        if self.__conj==otro.get_conj():
            return "Verdadero"
        else: 
            return "Falso"