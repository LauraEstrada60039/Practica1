#Aquí vamos a tener las librerías
import datetime #Para obtener fechas su link es: https://docs.python.org/es/3/library/datetime.html
import random #Genera numeros aleatorios

# def SolicitarCoordenada():
#     print("vamos a solicitar coordenas")

# GENERO UNA FUNCION QUE CALCULE LOS DIAS QUE HE VIVIDO
def CuantosDiasHeVivido():
    #Anio bisiesto es cuando:
    # El año acaba en dos ceros
    # Se repirte cada 4 años
    # Es uniformemente divisible por 4 pero no por 100, aunque si es divisible por 100 se hace lo siguiente:
    # Es divisible entre 100, pero también por 400 -> entonces es bisiesto
    # Pero con Python es más fácil el asunto:
    # Necesitamos la fecha de nacimiento
    fecha = input("> Ingrese su fecha de nacimiento(AAAA/MM/DD):\t") #Solicito el día de nacimiento
    fecha = datetime.datetime.strptime(fecha, '%Y/%m/%d').date() #Le damos el formarto de fecha
    # print("La fecha: ", fecha)
    # Calculamos a la fecha que necesitamos
    #Si queremos al día de hoy se usa: datetime.date.today();
    fechaEstablecida = datetime.date(2023, 3, 8) #Asigno la fecha hasta la que hay que calcular los dias vividos
    #Obtenemos el numero de días vividos
    tiempoVividoDias = (fechaEstablecida-fecha).days #fecha establecida es mayor que cuando nací 1999 < 2023
    print("\nUsted ha vivido: ",tiempoVividoDias, " días.\n")
    
#GENERO UNA FUNCION QUE CALCULE EL MODULO DE UNA CANTIDAD
def moduloCantidad(cantidad):
    moduloCantidad = cantidad%3
    print(f"El módulo 3 de {cantidad} es: {moduloCantidad}")

