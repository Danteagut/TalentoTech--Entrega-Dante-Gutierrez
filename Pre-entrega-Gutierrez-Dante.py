.venv\Scripts\activate
import colorama  # Colores para agregar en el terminal
from colorama import Fore, Style # importacion de colores

# 'autoreset=True' es para que pinte solo lo que le pedimos
colorama.init(autoreset=True)

# -stock inicial ID  mano, nombre, categoria, precio y stock en números limpios para hacer la matemática de almacenero, y el vencimiento con datetime o None.
stock = [
    {"ID": "AA0054", "nombre": "Arroz", "categoria": "Almacen", "precio": 1200, "stock": 45, "Vencimiento": datetime.datetime(2027, 8, 15)},
    {"ID": "CC5689", "nombre": "Cacao", "categoria": "Almacen", "precio": 2800, "stock": 4, "Vencimiento": datetime.datetime(2026, 11, 20)},
    {"ID": "TT3245", "nombre": "Te", "categoria": "Almacen", "precio": 950, "stock": 30, "Vencimiento": datetime.datetime(2027, 5, 10)},
    {"ID": "LL1122", "nombre": "Lavandina", "categoria": "Limpieza", "precio": 1500, "stock": 20, "Vencimiento": None},
    {"ID": "DD4455", "nombre": "Detergente", "categoria": "Limpieza", "precio": 1900, "stock": 3, "Vencimiento": None},
    {"ID": "FF8899", "nombre": "Fideos", "categoria": "Almacen", "precio": 1100, "stock": 60, "Vencimiento": datetime.datetime(2026, 12, 5)},
    {"ID": "GG2233", "nombre": "Galletitas", "categoria": "Almacen", "precio": 850, "stock": 80, "Vencimiento": datetime.datetime(2026, 10, 18)},
    {"ID": "BB9911", "nombre": "Balde", "categoria": "Bazar", "precio": 4500, "stock": 8, "Vencimiento": None},
    {"ID": "EE7744", "nombre": "Escoba", "categoria": "Bazar", "precio": 3200, "stock": 10, "Vencimiento": None},
    {"ID": "YY6655", "nombre": "Yerba", "categoria": "Almacen", "precio": 3800, "stock": 25, "Vencimiento": datetime.datetime(2027, 3, 22)}
]

opcion = "0"

