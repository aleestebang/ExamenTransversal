import Asistente
from Asistente import *
import numpy as np

def llenarescenario(asiento_escenario):
    x=0
    for f in range(10):
        for c in range(10):
            x=x+1
            asiento_escenario[f][c]=str(x)


def mostrarUbicaciones(asiento_escenario):
    for f in range(10):
        fila=''
        for c in range(10):
            datos=str(asiento_escenario[f][c])
            if len(str(asiento_escenario[f][c]))==1:
                datos='0'+str(asiento_escenario[f][c])
            if len(str(asiento_escenario[f][c]))==2:
                datos='0'+str(asiento_escenario[f][c])
            fila=fila+''+datos
            print(fila)


def comprarEntrada(asiento_escenario, lista_asistentes):
    print("Venta Maxima de entradas 3")
    num_asiento=validarasiento()
    x=1
    while(x<=num_asiento):
        print("Seleccione Asiento")
        print("******************")
        mostrarUbicaciones(asiento_escenario)
        print(f"-Seleccione el {x} asiento-")
        num_asiento=validarasiento()
        disponible=validarasiento(asiento_escenario, num_asiento)
        if disponible==True:
            asis=Asistente()
            asis.run=validarrut()
            asis.nombre=input("Ingrese nombre:")
            asis.apellido=input("Ingrese Apellido:")
            asis.num_asiento=num_asiento
            asis.valor_asiento=valorasiento(num_asiento)
            marcarocupado(asiento_escenario, num_asiento)
            print("asiento Comprado")
            x=x+1
            lista_asistentes.append(asis)
        else:
            print("Asiento Comprado anteriormente")

def marcarocupado(asiento_escenario, num_asiento):
    x=0
    for f in range(10):
        for c in range(10):
            x=x+1
            if x==int(num_asiento):
                asiento_escenario[f][c]='-X-'

def valorasiento(num_asiento):
    if int(num_asiento)>=1 and int(num_asiento)<=20:
        print("Asiento Platinum $120.000")
        return 120000
    if int(num_asiento)>=21 and int(num_asiento)<=50:
        print("Asiento Gold $80.000")
        return 80000
    if int(num_asiento)>=51 and int(num_asiento)<=100:
        print("Asiento Silver $50.000")
        return 50000

def validarasiento():
    ciclo = True
    while (ciclo):
        try:
            num_asientos=int(input("Indique los asientos a comprar (maximo 3):"))
            if num_asientos>=1 and num_asientos<=100:
                return num_asientos
            else:
                print("La venta maxima de entrada son 3 por persona ")
        except:
            print("Ingrese solo numeros")

def validar_opcionasiento():
    ciclo =True
    while(ciclo):
        try:
            num_asientos=int(input('Indique la cantida de asiento a comprar (1-3):'))
            if num_asientos>=1 and num_asientos<=5:
                return num_asientos
            else:
                print("Asientos maximos a comprar 3")
        except:
            print("solo numeros")

def validarrut():
    ciclo=True
    while(ciclo):
        run=input("Ingrese Run ej 12345678")
        if run.isnumeric() and len(run)==8:
            return run
        else:
            print("Ingreso un rut erroneo")
            return  False

def cont_asiento(inicio, fin ,asiento_escenario):
    x=0
    contador=0
    for f in range(10):
        for c in range (10):
            x=x+1
            if x>=inicio and x<=fin:
                if asiento_escenario[f][c]=='-X-':
                    contador=contador+1
    return contador

def MostrarGanancias(asiento_escenario):
    cantplat=cont_asiento(1, 20, asiento_escenario)
    cantgold=cont_asiento(21, 50, asiento_escenario)
    cantsilver=cont_asiento(51, 100, asiento_escenario)
    totalplat=cantplat*120000
    totalgold=cantgold*80000
    totalsilver=cantsilver*50000
    print('Platinum: '+str(cantplat)+'='+str(totalplat))
    print('Gold: ' + str(cantgold) + '=' + str(totalgold))
    print('Silver: ' + str(cantsilver) + '=' + str(totalsilver))



def ListadoAsistentes(lista_asistentes):
    for item in lista_asistentes:
        print('Run:'+str(item.run)+'Nombre'+str(item.nombre)+' '+str(item.apellido))


def salir():
    print("Saliendo de Eventos Creativos.cl")
    print("Version 1.0")
    return False

