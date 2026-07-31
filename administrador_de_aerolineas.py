ids = []
aerolineas = []
numeros_vuelo = []
aviones = []
origenes = []
destinos = []
fechas = []
horas_salida = []
horas_llegada = []
estados = []
observaciones = []
#---------------------------------------------#
#--|menu_principal_administrador_aerolineas|--#
#---------------------------------------------#
while True:
    print("menu principal administrador de aerolineas")
    print("1) crear vuelo")
    print("2) editar vuelo")
    print("3) eliminar vuelo")
    print("4) buscar vuelo")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------#
    #--|crear_vuelo|--#
    #-----------------#
    if opcion == "1":
        if len(ids) == 0:
            id_vuelo = 1
        else:
            id_vuelo = ids[-1] + 1
        aerolinea = input("nombre de la aerolínea: ")
        numero_vuelo = input("número de vuelo: ")
        avion = input("modelo del avión: ")
        origen = input("ciudad de origen: ")
        destino = input("ciudad de destino: ")
        fecha = input("fecha del vuelo: ")
        hora_salida = input("hora de salida: ")
        hora_llegada = input("hora de llegada: ")
        estado = input("estado del vuelo: ")
        observacion = input("observación: ")
        ids.append(id_vuelo)
        aerolineas.append(aerolinea)
        numeros_vuelo.append(numero_vuelo)
        aviones.append(avion)
        origenes.append(origen)
        destinos.append(destino)
        fechas.append(fecha)
        horas_salida.append(hora_salida)
        horas_llegada.append(hora_llegada)
        estados.append(estado)
        observaciones.append(observacion)
        print("vuelo registrado correctamente.")
        print("id:", id_vuelo)
    #------------------#
    #--|editar_vuelo|--#
    #------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar vuelo")
            for i in range(len(ids)):
                print(f"{ids[i]} | {aerolineas[i]} | {numeros_vuelo[i]} | {aviones[i]} | {origenes[i]} | {destinos[i]} | {fechas[i]} | {horas_salida[i]} | {horas_llegada[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {aerolineas[posicion]} | {numeros_vuelo[posicion]} | {aviones[posicion]} | {origenes[posicion]} | {destinos[posicion]} | {fechas[posicion]} | {horas_salida[posicion]} | {horas_llegada[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                aerolineas[posicion] = input("nueva aerolínea: ")
                numeros_vuelo[posicion] = input("nuevo número de vuelo: ")
                aviones[posicion] = input("nuevo avión: ")
                origenes[posicion] = input("nuevo origen: ")
                destinos[posicion] = input("nuevo destino: ")
                fechas[posicion] = input("nueva fecha: ")
                horas_salida[posicion] = input("nueva hora de salida: ")
                horas_llegada[posicion] = input("nueva hora de llegada: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|eliminar_vuelo|--#
    #--------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar vuelo")
            for i in range(len(ids)):
                print(f"{ids[i]} | {aerolineas[i]} | {numeros_vuelo[i]} | {aviones[i]} | {origenes[i]} | {destinos[i]} | {fechas[i]} | {horas_salida[i]} | {horas_llegada[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {aerolineas[posicion]} | {numeros_vuelo[posicion]} | {aviones[posicion]} | {origenes[posicion]} | {destinos[posicion]} | {fechas[posicion]} | {horas_salida[posicion]} | {horas_llegada[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    aerolineas.pop(posicion)
                    numeros_vuelo.pop(posicion)
                    aviones.pop(posicion)
                    origenes.pop(posicion)
                    destinos.pop(posicion)
                    fechas.pop(posicion)
                    horas_salida.pop(posicion)
                    horas_llegada.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #------------------#
    #--|buscar_vuelo|--#
    #------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar vuelo")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {aerolineas[posicion]} | {numeros_vuelo[posicion]} | {aviones[posicion]} | {origenes[posicion]} | {destinos[posicion]} | {fechas[posicion]} | {horas_salida[posicion]} | {horas_llegada[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            programados = 0
            en_vuelo = 0
            aterrizados = 0
            cancelados = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {aerolineas[i]} | {numeros_vuelo[i]} | {aviones[i]} | {origenes[i]} | {destinos[i]} | {fechas[i]} | {horas_salida[i]} | {horas_llegada[i]} | {estados[i]} | {observaciones[i]}")
                if estados[i].lower() == "programado":
                    programados += 1
                elif estados[i].lower() == "en vuelo":
                    en_vuelo += 1
                elif estados[i].lower() == "aterrizado":
                    aterrizados += 1
                elif estados[i].lower() == "cancelado":
                    cancelados += 1
            print("estadísticas administrador de aerolíneas")
            print("cantidad de registros:", len(ids))
            print("vuelos programados:", programados)
            print("vuelos en vuelo:", en_vuelo)
            print("vuelos aterrizados:", aterrizados)
            print("vuelos cancelados:", cancelados)
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el programa.")
        break
    else:
        print("opción inválida.")