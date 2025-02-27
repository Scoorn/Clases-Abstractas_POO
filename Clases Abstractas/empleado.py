from abc import ABC, abstractmethod

class Empleado (ABC):
    @abstractmethod
    def calcular_salario():
        pass
    
    @abstractmethod
    def mostrar_info():
        pass