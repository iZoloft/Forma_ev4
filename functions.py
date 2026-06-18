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
    if numero >= 0:
        return True
    else:
        print("El número debe ser mayor a 0")

def _validar_float(numero):
    if numero > 0:
        return True
    else:
        print("El número debe ser mayor a 0")

def mostrar_menu():
    print("=======Menu=======")
    print("1. Agregar Producto")
    print("2. Mostrar Producto")
    print("3. Eliminar Producto")
    print("4. Actualizar Disponibilidad")
    print("5. Mostrar Productos")
    print("6. Salir")

def leer_opcion():
    try:
        opcion = int(input("Ingrese opción: \n"))
        if opcion > 0 and opcion <= 6:
            return opcion
        else:
            print("Opción debe estar entre 1 y 6")
    except:
        print("Valor debe ser numérico")

def agregar_producto(lista_productos):
    while True:
        nombre = input("Ingrese nombre del producto: \n").strip()
        if _validar_str(nombre):
            break
    while True:
        try:
            stock = int(input("Ingrese stock del producto: \n"))
            if _validar_int(stock) == True:
                break
        except:
            print("El número ingresado no es un entero")
    while True:
        try:
            precio = float(input("Ingrese precio del producto: \n"))
            if _validar_float(precio) == True:
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
    lista_productos.append(producto)
    print("Producto Agregado")
    pausar()

def buscar_producto(nombre):
    for p in range(len(lista_productos)):
        #si el nombre que busco existe en la lista
        if lista_productos[p]["nombre"] == nombre:
            #retornare la posicion en la que se encuentra 'EL producto'
            return p
    #si no encuentra ningun nombre, retornara -1
    return -1

def actualizar_disponibilidad(lista_productos):
    for p in lista_productos:
        if p["stock"] > 0:
            p["disponible"] = True
        else:
            p["disponible"] = False
    print("Lista actualizada")

def mostrar_productos():
    actualizar_disponibilidad(lista_productos)
    print("=== LISTA DE PRODUCTOS ===")
    for p in lista_productos:
        print(f"Nombre: {p["nombre"]}")
        print(f"Stock: {p["stock"]}")
        print(f"Precio: {p["precio"]}")
        if p["disponible"] == True:
            print("Estado: Disponible")
        else:
            print("Estado: Sin Stock")
        print("*********************************")
