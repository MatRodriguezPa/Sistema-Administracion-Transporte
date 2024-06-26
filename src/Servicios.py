
from datetime import datetime

class ClassServicios:

    def __init__(self):
        codigoServicio = None
        nombre = None
        origen = None
        destino = None
        precioVenta = None
        horaSalida = None
        cantidadMaxPuestos = None
        cantidadMaxKilos = None

    #se crea la tabla servicios si no existe
    def crearTablaServicios(self,con):
        cursorObj=con.cursor()
        crear='''CREATE TABLE IF NOT EXISTS Servicios(
                codigoServicio integer NOT NULL,
                nombre text NOT NULL,
                origen text NOT NULL,
                destino text NOT NULL,
                precioVenta integer NOT NULL,
                horaSalida date NOT NULL,
                cantidadMaxPuestos integer NOT NULL,
                cantidadMaxKilos integer NOT NULL,
                PRIMARY KEY(codigoServicio)
                )
                '''
        cursorObj.execute(crear)
        con.commit()

    #Escribir un servicio que sera insertado luego
    def leerServicio(self):
        codigoServicio=input("Código del servicio: ").ljust(10)
        nombre=input("Nombre: ")
        origen=input("Ciudad de Origen: ")
        destino=input("Ciudad de destino: ")
        precioVenta=input("Precio de venta: ")

        #Comprueba si esta en el formato correcto la hora ingresada
        while True:
            hora = input("Hora de salida (HH:MM:SS): ")
            fecha = datetime.now().strftime("%Y:%m:%d:")
            try:
                fechaCompleta = fecha + hora
                horaSalida = datetime.strptime(fechaCompleta, "%Y:%m:%d:%H:%M:%S")
                print("Fecha y hora de salida:", horaSalida)
                break
            except ValueError:
                print("Error: La hora de salida debe estar en el formato HH:MM:SS.")

        cantidadMaxPuestos=input("Cantidad de puestos: ")
        cantidadMaxKilos=input("Peso que puede llevar: ")

        servicio=(codigoServicio,nombre,origen,destino,precioVenta,horaSalida,cantidadMaxPuestos,cantidadMaxKilos)
        print("La tupla servicio es :",servicio)
        return servicio

    #inserta un registro vacio en latabla
    def insertarTablaServicios(self,con,miServicio):
        cursorObj=con.cursor()
        insertar="INSERT INTO servicios VALUES(?,?,?,?,?,?,?,?)"
        print("Insertar = ",insertar)
        cursorObj.execute(insertar,miServicio)
        con.commit()

    #insertar un registro en la trabla servicios # no utilizado
    def insertarTablaServicios1(self,con):
        codigoServicio=input("Código del servicio: ")
        cursorObj=con.cursor()
        insertar='INSERT INTO servicios VALUES('+codigoServicio+', "REMESA","CHIA","COTA","100","1900-01-01 12:15:20","10","200")'
        print("Accion ejecutada = ",insertar)
        cursorObj.execute(insertar)
        con.commit()
    
    #consultar todos los registros de la tabla servicios
    def consultarTablaServicios(self,con):
        cursorObj=con.cursor()
        consultar='SELECT codigoServicio, nombre, origen, destino, precioVenta FROM servicios'
        print("Consulta construida = ",consultar)
        cursorObj.execute(consultar)
        filas=cursorObj.fetchall()
        for row in filas:
            cs=row[0]
            nom=row[1]
            ori=row[2]
            des=row[3]
            pv=row[4]
            print("La información del servicio es: ",cs,nom,ori,des,pv)

    #PRUEBA retorna un dato especifico de un registro
    def consultarTablaServicios0(self,con):
        cursorObj=con.cursor()
        dato = input("Dato a consultar: ")
        codigoServicio = input("Código del dato: ")
        consultar = 'SELECT '+dato+' FROM servicios WHERE codigoServicio="'+codigoServicio+'"'
        cursorObj.execute(consultar)
        resultado=cursorObj.fetchall()
        return resultado

    #consultar fecha y hora de salida
    def consultarTablaServicios1(self,con):
        cursorObj=con.cursor()
        consultar='''SELECT codigoServicio,
                            nombre,
                            origen,
                            destino,
                            precioVenta,
                            horaSalida,
                            date(horaSalida),
                            time(horaSalida)
                    FROM servicios'''
        print("Consulta construida = ",consultar)
        cursorObj.execute(consultar)
        filas=cursorObj.fetchall()
        print("El tipo de dato de filas es: ",type(filas))
        for row in filas:
            cs=row[0]
            nom=row[1]
            ori=row[2]
            des=row[3]
            fecha=row[5]
            date=row[6]
            time=row[7]
            print("La información del servicio es: ",cs,nom,ori,des,fecha,"|",date,"|",time)

    #consultar puestos máximos y peso máximos 
    def consultarTablaServicios2(self,con):
        cursorObj=con.cursor()
        consultar='''SELECT * FROM servicios'''
        print("Consulta construida = ",consultar)
        cursorObj.execute(consultar)
        filas=cursorObj.fetchall()
        print("El tipo de dato de filas es: ",type(filas))
        for row in filas:
            cs=row[0]
            nom=row[1]
            ori=row[2]
            puestos=row[6]
            kilos=row[7]
            print("La información del servicio es: ",cs,nom,ori,"|",puestos,"|",kilos)

    #consultar cuantos registros hay en la base de datos
    def consultarTablaServicios3(self,con):
        cursorObj=con.cursor()
        consultar='''SELECT COUNT(*) FROM servicios'''
        print("Consulta construida = ",consultar)
        cursorObj.execute(consultar)
        filas=cursorObj.fetchall()
        print("El tipo de dato de filas es: ",type(filas))
        for row in filas:
            cuenta=row[0]
            print("La cantidad de registros en la base de datos es: ",cuenta)

    #consultar suma de los precios de las ventas
    def consultarTablaServicios4(self,con):
        cursorObj=con.cursor()
        consultar='''SELECT sum(precioVenta) FROM servicios'''
        print("Consulta construida = ",consultar)
        cursorObj.execute(consultar)
        filas=cursorObj.fetchall()
        print("El tipo de dato de filas es: ",type(filas))
        for row in filas:
            suma=row[0]
            print("La sumatoria de los precios de venta es: ",suma)

    #consultar registro por nombre
    def consultarTablaServicios6(self,con):
        origen=input("Ciudad de origen: ")
        cursorObj=con.cursor()
        consultar='SELECT * FROM servicios WHERE origen="'+origen+'"'
        print("Consulta construida = ",consultar)
        cursorObj.execute(consultar)
        filas=cursorObj.fetchall()
        print("El tipo de dato de filas es: ",type(filas))
        for row in filas:
            cs=row[0]
            nom=row[1]
            ori=row[2]
            des=row[3]
            pv=row[4]
            fecha=row[5]
            puestos=row[6]
            kilos=row[7]
            print("La información del servicio es: ",cs,nom,ori,des,pv,fecha,"|",puestos,"|",kilos)

    #consultar registros por letra
    def consultarTablaServicios7(self,con):
        cursorObj=con.cursor()
        origen=input("Primera letra de Ciudad de origen: ")
        consultar='SELECT * FROM servicios WHERE origen like "'+origen+'%"'
        print("Consulta construida = ",consultar)
        cursorObj.execute(consultar)
        filas=cursorObj.fetchall()
        print("El tipo de dato de filas es: ",type(filas))
        for row in filas:
            cs=row[0]
            nom=row[1]
            ori=row[2]
            des=row[3]
            pv=row[4]
            fecha=row[5]
            puestos=row[6]
            kilos=row[7]
            print("La información del servicio es: ",cs,nom,ori,des,pv,fecha,"|",puestos,"|",kilos)

    #actualiza el nombre de un registro de la trabla de servicios
    def actualizarTablaServicios(self,con):
        codigoServicio=input("Codigo del servicio a actualizar: ")
        nombre=input("Dato actualizado: ")
        cursorObj=con.cursor()
        actualizar='UPDATE servicios SET nombre="'+nombre+'" WHERE codigoServicio='+codigoServicio
        print("Actualizar = ",actualizar)
        cursorObj.execute(actualizar)
        con.commit()

    #actualiza el dato de un registro de la trabla de servicios
    def actualizarTablaServicios1(self,con):
        codigoServicio=input("Codigo del servicio a actualizar: ")
        origen=input("Dato actualizado: ")
        cursorObj=con.cursor()
        actualizar='UPDATE servicios SET origen="'+origen+'" WHERE codigoServicio='+codigoServicio
        print("Actualizar = ",actualizar)
        cursorObj.execute(actualizar)
        con.commit()

    #actualiza el dato de un registro de la trabla de servicios
    def actualizarTablaServicios2(self,con):
        codigoServicio=input("Codigo del servicio a actualizar: ")
        destino=input("Dato actualizado: ")
        cursorObj=con.cursor()
        actualizar='UPDATE servicios SET destino="'+destino+'" WHERE codigoServicio='+codigoServicio
        print("Actualizar = ",actualizar)
        cursorObj.execute(actualizar)
        con.commit()

    #actualiza el dato de un registro de la trabla de servicios
    def actualizarTablaServicios3(self,con):
        codigoServicio=input("Codigo del servicio a actualizar: ")
        precioVenta=input("Dato actualizado: ")
        cursorObj=con.cursor()
        actualizar='UPDATE servicios SET precioVenta="'+precioVenta+'" WHERE codigoServicio='+codigoServicio
        print("Actualizar = ",actualizar)
        cursorObj.execute(actualizar)
        con.commit()

    #actualiza el dato de un registro de la trabla de servicios
    def actualizarTablaServicios4(self,con):
        codigoServicio=input("Codigo del servicio a actualizar: ")
        horaSalida=input("Dato actualizado: ")
        cursorObj=con.cursor()
        actualizar='UPDATE servicios SET horaSalida="'+horaSalida+'" WHERE codigoServicio='+codigoServicio
        print("Actualizar = ",actualizar)
        cursorObj.execute(actualizar)
        con.commit()

    #actualiza el dato de un registro de la trabla de servicios
    def actualizarTablaServicios5(self,con):
        codigoServicio=input("Codigo del servicio a actualizar: ")
        cantidadMaxPuestos=input("Dato actualizado: ")
        cursorObj=con.cursor()
        actualizar='UPDATE servicios SET cantidadMaxPuestos="'+cantidadMaxPuestos+'" WHERE codigoServicio='+codigoServicio
        print("Actualizar = ",actualizar)
        cursorObj.execute(actualizar)
        con.commit()

    #actualiza el dato de un registro de la trabla de servicios
    def actualizarTablaServicios6(self,con):
        codigoServicio=input("Codigo del servicio a actualizar: ")
        cantidadMaxKilos=input("Dato actualizado: ")
        cursorObj=con.cursor()
        actualizar='UPDATE servicios SET cantidadMaxKilos="'+cantidadMaxKilos+'" WHERE codigoServicio='+codigoServicio
        print("Actualizar = ",actualizar)
        cursorObj.execute(actualizar)
        con.commit()

    #borra un registro
    def borrarRegistroTablaServicios(self,con):
        codigoServicio=input("Codigo del servicio a borrar: ")
        cursorObj=con.cursor()
        borrar='DELETE FROM servicios WHERE codigoServicio='+codigoServicio
        print("Sentencia = ",borrar)
        cursorObj.execute(borrar)
        con.commit()

    #borra toda la tabla
    def borrarTablaServicios(self,con):
        cursorObj=con.cursor()
        borrar='DROP TABLE servicios'
        print("Sentencia = ",borrar)
        cursorObj.execute(borrar)
        con.commit()