def imprimirTablero(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()
    print()

def generarTableroCliente(n, dificultad):
    if dificultad == 'f':
        tableroCabecera = [" ","A","B","C","D","E","F","G","H","I"]
        tableroColumna = [" ", 0,1,2,3,4,5,6,7,8]
    else:
        tableroCabecera = [" "," A","B","C","D","E","F","G","H","I", "J", "K", "L", "M","N", "O", "P"]
        tableroColumna = [" ", " 0"," 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9",10,11,12,13,14,15]
    tableroCliente = [[ "*" for x in range(n+1)] for x in range(n+1)]
    for i in range(1):
        for j in range(len(tableroCliente[i])):
            if tableroCliente[i][j] == "*":
                tableroCliente[i][j] = tableroCabecera[j]
                tableroCliente[j][i] = tableroColumna[j]
    return tableroCliente


def generarTableroServidor(n, dificultad, minas):
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
    incremento = 0
    while incremento < minas:
        posX = random.randint(2, n)
        # print("El valor posX: ", posX)
        posY = random.randint(2, n)
        # print("El valor posY: ", posX)
        if tableroServidor[posX][posY] == "*":
            # print("cumple")
            tableroServidor[posX][posY] = "M"
            incremento+=1
    return tableroServidor

def actualizarTableroCliente(tableroCliente, CooX, CooY, toque):
    print("Actualizo tablero del cliente")
    if toque == 0:
        tableroCliente[CooX+1][CooY] = "-"
    else:
        tableroCliente[CooX+1][CooY] = "X"
    imprimirTablero(tableroCliente)

def verificarToqueMina(tableroServidor, tableroCliente):
    respuesta = 0
    print(" == Ingrese primero un numero y despues la letra ==")
    toqueMina = 0
    while toqueMina!=1:
        pedirCoordenadasX = int(input("> Ingrese la coordenada X:\t"))
        tempPedirCoordenadasY = input("> Ingrese la letra:\t")
        tempPedirCoordenadasY = tempPedirCoordenadasY.upper()
        #Buscamos el numero de la letra para obtener la coordenada de la mina
        for i in range(1):
            for j in range (len(tableroServidor[i])):
                # print("Con espacio:",tempPedirCoordenadasY)
                # print("Sin espacio segun:",tempPedirCoordenadasY.strip())
                if tableroServidor[i][j].strip() == tempPedirCoordenadasY:
                    pedirCoordenadasY = j
                    # print("El valor de j es: ", j)
        # pedirCoordenadasY = int(input("Ingrese la coordenada Y:\t"))
        #Verifica si existe la mina en la coordenada
        # print("Coordenada es: (", pedirCoordenadasX, ",", pedirCoordenadasY, ")")
        # print("Lo que nos arroja(-1) es: ", tableroServidor[pedirCoordenadasX-1][pedirCoordenadasY-1])
        # print("Lo que nos arroja(+1) es: ", tableroServidor[pedirCoordenadasX+1][pedirCoordenadasY+1])
        # print("Lo que nos arroja es: ", tableroServidor[pedirCoordenadasX+1][pedirCoordenadasY])
        # print(tableroServidor[pedirCoordenadasX+1])
        # print(tableroServidor[pedirCoordenadasY+1])
        # imprimirTablero(tableroCliente)
        if tableroServidor[pedirCoordenadasX+1][pedirCoordenadasY] == "M":
            print(" *** Has tocado una mina :( *** ")
            toqueMina = 1
            actualizarTableroCliente(tableroCliente, pedirCoordenadasX, pedirCoordenadasY, toqueMina)
            return respuesta
        else:
            toqueMina = 0
            # print("El juego continúa...")
            actualizarTableroCliente(tableroCliente, pedirCoordenadasX, pedirCoordenadasY, toqueMina)

#GENERO UNA FUNCION PARA EL MENU GENERAL
def main():
    inicio = """
    =============================================================================================================
     *************************   Bienvenido al programa que calcula tus días de vida   *************************
    =============================================================================================================
    
    Menú: 
    1. Calcular días vividos
    2. Calcular el módulo 3 de una cantidad
    3. Jugar Buscaminas
    """
    print(inicio)
    condicion = input("> Ingrese una opción del menú: ")
    condicion = int(condicion)
    if condicion == 1:
        print("\nVamos a calcular los días que ha vivido")
        CuantosDiasHeVivido()
    elif condicion == 2:
        print("\nVamos a calcular el módulo 3 de una cantidad")
        moduloCantidad(int(input("> Ingrese la cantidad:\t")))
    elif condicion == 3:
        print("Vamos a jugar Buscaminas")
        #Solicitamos la dificultad del ejercicio
        dificultad = input("> Ingrese la dificultad del juego (f->Fácil/d->Difícil)")
        if(dificultad.lower() == 'f'):
            print("Escogió la dificultad de fácil")
            #Genero el tablero
            tableroCliente = generarTableroCliente(9, dificultad)   

            #CLIENTE
            print("Vista del Cliente: \n")
            imprimirTablero(tableroCliente)

            #SERVIDOR
            print("Vista del Servidor: \n")
            tableroServidor = generarTableroServidor(9, dificultad, 10)
            imprimirTablero(tableroServidor)
            resp = verificarToqueMina(tableroServidor, tableroCliente)
            print("La respuesta es: ", resp)
            if resp == 1:
                print("Fin del juego")
        else:
            print("Escogió la dificultad de difícil")
            #Genero el tablero

            #CLIENTE
            #Genero la tabla del cliente
            print("\nVista del cliente")
            tableroCliente = generarTableroCliente(16, dificultad)
            imprimirTablero(tableroCliente)

            #SERVIDOR
            #Genero la tabla del servidor
            print("\n\nVista del servidor")
            tableroServidor = generarTableroServidor(16, dificultad, 40)
            imprimirTablero(tableroServidor)
            resp = verificarToqueMina(tableroServidor, tableroCliente)
            print("La respuesta es: ", resp)
            if resp == 1:
                print("Fin del juego")
    else:
        print("No se encontró la opción que busca")

#CON LAS SIGUIENTES LINEAS LLAMAMOS LA FUNCION PRINCIPAL DE MENU
if __name__ == "__main__":
    opcUsuario = 's'
    while opcUsuario == 's':
        main()
        opcUsuario = input("> ¿Desea repetir el programa?(s/n)\t")
        opcUsuario.lower()
        while (opcUsuario != 's') and (opcUsuario != 'n'):
            print("Ingrese: s ó n")
            opcUsuario = input("> ¿Desea repetir el programa?(s/n)\t")
            opcUsuario.lower()
    print("Fin del programa")
    print("Adiós")

