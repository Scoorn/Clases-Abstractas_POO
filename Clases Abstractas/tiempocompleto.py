from empleado import Empleado

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self,nombre,salario_mensual):
        self.nombre=nombre
        self.salario_mensual=salario_mensual
        
    def calcular_salario(self):
        return self.salario_mensual
    
    def mostrar_info(self):
        print(f"Empleado: {self.nombre}")
        print(f"Salario mensual: {self.calcular_salario()}")
        