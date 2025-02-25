from tkinter import Tk,Label, Button, Entry, Frame, messagebox, mainloop
from PIL import Image, ImageTk, Image

class Login:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x700")
        self.ventana.title("Login")

        fondo = "#88FFB4"

        self.frame_superior = Frame(self.ventana)
        self.frame_superior.configure(bg=fondo)
        self.frame_superior.pack(fill"both", expand=True)

        self.frame_inferior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(1, weight=1)
        

        self.titulo = Label(self.frame_superior,
                            text="login",
                            font=("Terrenos", 36, "bold")
                            bg=fondo)
        self.titulo.pack(side="top", pady=20)


        self.img = Image.open(  ) #"se pone la ruta del usuario"
        self.img = self.img.resize((150,165))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame_superior, image = self.render, bg = fondo)
        self.fondo.pack(expand=True, fill"both", side="top")


        self.label_usuario = Label(self.frame_inferior,
                                  text="Usuario:";
                                  font=("Arial", 18),
                                  bg = fondo,
                                  fg="black")
        self.label_usuario.grid(row=0, column=0, padx=10, sticky="e")

        self.entry_usuario = Entry(self.frame_inferior,
                                   bd=0,
                                   width=14,
                                   font=("Arial", 18))
        self.entry_usuario.grid(row = 10, column=1, columnspan=3, padx=5, sticky="w")

        self.boton_ingresar = Button(self.frame_inferior,
                                     text="ingresar",
                                     width=16,
                                     font=("Arial", 12),
                                     command=self.entrar)
        self.boton_ingresar.grid(row=2, column=0, columnspan=2, pady=35)


        
    
        mainloop()
    def entrar(self):
        nombre = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()

        if nombre == "Admin" and contraseña == "hola123":
            messagebox.showinfo("Acceso Correcto", "Has podido ingresar")
        else:
            messagebox.showinfo("Acceso Incorrecto", "Algun dato es incorrecto")
Login()  