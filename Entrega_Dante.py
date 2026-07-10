
import colorama  # Colores para agregar en el terminal
from colorama import Fore, Style # importacion de colores

# 'autoreset=True' es para que pinte solo lo que le pedimos
colorama.init(autoreset=True)

# -stock inicial ID (NOMBRE DE ITEM, CATEGORIA Y PESO, TOTALMENTE ARBITRARIO PERO NO DOY MAS)  mano, nombre, categoria, precio y stock en números limpios para hacer la matemática de almacenero.
stock = [
    {"ID": "AA200", "nombre": "Arroz", "categoria": "Almacen", "precio": 1200, "stock": 45,},
    {"ID": "AC500", "nombre": "Cacao", "categoria": "Almacen", "precio": 345, "stock": 4,},
    {"ID": "AT20", "nombre": "Tartas", "categoria": "Cocina", "precio": 1000, "stock": 30,},#ahre por que cocina en un almacen
    {"ID": "LA220", "nombre": "Leche", "categoria": "Almacen", "precio": 1500, "stock": 12,},
    {"ID": "LD500", "nombre": "Detergente", "categoria": "Limpieza", "precio": 1900, "stock": 4,},
    {"ID": "FF8899", "nombre": "Fideos", "categoria": "Almacen", "precio": 1100, "stock": 45,},
    {"ID": "GG2233", "nombre": "Galletitas", "categoria": "Almacen", "precio": 850, "stock": 845,},
    {"ID": "BB100", "nombre": "Balde", "categoria": "Bazar", "precio": 4500, "stock": 10,},
    {"ID": "EB20", "nombre": "Escoba", "categoria": "Bazar", "precio": 3200, "stock": 67,},
    {"ID": "YA250", "nombre": "Yerba", "categoria": "Almacen", "precio": 3800, "stock": 2,}
]

opcion = "0"

