import sys # Para cerrar el programa desde la interfáz

class menu:
    def menuPrincipal(self):
        return input('''
             ____        _      _____  
            / ___|      / \    |_   _| 
           | (___      / _ \     | |   
            \___ \    / /_\ \    | |   
            ____) |  / _____ \   | |   
           |_____/  /_/     \_\  |_|   

        SISTEMA DE ADMINISTRACIÓN DE TRANSPORTES 
                    LA NACIONAL

        MENU PRINCIPAL
        1. Modulo de Ventas
        2. Modulo de gestión de Clientes
        3. Modulo de gestión de Servicios
        4. Cerrar programa

        Seleccione una opción: ''')

    def menuVentas(self,miConexion, objServicios, objVentas, objClientes):
        salirVentas = False
        while not salirVentas:
            opcionVentas = input('''
            MODULO VENTAS
            1. Vender un servicio.
            2. Consultar todas las ventas.
            3. Consultar un dato de una venta.
            4. Consultar cuantos servicios hay en total. 
            5. Consultar suma de los precios de venta de los servicios.
            6. Consultar registro por nombre.
            7. Consultar registro por letra inicial.
            8. Borrar venta
            9. Imprimir factura.
            10. Volver.

            Seleccione una opción:  ''')

            if opcionVentas == '1':
                ventaConstruida=objVentas.leerVenta()
                while True:
                    
                    # Preguntar si es de pasajeros o encomienda
                    while True:
                        opcionTipo=input('''
                            1.Pasajero
                            2.Encomienda
                            Selecione el tipo de servicio: 
                            ''')
                        if opcionTipo=="1":
                            cantidadMaxDato = "cantidadMaxPuestos"
                        elif opcionTipo=="2":
                            cantidadMaxDato = "cantidadMaxKilos"
                        break

                    #si el número de identificación no existe, no lo acepta
                    while True:
                        existeCliente = objClientes.consultarTablaClientes2(con)
                        if existeCliente[0]== ventaConstruida[0]:
                            break
                        else:
                            print("Intente otra otra vez")

                     #si cantidadMaxima (Puestos o Kilos) > cantidadVendidaTotal+cantidadVender, no lo acepta.
                    while True:
                        cantidadVender=input("Cantidad a vender: ")
                        try:
                            #consultar el dato de la capacidad máxima puestosMaximos / kilosMaximos del registro
                            cantidadMaxima=objServicios.consultarTablaServicios0(cantidadMaxDato)
                            #consular lo que ya se ha vendido
                            cantidadVendidaTotal=objVentas.ConsultarCantidadVendidaTotal(con,objServicios)
                            
                            if cantidadMaxima == cantidadVendidaTotal:
                                print("No hay más puestos disponibles, intente con otro servicio.")
                            if (cantidadMaxima>cantidadVendidaTotal+cantidadVender):
                                break
                            else:
                                print("Intente otra vez, puestos disponibles: "+cantidadMaxima-cantidadVendidaTotal)
                        except:print("Puestos disponibles exedidos, ingrese una cantidad menor.")
                    break
                objVentas.añadirServicioAVender(miConexion,ventaConstruida)
                while True:
                    opcionFactura = input("¿Imprimir factura? (S/N): ")
                    if opcionFactura.upper() == "S":
                        objVentas.imprimirFactura()
                    break
            elif opcionVentas == '2':       
                confirmacion = input(f"¿Estás seguro de que deseas borrar el registro? (s/n): ").lower()
                if confirmacion != 's':
                    print("Operación cancelada.")
                    return
                objVentas.borrarRegistroTablaVentas()
            elif opcionVentas == '3':     
                objVentas.consultarTablaVentas()  
                objVentas.imprimirFactura()
            elif opcionVentas == '4':
                salirVentas = True
            elif opcionVentas == '5':
                salirVentas = True
            elif opcionVentas == '6':
                salirVentas = True
            elif opcionVentas == '7':
                salirVentas = True
            elif opcionVentas == '8':
                salirVentas = True
            elif opcionVentas == '9':
                salirVentas = True
            elif opcionVentas == '10':
                salirVentas = True
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def menuClientes(self, miConexion, objClientes):
        salirClientes = False
        while not salirClientes:
            opcionClientes = input('''
            MODULO CLIENTES
            1. Inserta un nuevo cliente.
            2. Consultar todos los clientes.
            3. Consultar un dato de un cliente.
            4. Consultar cuantos servicios hay en total. 
            5. Consultar registro por nombre.
            6. Consultar registro por letra inicial del nombre.
            7. Actualizar dato de un cliente.
            8. Borra un cliente.
            9. Borrar toda la tabla de clientes.
            10. Volver.

            Seleccione una opción:  ''')

            if opcionClientes == '1':
                clienteCreado = objClientes.leerCliente()
                objClientes.insertarTablaClientes(miConexion,clienteCreado)

            elif opcionClientes == '2':
                objClientes.consultarTablaClientes(miConexion)

            elif opcionClientes == '3':
                dato = input("Dato a consultar: ")
                noIdentificacionCliente = input("Número de identificación del cliente: ")
                objClientes.consultarTablaClientes1(miConexion,dato,noIdentificacionCliente)

            elif opcionClientes == '4':
                objClientes.consultarTablaSClientes2(miConexion)

            elif opcionClientes == '5':
                datoConsulta=input("Busqueda: ")
                objClientes.consultarTablaClientes3(miConexion,datoConsulta)

            elif opcionClientes == '6':
                datoConsulta = input("Búsqueda: ")
                objClientes.consultarTablaClientes4(miConexion,datoConsulta)

            elif opcionClientes == '7':
                objClientes.actualizarTablaServicios(miConexion)

            elif opcionClientes == '8':
                noIdentificacionCliente = input("Identificación del cliente a borrar: ")
                confirmacion = input(f"¿Estás seguro de que deseas borrar el cliente {noIdentificacionCliente}? (s/n): ").lower()
                
                if confirmacion != 's':
                    print("Operación cancelada.")
                else:
                    objClientes.borrarRegistroTablaClientes(miConexion,objClientes,noIdentificacionCliente)

            elif opcionClientes == '9':
                confirmacion = input("¿Estás seguro de que deseas borrar toda la tabla 'Clientes'? (s/n): ").lower()
                if confirmacion != 's':
                    print("Operación cancelada.")
                else:
                    objClientes.borrarTablaClientes(miConexion)

            elif opcionClientes == '10':
                salirClientes = True
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def menuServicios(self,miConexion, objServicios):
        salirServicios = False

        while not salirServicios:
            opcionServicios = input('''
            MODULO SERVICIOS
            1. Inserta un servicio
            2. Consultar todos los servicios.
            3. Consultar la fecha y hora de salida de todos los servicios.
            4. Consultar los puestos y peso máximos de todos los servicios.
            5. Consultar un dato de un Servicio.
            6. Consultar cuantos servicios hay en total. 
            7. Consultar suma de los precios de venta de los servicios.
            8. Consultar registro por nombre.
            9. Consultar registro por letra inicial del nombre.
            10. Actualizar un dato de un registro.
            11. Borra un registro de la tabla servicios.
            12. Borrar toda la tabla de servicios.
            13. Volver.

            Seleccione una opción: ''')

            if opcionServicios == '1':
                SercivioCreado = objServicios.leerServicio()
                objServicios.insertarServicio(miConexion, SercivioCreado)

            elif opcionServicios == '2':
                objServicios.consultarTablaServicios(miConexion)

            elif opcionServicios == '3':
                objServicios.consultarTablaServicios1(miConexion)

            elif opcionServicios == '4':
                objServicios.consultarTablaServicios2(miConexion)

            elif opcionServicios == '5':        
                dato = input("Dato a consultar: ")
                codigoServicio = input("Código del dato: ")
                objServicios.consultarTablaServicios3(miConexion,dato,codigoServicio) 
                
            elif opcionServicios == '6':
                objServicios.consultarTablaServicios4(miConexion)

            elif opcionServicios == '7':
                objServicios.consultarTablaServicios5(miConexion)

            elif opcionServicios == '8':
                datoConsulta=input("Busqueda: ")
                objServicios.consultarTablaServicios6(miConexion,datoConsulta)
                
            elif opcionServicios == '9':
                objServicios.consultarTablaServicios7(miConexion)
                
            elif opcionServicios == '10':
                objServicios.actualizarTablaServicios(miConexion)

            elif opcionServicios == '11':
                codigoServicio = input("Código del servicio a borrar: ")

                confirmacion = input(f"¿Estás seguro de que deseas borrar el registro {codigoServicio}? (s/n): ").lower()
                if confirmacion != 's':
                    print("Operación cancelada.")
                else:
                    objServicios.borrarRegistroTablaServicios(miConexion,objServicios)

            elif opcionServicios == '12':
                confirmacion = input("¿Estás seguro de que deseas borrar toda la tabla 'servicios'? (s/n): ").lower()
                if confirmacion != 's':
                    print("Operación cancelada.")
                else:
                    objServicios.borrarTablaServicios(miConexion)

            elif opcionServicios == '13':
                salirServicios = True
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def menu(self,miConexion,objServicios,objVentas,objClientes,objMenu):
        objServicios.crearTablaServicios(miConexion)
        objClientes.crearTablaClientes(miConexion)
        objVentas.crearTablaVentas(miConexion)

        salirPrincipal = False
        while not salirPrincipal:
            opcPrincipal = objMenu.menuPrincipal()
            if opcPrincipal == '1':
                objMenu.menuVentas(miConexion, objServicios, objVentas, objClientes)
            elif opcPrincipal == '2':
                objMenu.menuClientes(miConexion, objClientes)
            elif opcPrincipal == '3':
                objMenu.menuServicios(miConexion, objServicios)
            elif opcPrincipal == '4':
                sys.exit("Saliendo del programa.")
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")