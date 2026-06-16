import os, time

lista_productos= []

def limpiar():
    os.system("cls")

def pausar():
    time.sleep(2)

def _validar_str(string):
    if len(string) > 0:
        return True
    else:
        print("Campo no puede venir vacio")

def _validar_int(numero):
    if numero > 0:
        return True
    else:
        print("El número debe ser mayor a 0")

def _validar_float(numero):
    if numero > 0:
        return True
    else:
        print("El número debe ser mayor a 0")

def agregar_producto(lista_productos):
    while True:
        nombre = input("Ingrese nombre del producto: \n").split()
        if _validar_str(nombre):
            break
    while True:
        try:
            stock = int(input("Ingrese stock del producto: \n"))
            if _validar_int == True:
                break
        except:
            print("El número ingresado no es un entero")
    while True:
        try:
            precio = float(input("Ingrese precio del producto: \n"))
            if _validar_float == True:
                break
        except:
            print("El número ingresado no es un entero")
    # Cargamos diccionario
    producto = {
        "nombre" : nombre,
        "stock" : stock,
        "precio" : precio,
        "disponible" : False
    }
    # Agregamos el elemento a la lista
    producto.append(lista_productos)
    pausar()