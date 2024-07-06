import socket 



class Car ():
    
    def __init__(self):
        
        HOST = "localhost"
        PORT = 8050
        
        #socket
        self.obj = socket.socket()
        self.obj.connect((HOST,PORT))
        print("Conectado al servidor")
        

    # #envia mensajes al server
    def send_data(self,speed,direction):
 
        #envia direccion
        msg=direction
        self.obj.send(msg.encode("utf-8"))
        recive = self.obj.recv(1024)
        print("Recibido")
            
        #envia velocidad
        msg = speed
        self.obj.send(msg.encode("utf-8"))
        recive = self.obj.recv(1024)
        print("Recibido")
            
    

    #validaciones
    def validation(self,speed,direction):
        
        if((speed == "") | (direction =="")):
            return "No puede dejar casillas sin rellenar"
    
    #velocidad
        try:
            sp = int(speed)
        except ValueError:
            return "La velocidad debe ser un valor numérico entero positivo"
        if(sp==0):
            return  "La velocidad no puede ser cero" 
        elif(sp < 0):
            return "La velocidad no puede ser negativa"
        elif(sp > 120):
            return "La velocidad Max. del vehículo no puede exceder los 120 km/h"
        
    #direccion
        dir = str(direction).upper()
        if(not dir.isalpha()):
            return "La dirección no puede ser alfanumérica"
        if((dir != "BROOKLYN" ) & (dir != "MANHATTAN")):
            return "La dirección no es válida" 
        
        
        return "true"



    