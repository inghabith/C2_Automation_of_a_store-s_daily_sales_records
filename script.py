def registro_de_ventas():
    productos = []
    agregar = "si"

    while agregar == "si":
        print()
        print("     ----NUEVO PRODUCTO----")
        print()
        nombre_producto = input("Ingrese el nombre del producto:          ")
        cantidad_producto = int(input("Ingrese la cantidad del producto:        "))
        precio_producto = int(input("Ingrese el precio unitario del producto: "))


        diccionario_produtos = {
            "nombre": nombre_producto,
            "cantidad": cantidad_producto,
            "precio": precio_producto
        }

        productos.append(diccionario_produtos)
        agregar = input("Desea ingresar otra venta? si/no: ")


    #resumen de venta
    print ("="*60)
    print ("                RESUMEN DE VENTAS DIARIAS")

    total_a = []
    for venta in productos:
        print("Producto:                     ", venta["nombre"])
        print("Precio por unidad:             $", venta["precio"])
        print("Cantidad vendida hoy:           ", venta["cantidad"], "unidades")

        a = (venta["cantidad"]* venta["precio"])
        print("Subtotal vendido por producto: $",a)

        print("="*60)
        
        total_a.append(a)   

    # total recaudado en el dia
    print ("               TOTAL RECAUDADO HOY: $" ,sum(total_a))
    print("="*60)

registro_de_ventas()