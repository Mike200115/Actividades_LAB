import tkinter as tk
from tkinter import ttk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

raiz= tk.Tk()
raiz.geometry('500x400')
raiz.configure(bg = '#1E1E1E')
raiz.title('Practica')
#controles
def txt(x1,y1,tamaño):
    textbox = ttk.Entry(raiz,width=tamaño)
    textbox.config(font=('Century Gothic', 10))
    textbox.place(x=x1,y=y1)
    return textbox
def lbl(x1,y1,texto,tamaño,color):
    label = ttk.Label(raiz,text=texto)
    label.config(background='#1E1E1E',foreground=color,font=('Century Gothic', tamaño))
    label.place(x=x1,y=y1)
    return label
def btn(x1,y1,texto,ancho,alto,funcion):
    button = tk.Button(raiz,text=texto,height = alto,width=ancho,command=funcion)
    button.config(background='#1E1E1E',foreground='white',font=('Century Gothic', 12))
    button.place(x=x1,y=y1)
    return button

def mandar_correos():
    msg = MIMEMultipart()
    message = 'Holaaaa' #Ingrese el mensaje que va a mandar
    msg['From'] = txt_usu.get()

lbl_titulo = lbl(85,1,'Mandar spam a tus amigos',18,'white')
lbl_usu = lbl(73,65,'Correo :',11,'white')
lbl_pass = lbl(73,145,'Contraseña :',11,'white')
lbl_path = lbl(73,225,'Direccion de archivo.txt :',11,'white')
txt_usu = txt(73,90,50)
txt_pass = txt(73,170,50)
txt_direccion = txt(73,250,50)
btn_enviar = btn(83,315,'Enviar Correos',32,2, mandar_correos)





raiz.mainloop()