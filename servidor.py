#!/usr/bin/env python3
#librerias a usar
import socket
import random #Genera numeros aleatorios
import os #Para "pulse una tecla para continuar"
import sys #para salir del programa
import time #Para calculae el tiempo


HOST = input("\nIngrese la dirección IP:\t")  # Direccion de la interfaz de loopback estándar (localhost)
PORT = 65432  # Puerto que usa el cliente  (los puertos sin provilegios son > 1023)
buffer_size = 1024

#Declaracion de variables
partida = ''


#Funcion que imprime tablero
def imprimirTablero(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()
    print()

# tableroServidor


#Mis funciones a emplear
def generarTableroServidor(n, dificultad, minas):
    minasArregloPosiciones = ""
    if dificultad == 'f':
        tableroCabecera = [" ","A","B","C","D","E","F","G","H","I"]
        tableroColumna = [" ", 0,1,2,3,4,5,6,7,8]
    else:
        tableroCabecera = [" "," A","B","C","D","E","F","G","H","I", "J", "K", "L", "M","N", "O", "P"]
        tableroColumna = [" ", " 0"," 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9",10,11,12,13,14,15]
    tableroServidor = [[ "*" for x in range(n+1)] for x in range(n+1)]
    for i in range(1):
        for j in range(len(tableroServidor[i])):
            if tableroServidor[i][j] == "*":
                tableroServidor[i][j] = tableroCabecera[j]
                tableroServidor[j][i] = tableroColumna[j]
    #Vamos a insertar las minas de forma aleatoria
    #También las guardamos en una tupla
    incremento = 0
    while incremento < minas:
        posX = random.randint(2, n)
        # print("El valor posX: ", posX)
        posY = random.randint(2, n)
        # print("El valor posY: ", posX)
        if tableroServidor[posX][posY] == "*":
            # print("cumple")
            tableroServidor[posX][posY] = "M"
            coordenadas = str(posX) + "," +str(posY) + "|"
            minasArregloPosiciones = minasArregloPosiciones + coordenadas
            incremento+=1
    return (tableroServidor, minasArregloPosiciones)

def verificarToqueMina(tableroServidor, CooX, CooY):
    #Buscamos el numero de la letra para obtener la coordenada de la mina
    for i in range(1):
        for j in range (len(tableroServidor[i])):
            if tableroServidor[i][j].strip() == CooY:
                CooY = j
    if tableroServidor[CooX+1][CooY] == "M":
        print(" *** El cliente ha tocado una mina :( *** ")
        return 1
    else:
        return 0



#Aqui empieza la comunicacion con el servidor y el cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen(1)
    mensajeInicial = """
    =======================================================
    ***************** Aplicación Servidor *****************
    =======================================================
    """
    print(mensajeInicial)
    print("Servidor en espera de una conexión...")
    Client_conn, Client_addr = TCPServerSocket.accept()
    with Client_conn:
        print("\nEl servidor se ha conectado con: ", Client_addr , "\n")
        #Solicito el nivel de dificultad
        mensajeEnviar = "Que nivel de dificultad desea? (f: facil / d:dificil)"
        Client_conn.send(mensajeEnviar.encode(encoding="ascii", errors="ignore"))
        mensajeRecibido = Client_conn.recv(buffer_size)
        print("Cliente: ", mensajeRecibido.decode(encoding="ascii", errors="ignore"))
        #Recobo el nivel de la dificultad
        
        mensajeRecibido = Client_conn.recv(buffer_size)
        verificarDificultad = mensajeRecibido.decode(encoding="ascii", errors="ignore")
        # print("Verificamos: ", verificarDificultad, "\nEs del tipo: ", type(verificarDificultad))
        if verificarDificultad == 'f':
            print("Solicito una partida facil")
            partida = 'f'
            #genero el tablero
            tableroServidor, minasArregloPosiciones = generarTableroServidor(9, verificarDificultad, 10)
            imprimirTablero(tableroServidor)
        else:
            print("Solicito una partida dificil")
            partida = 'd'
            #genero el tablero
            tableroServidor, minasArregloPosiciones = generarTableroServidor(16, verificarDificultad, 40)
            imprimirTablero(tableroServidor)
            
        print("veamos el arreglo de las posiciones de las minas: ", minasArregloPosiciones)
        mensajeEnviar = "Buena suerte en su partida..."
        Client_conn.send(mensajeEnviar.encode(encoding="ascii", errors="ignore"))
        mensajeRecibido = Client_conn.recv(buffer_size)
        print("Cliente: ", mensajeRecibido.decode(encoding="ascii", errors="ignore"))
        mensajeRecibido = Client_conn.recv(buffer_size)
        print("Cliente: ", mensajeRecibido.decode(encoding="ascii", errors="ignore"))
        # print("stop")
        # wait_time = 2
        # time.sleep(wait_time)
        #Aqui empieza a pedir coordenadas
        numeroPaso = 0
        while True:   
            inicio = time.time() #Empiezo a medir el tiempo del juego  
            print("Server: Le Solicitamos coordenadas al cliente")
            mensajeEnviar = "Ingresa las coordenadas: (Numero,Letra)\t"
            Client_conn.send(mensajeEnviar.encode(encoding="ascii", errors="ignore"))
            mensajeRecibido = Client_conn.recv(buffer_size)
            print("Cliente: ", mensajeRecibido.decode(encoding="ascii", errors="ignore"))
            a = mensajeRecibido.decode(encoding="ascii", errors="ignore")
            if numeroPaso >0:
                print("La coordenada Ingresada: ", a)
                # print(type(a))
                # print(f"{int(a[0])} {a[1]} {(a[2]).upper()}")
                respVTM = verificarToqueMina(tableroServidor, int(a[0]), a[2].upper())
                if respVTM == 1:
                    # print("Toco la mina")
                    mensajeAEnviar = "True"
                    Client_conn.send(mensajeAEnviar.encode(encoding="ascii", errors="ignore"))
                    print("Al continuar se saldrá del programa")
                    fin = time.time() #finaliza el tiempo 
                    duracionJuego = fin-inicio
                    #Envio la posicion de las minas para mostrarlas del lado del cliente
                    mensajeAEnviar = minasArregloPosiciones
                    Client_conn.send(mensajeAEnviar.encode(encoding="ascii", errors="ignore"))
                    # print("La duracuión del juego fue: ", duracionJuego) # imprimo el tiempo que tardó
                    mensajeAEnviar = "La duracion del juego fue de: " + str(round(duracionJuego, 2))
                    print(mensajeAEnviar)
                    Client_conn.send(mensajeAEnviar.encode(encoding="ascii", errors="ignore"))
                    os.system("Pause")
                    # sys.exit()
                    break;
                else:
                    print("No ha tocado mina")
            numeroPaso+=1
    # Client_conn.close()        

#cd downloads/"redes 2"/practicas/Practica1