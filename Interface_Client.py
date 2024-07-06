from tkinter import Tk, Label , Button ,Entry, messagebox,Frame,Menu
from Client import Car


#empaca frame de la opcion ayuda
def pack_info():

    frame_h.pack_forget()#oculta fame 
    label_c.pack_forget()#ocula label inferior


    #destruye widgest del frame para que no se repitan en la proxima llamada
    for widget  in frame_h.winfo_children():
        widget.destroy()
    
    #desempaca frame data
    frame_data.pack(expand= True,fill="both")
    #label inferior cliente
    label_c.pack(fill="x",side="top")

    #habilita opcion
    option.entryconfig(index="Ayuda",state= "active")
    
    #habilita opcion
    option.entryconfig(index="Volver",state = 'active')
              

#muestra informacion de ayuda 
def help_info():

    frame_data.pack_forget()#oculta el frame data
    
    archive_info = open("info.txt","r")
    data_info = archive_info.read()
    
    frame_h.pack(expand= True,fill="both")

    text_info = Label(frame_h,bg="white",text=data_info,bd=5,font=("Arial",9),justify="left").pack()

    
    #activa la opcion volver
    option.entryconfig(index="Volver",state ="active")

    #deshabilita la opcion de ayuda
    option.entryconfig(index="Ayuda",state= "disabled")

    archive_info.close()


    
    
#envia datos al objeto  
def send_data():

    #valida datos
    message = car.validation(speed.get(),direction.get())
    if(message != "true"):
        messagebox.showerror(message = message,title="ERROR")#tipo de error
        return True
    
    #desactiva boton
    boton_send.config(state= 'disabled')
    
    #asigna datos  al cliente
    car.send_data(speed.get(),direction.get())




#ventana raiz
root = Tk()
root.title("Aplicación")
root.minsize(400,200)
root.resizable(False,False)

#menu
main = Menu()
option = Menu(main,tearoff= False)
main.add_cascade(menu = option, label= "Opción")
option.add_command(label="Ayuda",command = help_info)
option.add_command(label="Volver",command = pack_info,state="normal")
option.add_separator()
option.add_command(label="Salir",command= root.quit)
root.config(menu= main)


#frame para mostrar info del txt ayuda
frame_h = Frame(root,bg="white")


#----------------------------------------
#frame para vista de ingreso de datos
frame_data = Frame(root,bg="white")
frame_data.pack(expand= True,fill="both")

# label y entry direccion
direction_ = Label(frame_data,text="Dirección",bd=5,font=("Arial,25")).place(x= 20,y =34)
direction = Entry(frame_data,bg="gray",bd=5)
direction.place(x= 120, y= 34)

#label y entry velocidad
speed_ = Label(frame_data,text="Velocidad",bd=5,font=("Arial,25")).place(x= 19, y= 84)
speed = Entry(frame_data,bg="gray",bd=5)
speed.place(x= 119, y= 84)
unit = Label(frame_data,text="km/h",bd=5,font=("Arial,25")).place(x= 265,y =84)

#boton
boton_send = Button(frame_data,text="Enviar",command = send_data)
boton_send.place(x=162,y=130)

#label inferior cliente
label_c = Label(root,bg="black",text="Cliente",font=("Arial",9),fg="white")
label_c.pack(fill="x",side="top")


#objeto auto
car = Car()


root.mainloop()