# Bucle infinito hasta que elija la opcion 7.
while opcion != "7":
    # Le mandamos un celeste de bienvenida.
    print()
    print(Fore.RED + "--- Bienvenido al Sistema de Gestión Avanzado ---")
    print("1 - Registrar nuevo producto")
    print("2 - Visualizar datos de productos")
    print("3 - Actualizar datos de producto (Por ID)")
    print("4 - Búsqueda inteligente de productos")
    print("5 - Eliminación de producto (Por posición)")
    print("6 - Reporte de límite de stock")
    print("7 - Salir")
    print(Fore.RED + "-------------------------------------------------")
    
    opcion = input("Elegí una opción para continuar: ").strip()

    match opcion:
        
        case "1":
            print("\n-------------------------")
            print("Registrar nuevo producto")
            print("-------------------------")

            # .upper() es para que si el usuario es un colgado y te escribe en minúscula, el sistema se lo pase a un roscazo a mayúsculas
            id_producto = input("ID único del producto: ").strip().upper()
            while id_producto == "":  
                print(Fore.RED + "[!] Pará la mano, el ID no puede quedar en banda (vacío).")
                id_producto = input("ID único del producto: ").strip().upper()

            # .title() te acomoda el texto, con la primera en mayúscula
            nombre = input("Nombre del producto: ").strip().title()
            while nombre == "":  
                print(Fore.RED + "[!] Dale, no te hagás el vivo y metele un nombre al bicho.")
                nombre = input("Nombre del producto: ").strip().title()
            
            categoria = input("Categoría a la que pertenece: ").strip().title()
            while categoria == "":
                print(Fore.RED + "[!] ¿Qué categoría? No dejes esto en bolas, poné algo.")
                categoria = input("Categoría a la que pertenece: ").strip().title()

            precio = input("Precio del producto: ").strip()
            # .isdecimal() vigila que sean números de verdad. Si le mandás letras, te lo devuelve como falso y te hace repetir la jugada.
            while precio == "" or not precio.isdecimal():
                print(Fore.RED + "[!] No me rompás el boliche, meté un precio que sea un número entero.")
                precio = input("Precio del producto: ").strip()
            
            cantidad = input("Stock inicial disponible: ").strip()
            while cantidad == "" or not cantidad.isdecimal():
                print(Fore.RED + "[!] ¿Cuánta merca tenés? Poné un número de verdad o nos fundimos.")
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
            print(Fore.GREEN + f"\n¡Listo el pollo! '{nombre}' adentro del stock con el ID {id_producto}.")

        case "2":
            print("\n" + Fore.RED + "=========================================================================================")
            print(Fore.RED + "                                   DATOS DE PRODUCTOS REGISTRADOS                        ")
            print(Fore.RED + "=========================================================================================")
            
            total_dinero_stock = 0
            total_unidades_stock = 0

            # Recorremos el espinel arrancando desde 1 para que el ser humano lea prolijo
            for contador, item in enumerate(stock, start=1):
                if item["Vencimiento"] is not None:
                    vence_txt = item["Vencimiento"].strftime("%d/%m/%Y")
                else:
                    vence_txt = "No vence"

                # Metemos los modificadores de espacio (:<14) para que la tabla no quede hecha un acordeón desinflado.
                # Al ID le mandamos un amarillo para que resalte.
                print(f"#{contador:<2} | ID: {Fore.YELLOW}{item['ID']:<6}{Style.RESET_ALL} | Nombre: {item['nombre']:<18} | Cat: {item['categoria']:<10} | Precio: ${item['precio']:<5} | Stock: {item['stock']:<3} u. | Vence: {vence_txt}")
                
                # Sumamos los porotos: cuántas unidades hay y cuánta guita vale el galpón completo
                total_unidades_stock += item["stock"]
                total_dinero_stock += (item["precio"] * item["stock"])

            print(Fore.CYAN + "=========================================================================================")
            print(f" TOTAL DE UNIDADES EN EL GALPÓN: {total_unidades_stock} unidades.")
            print(f" GUITA TOTAL QUE VALE EL DEPOSITO: ${total_dinero_stock}")
            print(Fore.CYAN + "=========================================================================================")

        case "3":
            print("\n----------------------------")
            print("Actualizar datos de producto")
            print("----------------------------")
            
            id_buscar = input("Ingresá el ID del producto a modificar: ").strip().upper()
            encontrado = False  # El perito que nos dice si el ID existe o si nos están vendiendo humo

            for contador, item in enumerate(stock):
                if id_buscar == item["ID"]:
                    print(Fore.GREEN + f"\n[✓] ¡Fichado! Encontramos al sospechoso: {item['nombre']}")
                    encontrado = True  

                    # Interrogatorio con Si/No para ver qué parte quiere cambiar
                    nombre_bool = input("¿Modificar nombre? Si/No: ").strip().title()
                    categoria_bool = input("¿Modificar categoría? Si/No: ").strip().title()
                    precio_bool = input("¿Modificar precio? Si/No: ").strip().title()
                    cantidad_bool = input("¿Modificar stock? Si/No: ").strip().title()

                    if nombre_bool == "Si":
                        nuevo_nom = input("Nuevo nombre: ").strip().title()
                        while nuevo_nom == "":
                            nuevo_nom = input(Fore.RED + "Mete algo pa, no lo dejes en blanco: ").strip().title()
                        stock[contador]["nombre"] = nuevo_nom  

                    if categoria_bool == "Si":
                        nueva_cat = input("Nueva categoría: ").strip().title()
                        while nueva_cat == "":
                            nueva_cat = input(Fore.RED + "La categoría no puede ser un fantasma: ").strip().title()
                        stock[contador]["categoria"] = nueva_cat

                    if precio_bool == "Si":
                        nuevo_pre = input("Nuevo precio: ").strip()
                        while nuevo_pre == "" or not nuevo_pre.isdecimal():
                            nuevo_pre = input(Fore.RED + "Mandale un número entero o me enojo: ").strip()
                        stock[contador]["precio"] = int(nuevo_pre)

                    if cantidad_bool == "Si":
                        nuevo_stk = input("Nuevo stock físico: ").strip()
                        while nuevo_stk == "" or not nuevo_stk.isdecimal():
                            nuevo_stk = input(Fore.RED + "Poné cuántos bultos quedan de verdad: ").strip()
                        stock[contador]["stock"] = int(nuevo_stk)
                    
                    print(Fore.GREEN + "\n[✓] Ficha tuneada correctamente. Quedó una pinturita.")
                    break  # Si ya lo pescamos, rompemos el bucle para no seguir buscando

            if not encontrado:
                print(Fore.RED + "[!] Error: No se registra ningún artículo bajo el ID especificado.")

        case "4":
            print("\n--------------------------------")
            print("Búsqueda inteligente de productos")
            print("--------------------------------")
            
            print("Acá podés meter el ID, el nombre o la categoría... lo que pinte.")
            busqueda = input("¿Qué estás buscando, chamigo?: ").strip().title()
            
            # Pasamos la búsqueda a mayúsculas por si el tipo metió un código de ID y anda con paja de apretar el Shift
            busqueda_id = busqueda.upper()
            encontrado = False

            print("\nLo que saltó en el radar:")
            print("-----------------------------------------------------------------------------------------")
            for item in stock:
                # El truco del 'in': si lo que buscás está metido adentro del nombre o del rubro, se lo fuma igual
                if (busqueda_id == item["ID"]) or (busqueda in item["nombre"]) or (busqueda in item["categoria"]):
                    if item["Vencimiento"] is not None:
                        vence_txt = item["Vencimiento"].strftime("%d/%m/%Y")
                    else:
                        vence_txt = "No vence"
                    
                    print(f"ID: {Fore.YELLOW}{item['ID']:<6}{Style.RESET_ALL} | Nombre: {item['nombre']:<14} | Cat: {item['categoria']:<10} | Precio: ${item['precio']:<5} | Stock: {item['stock']:<3} u. | Vence: {vence_txt}")
                    encontrado = True

            print("-----------------------------------------------------------------------------------------")
            if not encontrado:
                print(Fore.RED + "[!] No saltó nada en el radar. Revisá lo que tipeaste, ERROR DE CAPA 8.")

        case "5":
            print("\n-----------------------")
            print("Eliminación de producto")
            print("-----------------------")

            print(f"Bultos registrados en la lista: {len(stock)}")
            eliminar = input("¿Qué número de fila querés borrar del mapa? (ej: 1, 2): ").strip()
            
            while eliminar == "" or not eliminar.isdecimal():
                print(Fore.RED + "[!] Error: Meté un número de posición de la tabla, no inventes palabras.")
                eliminar = input("Número de posición a eliminar: ").strip()

            num_posicion = int(eliminar)

            # El candado para que el usuario no pida borrar la fila 50 si tenemos 10 productos cargados
            if 1 <= num_posicion <= len(stock):
                # .pop() le mete un hachazo al elemento. Le restamos 1 porque Python cuenta desde el cero (es medio raro)
                eliminado = stock.pop(num_posicion - 1)
                print(Fore.GREEN + f"\n[✓] El producto '{eliminado['nombre']}' marchó al espiedo. Borrado por completo.")
            else:
                print(Fore.RED + "[!] Te fuiste al pasto. Esa fila no existe en este inventario.")

        case "6":
            print("\n---------------------------")
            print("Reporte de límite de stock")
            print("---------------------------")
            
            limite_bajo = input("¿Por debajo de qué número estamos en problemas? (Límite crítico): ").strip()
            while limite_bajo == "" or not limite_bajo.isdecimal():
                limite_bajo = input(Fore.RED + "Dejate de joder y poné un número entero entero: ").strip()
            
            limite_bajo = int(limite_bajo)
            encontrado_bajo = False 

            print(f"\nArtículos que están en la lona (igual o menos de {limite_bajo} unidades):")
            print("-----------------------------------------------------------------------------------------")
            for item in stock:
                # Comparamos la escasez. Si la cantidad es menor al límite, tiramos la bronca en pantalla
                if item["stock"] <= limite_bajo:
                    print(f"  -> {Fore.RED}ALERTA:{Style.RESET_ALL} A '{item['nombre']}' (ID: {item['ID']}) le quedan apenas {item['stock']} unidades. ¡Se viene la noche!")
                    encontrado_bajo = True 
            print("-----------------------------------------------------------------------------------------")
            
            if not encontrado_bajo:
                print(Fore.GREEN + "Venimos zafando. Todo el stock está por encima del nivel de malaria.")

        case "7":
            # Agarramos la hora del segundero de la PC para dejar asentado cuándo rajó el operario
            fecha_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print("\n" + Fore.CYAN + "#############################################################")
            print(f"Gracias por utilizar el Sistema de Gestión de Ricardo.")
            print(f"Rajamos del sistema a las: {fecha_hora}. ¡Nos vemo' en la esquina!")
            print(Fore.CYAN + "#############################################################")

        case _:
            # Por si el usuario mete los dedos gordos en el teclado y tipea cualquiera
            print(Fore.RED + "\n###############")
            print(Fore.RED + "¿Qué tocás pa?")
            print(Fore.RED + "###############")