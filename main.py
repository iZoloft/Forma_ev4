from functions import *

limpiar()
while True:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 1:
        agregar_producto(lista_productos)   
    elif opcion == 2:
        nombre = input("Ingrese nombre a buscar: \n").strip()
        posicion = buscar_producto(nombre)
        if posicion != -1:
            print(f"producto encontrado en la posicion: {posicion}")
            print(f"Nombre: {lista_productos[posicion]["nombre"]}")
            print(f"Stock: {lista_productos[posicion]["stock"]}")
            print(f"Precio: {lista_productos[posicion]["precio"]}")
            if lista_productos[posicion]["disponible"] == True:
                print("Estado: Disponible")
            else:
                print("Estado: Sin Stock")
        else:
            print("No se encontraron productos")
    elif opcion == 3:
        nombre = input("Ingrese nombre a eliminar: \n").strip()
        posicion = buscar_producto(nombre)
        if posicion >= 0:
            lista_productos.pop(posicion)
            print("Producto Eliminado")
        else:
            print(f"El producto {nombre} no se encuentra registrado")
    elif opcion == 4:
        actualizar_disponibilidad(lista_productos)
    elif opcion == 5:
        mostrar_productos()
    elif opcion == 6:
        print("“Gracias por usar el sistema. Vuelva Pronto”")
        break