# Bucle infinito hasta que elija la opcion 7.
while opcion != "7":
    # UN COLOR POR CADA MENU, QUE SE MANTIENE DESPUES.
    print()
    print(Fore.RED + "--- Bienvenido al Sistema de Gestión Avanzado ---")
    print(Fore.GREEN +"1 - Registrar un producto neuvo")
    print(Fore.BLUE +"2 - Visualizar datos de productos")
    print(Fore.YELLOW +"3 - Actualizar datos de producto (Por ID)")
    print(Fore.MAGENTA +"4 - Búsqueda inteligente de productos")
    print(Fore.CYAN +"5 - Eliminación de producto (Por posición)")
    print(Fore.WHITE +"6 - Reporte de límite de stock")
    print(Fore.RED +"7 - Salir")
    print(Fore.RED + "-------------------------------------------------")
    
    opcion = input("Elegí una opción para continuar: ").strip()

    match opcion:
        #primero voy a registrar un producto nuevo, para eso voy a pedirle al usuario que ingrese los datos del producto y los voy a guardar en un diccionario. 
        # Luego voy a agregar ese diccionario a la lista de stock.
        case "1":
            print(Fore.GREEN +"\n-------------------------")
            print(Fore.GREEN +"Registrar nuevo producto")
            print(Fore.GREEN +"-------------------------")

            # .upper() pasa las cosas a mayusculas, para que el ID quede uniforme. .strip() le saca los espacios al principio y al final.
            id_producto = input("ID único del producto: ").strip().upper()
            while id_producto == "":  
                print(Fore.RED + "[!] El id no puede quedar en blanco.")
                id_producto = input("ID único del producto: ").strip().upper()

            # .title() te acomoda el texto, con la primera en mayúscula
            nombre = input("Nombre del producto: ").strip().title()
            while nombre == "":  
                print(Fore.RED + "[!] Agrega un nombre por favor.")
                nombre = input("Nombre del producto: ").strip().title()
            
            categoria = input("Categoría a la que pertenece: ").strip().title()
            while categoria == "":
                print(Fore.RED + "[!] ¿A que categoria pertenece? No lo dejes en blanco.")
                categoria = input("Categoría a la que pertenece: ").strip().title()

            precio = input("Precio del producto: ").strip()
            # .isdecimal() vigila que sean números de verdad. Si le mandás letras, te lo devuelve como falso.
            while precio == "" or not precio.isdecimal():
                print(Fore.RED + "[!] Solo acepta numeros enteros.")
                precio = input("Precio del producto: ").strip()
            
            cantidad = input("Stock inicial disponible: ").strip()
            while cantidad == "" or not cantidad.isdecimal():
                print(Fore.RED + "[!] Necesito un numero entero para el stock, no inventes palabras.")
                cantidad = input("Stock del producto: ").strip()

            # Armamos el diccionario
            nuevo_producto = {
                "ID": id_producto,
                "nombre": nombre,
                "categoria": categoria,
                "precio": int(precio),       
                "stock": int(cantidad),
            }

            # .append() empuja la ficha al fondo de la lista
            stock.append(nuevo_producto)
            print(Fore.GREEN + f"\n¡Listo! '{nombre}' ya esta en el stock con el ID {id_producto}, Producto agregado con exito😎"")

        case "2":
            print("\n" + Fore.BLUE + "--------------------------------")
            print(Fore.BLUE + "               ESTADO DEL STOCK                                           ")
            print(Fore.BLUE + "--------------------------------=")
            
            total_dinero_stock = 0
            total_unidades_stock = 0

            for contador, item in enumerate(stock, start=1):
                # Metemos los modificadores de espacio (:<14) para que quede todo alineado y prolijo en la tabla.
                # Al ID le mandamos un amarillo para que resalte.
                print(f"#{contador:<2} | ID: {Fore.YELLOW}{item['ID']:<6}{Style.RESET_ALL} | Nombre: {item['nombre']:<10} | Cat: {item['categoria']:<10} | Precio: ${item['precio']:<8} | Stock: {item['stock']:<3} u. ")
                
                # cuanto plata hay y cuanto stock tenemos
                total_unidades_stock += item["stock"]
                total_dinero_stock += (item["precio"] * item["stock"])

            print(Fore.CYAN + "----------------------------------------------------------------")
            print(f" TOTAL DE UNIDADES EN EL GALPÓN: {total_unidades_stock} unidades.")
            print(f" GUITA TOTAL QUE VALE EL DEPOSITO: ${total_dinero_stock}")
            print(Fore.CYAN + "----------------------------------------------------------------")

        case "3":
            print(Fore.YELLOW +"\n----------------------------")
            print(Fore.YELLOW +"Actualizar datos de producto")
            print(Fore.YELLOW +"----------------------------")
            
            id_buscar = input("Ingresá el ID del producto a modificar: ").strip().upper()
            encontrado = False  # aca sabemos si encontramos el producto o no

            for contador, item in enumerate(stock):
                if id_buscar == item["ID"]:
                    print(Fore.GREEN + f"\n[✓] ¡Fichado! Encontramos al sospechoso: {item['nombre']}")
                    encontrado = True  

                    # pregunto bien que quiero cambiar
                    nombre_bool = input("¿Modificar nombre? Si/No: ").strip().title()
                    categoria_bool = input("¿Modificar categoría? Si/No: ").strip().title()
                    precio_bool = input("¿Modificar precio? Si/No: ").strip().title()
                    cantidad_bool = input("¿Modificar stock? Si/No: ").strip().title()

                    if nombre_bool == "Si":
                        nuevo_nom = input("Nuevo nombre: ").strip().title()
                        while nuevo_nom == "":
                            nuevo_nom = input(Fore.RED + "El nombre no puede ser un fantasma: ").strip().title()
                        stock[contador]["nombre"] = nuevo_nom  

                    if categoria_bool == "Si":
                        nueva_cat = input("Nueva categoría: ").strip().title()
                        while nueva_cat == "":
                            nueva_cat = input(Fore.RED + "La categoría no puede ser un fantasma: ").strip().title()
                        stock[contador]["categoria"] = nueva_cat

                    if precio_bool == "Si":
                        nuevo_pre = input("Nuevo precio: ").strip()
                        while nuevo_pre == "" or not nuevo_pre.isdecimal():
                            nuevo_pre = input(Fore.RED + "Escribi un número válido: ").strip()
                        stock[contador]["precio"] = int(nuevo_pre)

                    if cantidad_bool == "Si":
                        nuevo_stk = input("Nuevo stock físico: ").strip()
                        while nuevo_stk == "" or not nuevo_stk.isdecimal():
                            nuevo_stk = input(Fore.RED + "Escribi un número válido: ").strip()
                        stock[contador]["stock"] = int(nuevo_stk)
                    
                    print(Fore.GREEN + "\n[✓] Ahora si, todo bien.")
                    break  # aca rompemos el bucle para que no siga buscando el ID, ya que lo encontramos y actualizamos.

            if not encontrado:
                print(Fore.RED + "[!] Error: No se registra ningún artículo bajo el ID especificado.")

        case "4":
            print(Fore.MAGENTA +"\n--------------------------------")
            print(Fore.MAGENTA +"Búsqueda inteligente de productos")
            print(Fore.MAGENTA +"--------------------------------")
            
            print("Acá podés meter el ID, el nombre o la categoría.")
            busqueda = input("¿Que buscas?: ").strip().title()
            
            # Pasamos la búsqueda a mayúsculas para asegurarnos que esta bien escrito
            busqueda_id = busqueda.upper()
            encontrado = False

            print("\n Resultados de la búsqueda:")
            print("----------------------------------------------------------------")
            for item in stock:
                # El truco del 'in': si lo que buscás está metido adentro del nombre o del rubro, se lo fuma igual
                if (busqueda_id == item["ID"]) or (busqueda in item["nombre"]) or (busqueda in item["categoria"]):
                    
                    print(f"ID: {Fore.YELLOW}{item['ID']:<6}{Style.RESET_ALL} | Nombre: {item['nombre']:<14} | Cat: {item['categoria']:<10} | Precio: ${item['precio']:<5} | Stock: {item['stock']:<3} u. ")
                    encontrado = True

            print("----------------------------------------------------------------")
            if not encontrado:
                print(Fore.RED + "[!] No se encontraron resultados, volve a intentar maquina.")

        case "5":
            print(Fore.CYAN +"\n-----------------------")
            print(Fore.CYAN +"Eliminación de producto")
            print(Fore.CYAN +"-----------------------")

            print(f"Productos registrados en la lista: {len(stock)}")
            eliminar = input("¿Que producto querés eliminar? (ej: 1, 2): ").strip()
            
            while eliminar == "" or not eliminar.isdecimal():
                print(Fore.RED + "[!] Error: Meté un número de posición de la tabla por favor.")
                eliminar = input("Número de posición a eliminar: ").strip()

            num_posicion = int(eliminar)

            # Verificamos que el número de posición ingresado esté dentro del rango válido de la lista de stock
            if 1 <= num_posicion <= len(stock):
                # .pop() borra el elemento de la lista y lo devuelve, así podemos mostrarle al usuario qué producto fue eliminado.
                eliminado = stock.pop(num_posicion - 1)
                print(Fore.GREEN + f"\n[✓] El producto '{eliminado['nombre']}' fue eliminado del inventario.")
            else:
                print(Fore.RED + "[!] No existe esta fila.")

        case "6":
            print(Fore.WHITE +"\n---------------------------")
            print(Fore.WHITE +"Reporte de límite de stock")
            print(Fore.WHITE +"---------------------------")
            
            limite_bajo = input("¿Por debajo de qué número ya hay que salir a comprar? (Límite crítico): ").strip()
            while limite_bajo == "" or not limite_bajo.isdecimal():
                limite_bajo = input(Fore.RED + "Estás desde hoy poniendo cualquier cosa, UN numero entero te pido: ").strip()
            
            limite_bajo = int(limite_bajo)
            encontrado_bajo = False 

            print(f"\n Pedi ya estos articulos que ya hay menos de {limite_bajo} unidades):")
            print("----------------------------------------------------------------")
            for item in stock:
                # aca comparamos el stock de cada producto con el límite que nos dio el usuario. Si es menor o igual, lo mostramos en rojo y avisamos que hay que comprar.
                if item["stock"] <= limite_bajo:
                    print(f"  -> {Fore.RED} ¡Ojo! :{Style.RESET_ALL} A '{item['nombre']}' (ID: {item['ID']}) le quedan pocas unidades (solo {item['stock']} ) anda a comprar")
                    encontrado_bajo = True 
            print("----------------------------------------------------------------")
            
            if not encontrado_bajo:
                print(Fore.GREEN + "No hay stock bajo.")

        case "7":
            # fin de la ejecución del programa, con un mensaje de despedida
            print("\n" + Fore.RED + "#############################################################")
            print(f"noooooo ya esta? no termino tu horario laboral seguro tenes que seguir sumando stock...")
            print(f"¡Chau! Nos vemos en la próxima, que tengas un buen día.")
            print(Fore.RED + "#############################################################")

        case _:
            # verificamos que la opción ingresada no esté en la lista de opciones válidas y le avisamos al usuario
            print(Fore.RED + "\n###############")
            print(Fore.RED + "Esa no es una opcion de la lista, fijate bien y volve a intentarlo.")
            print(Fore.RED + "###############")