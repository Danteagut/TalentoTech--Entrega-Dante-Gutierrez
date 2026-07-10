stock = [["camisa", "ropa", "1000"], ["pantalon", "ropa", "2000"], ["zapatillas", "calzado", "3000"]]

opcion = "0"
while opcion != "5":
    print  ("Bievenidos al organizador de productos online")
    print ( )
    print("1- Agregar producto")
    print("2- Visualizar productos")
    print("3- Buscar producto")
    print("4- Eliminar producto")
    print("5- Salir")

    opcion = input("elegi una opcion para continuar:")

    match opcion:
        case "1":
            print("////////////////" )
            print("agregar producto")
            print("////////////////" )

            nombre = input("Ingrese el nombre del producto:").strip().title()
            while nombre == "":
                print("El nombre del producto no puede estar vacio")
                nombre = input("Ingrese el nombre del producto:").strip().title()

            categoria = input("Ingrese la categoria del producto:").strip().title()
            while categoria == "":
                print("La categoria no puede estar vacia")
                categoria = input("Ingrese la categoria del producto:").strip().title()

            precio = input("Ingrese el precio del producto:").strip().title()
            while precio == "" or not precio.isdigit():
                print("El precio no puede estar vacio y tiene que ser un numero")
                precio = (input("Ingrese el precio del producto:").strip().title())
            
            producto = []
            producto.append(nombre)
            producto.append(categoria)
            producto.append(precio)

            stock.append(producto)

            
            print("Producto agregado con exito😎")

        case "2":
            print("////////////////")
            print("visualizar productos")
            print("////////////////")

            i = 1

            for item in stock:
                print(f"producto id # {i}")
                print("Nombre:", item[0])
                print("Categoria:", item[1])
                print("Precio:", item[2])
                print()
                i += 1

        case "3":
            print("////////////////" )
            print("Busca producto")
            print("////////////////" )
            encontrado = False
            for item in stock:
                busqueda = input("Ingrese el nombre del producto a buscar:").strip().title()
                if busqueda == item[0]:
                    print("Producto encontrado")
                    print("Nombre:", item[0])
                    print("Categoria:", item[1])
                    print("Precio:", item[2])
                    encontrado = True
            if encontrado == False:
                print("Producto no encontrado")
            if busqueda == "":
                print("La busqueda no puede estar vacia")
        case "4":
            print("////////////////" )
            print("Eliminar producto")
            print("////////////////" )
            eliminar = input("Ingrese el numero del producto a eliminar:").strip().title()
            encontrado = False
            for item in stock:
                if eliminar == item[0]:
                    print("Producto eliminado")
                    print("Nombre:", item[0])
                    print("Categoria:", item[1])
                    print("Precio:", item[2])
                    encontrado = True
                    stock.remove(item)
            if encontrado == False:
                print("Producto no encontrado")
        case "5":
            print("////////////////" )
            print("salir")
            print("////////////////" )
        case _:
            print("opcion no valida")   