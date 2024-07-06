import socket
import threading

# Puerto y servidor que debe escuchar
HOST = ""
PORT = 8050

# Creamos un socket servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)


def calculate(speed):#calcula el tiempo transcurrido en el puente

    distance = 1825 # distancia del puente en metros 

    speed =float(speed)

    speed = (speed * 1000) / (60*60) # transformacion km/h -> m/s

    time = distance / speed

    return (time / 60) # transformacion de s -> min


def direction(dir): #determina direccion del vehiculo
    if(dir.upper() == "BROOKLYN"):
        return "Manhattan a Brooklyn"
    else:
        return "Brooklyn a Manhattan"


def atender_cliente(cli_sock, addr):
    #contador
    cont = 1
    """
    Función para atender a un cliente en un hilo separado.

    Args:
        cli_sock (socket): Socket del cliente conectado.
        addr (tuple): Tupla con la dirección IP y el puerto del cliente.
    """
    while True:
        # Recibimos el mensaje del cliente
        recibido = cli_sock.recv(1024)

        if not recibido:
            # Si no se reciben datos, cerramos la conexión
            break

        # Mostramos la información del cliente y el mensaje de direccion
        if cont == 1:
            print("\n")
            print(f"Recibo conexion de la IP: {addr[0]} Puerto: {addr[1]}")
            print("El vehículo lleva dirección de: " + direction(recibido.decode('utf-8')))

        if cont == 2: # mensaje de velocidad y tiempo en el que recorrio el puente 
            print("Velocidad del vehículo: " + recibido.decode('utf-8') + " km/h")
            print("Tiempo de recorrido del vehículo en el puente: {:.2f}".format(calculate(recibido.decode('utf-8'))) ,"minutos")
            
        # Enviamos un mensaje de respuesta al cliente
        msg_toSend = "Mensaje recibido!!".encode('utf-8')
        cli_sock.send(msg_toSend)


        cont +=1

    # Cerramos el socket del cliente
    cli_sock.close()
    
    #print(f"Conexión con la IP: {addr[0]} cerrada.")
    

while True:
    # Aceptamos una nueva conexión
    cli_sock, addr = server.accept()

    # Creamos un nuevo hilo para atender al cliente
    hilo_cliente = threading.Thread(target=atender_cliente, args=(cli_sock, addr))
    hilo_cliente.start()



