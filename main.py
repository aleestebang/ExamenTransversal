from Asistente import *
import numpy as np
from Escenario import *

asiento_escenario=np.full((10, 10), '---')
lista_asistentes=[]


llenarescenario(asiento_escenario)
print(asiento_escenario)

ciclo = True

while ciclo:
    print("Eventos Creativos.cl")
    print("1) Comprar entradas")
    print("2) Mostrar ubicaciones disponibles")
    print("3) Ver Listado de asistentes")
    print("4) Mostrar Ganancias totales")
    print("5) Salir")
    try:
        op=int(input("Ingrese opcion (1-5): "))
        match op:
            case 1:
                print("Compra de entradas")
                comprarEntrada(asiento_escenario, lista_asistentes)
            case 2:
                print("Ubicaciones disponibles")
                mostrarUbicaciones(asiento_escenario)
            case 3:
                print("Listado")
                ListadoAsistentes(lista_asistentes)
            case 4:
                print("Ganancias")
                MostrarGanancias(asiento_escenario)
            case 5:
                print("Saliendo")
                ciclo = salir()
            case _:
                print("Ingreso un numero no valido")
    except BaseException as error:
        print(f"Error: {error}")