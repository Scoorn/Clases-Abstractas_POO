# Clases Abstractas
## Descripcion general 🚀
Para saber como emplear clases abstractas tienes que entender que te permite definir una especie de "plantilla" o "contrato" para otras clases. En este ejemplo veremos como aplicarla.
## Explicacion 
Haremos un ejemplo con el salario de un empleado tiempo completo y un empleado de medio tiempo. Comenzamos declarando la clase Empleado pero es importante aclarar que se nesecita:
```
from abc import ABC, abstractmethod

class Empleado (ABC):
    @abstractmethod
    def calcular_salario():
        pass
    
    @abstractmethod
    def mostrar_info():
        pass
```
"ABC, abstractmethod" se necesitan para hacerlas abstractas, con el "pass" la declaramos nula hasta que no se herede de ella y reciba argumentos. 

Ahora bien creamos la clase  EmpleadoTiempoCompleto(Empleado) y aqui definimos 3 metodos el primero para recibir los argumentos necesarios como nombre y salario_mensual. el segundo calcula el salario de la persona, pero en este caso como el salario del usuario es el mismo que ingreso, solo se le asigna lo ingresado, y por ultimo el tercer metodo muestrar la informacion detallada, como el nombre y su salario mensual: 
```
def mostrar_info(self):
        print(f"Empleado: {self.nombre}")
        print(f"Salario mensual: {self.calcular_salario()}")
```
Seguimos con la clase EmpleadoMedioTiempo(Empleado)igualmente con tres metodos, pero aqui el primer metodo recibe horas trabajadas y pago por hora que utilizaremos en el segundo metodo para calcular su salario que seria horas * pago por hora:
```
def calcular_salario(self):
        return self.horas_trabajadas*self.pago_por_hora
```
Se mantiene el metodo para mostrar informacion pero esta vez con el salario de la persona:
```
 print(f"Salario : {self.calcular_salario()}")
```
## Ejecutando las pruebas ⚙️ 
En el "main.py" (programa principal) importamos ambas clases:
```
from tiempocompleto import EmpleadoTiempoCompleto
from mediotiempo import EmpleadoMedioTiempo
```
Ahora le ingresamos valores para ver los resultados:
```
EMT=EmpleadoMedioTiempo("Norkys",8,20)
EMT.mostrar_info()
print("\n")
ETC=EmpleadoTiempoCompleto("Paulo",200)
ETC.mostrar_info()
```
El "print("\n")" lo que hace es agregar un salto de linea para que no se vea la informacion muy junta 

Finalmente la terminal deberia verse asi (recuerda que puedes modificar los nombres y salarios):
```
Empleado: Norkys
Horas trabajadas: 8 
Pago por hora: 20   
Salario : 160       


Empleado: Paulo     
Salario mensual: 200

```
## Autora✒️
Norkys Peña

## Gratitud 🎁
Si deseas apoyar siguenos y comenta por alguna duda. Aceptamos donaciones $$ 🤑
