import numpy as np
from paciente import Paciente

class ColaS:
    __cant = 0 
    __pr = 0
    __ul = 0
    __max = 0

    def __init__(self, max):
        self.__item = np.empty(max, dtype = Paciente)
        self.__pr = 0
        self.__ul = 0
        self.__cant = 0
        self.__max = max
    
    def vacio(self):
        return self.__cant == 0
    
    def lleno(self):
        return self.__cant == self.__max-1

    def insertar(self, x):
        if (self.__cant < self.__max):
            self.__item[self.__ul] = x
            self.__ul = (self.__ul+1)%self.__max
            self.__cant += 1
            return x
        else: 
            return 0
    
    def suprimir(self):
        if self.vacio():
            print('\nLa Cola esta vacia')
        else:
            x = self.__item[self.__pr]
            self.__item = np.delete(self.__item,self.__pr)
            self.__pr = (self.__pr+1)%self.__max
            self.__cant -= 1
            return x
        
    def mostrar(self):
        if not self.vacia():
            i = 0
            while (i < self.__cant):
                print(self.__item[i])
                i += 1 