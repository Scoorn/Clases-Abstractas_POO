from empleado import Empleado

class EmpleadoMedioTiempo(Empleado):
    def __init__(self,nombre,horas_trabajadas,pago_por_hora):
        self.nombre=nombre
        self.horas_trabajadas=horas_trabajadas
        self.pago_por_hora=pago_por_hora
    
    def calcular_salario(self):
        return self.horas_trabajadas*self.pago_por_hora
    
    def mostrar_info(self):
        print(f"Empleado: {self.nombre}")
        print(f"Horas trabajadas: {self.horas_trabajadas}")
        print(f"Pago por hora: {self.pago_por_hora}")
        print(f"Salario : {self.calcular_salario()}")
        
