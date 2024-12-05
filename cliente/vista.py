import tkinter as tk
from tkinter import ttk

class Frame(tk.Frame):
    #hereda de la clase Frame de tkinter
    def __init__(self, root = None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        #self.config(bg='blue')
        self.label_form()
        self.input_form()
        self.botones_principales()
        self.tabla_peliculas()
        self.tabla_series()
        self.bloquear_campos() #se bloquean todos los campos cuando se inicializa porque no se tocó editar

    def label_form(self):
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row = 0, column=0, padx=0, pady=10)

        self.label_nombre = tk.Label(self, text='Duración: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row = 1, column=0, padx=0, pady=10)

        self.label_nombre = tk.Label(self, text='Genero: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row = 2, column=0, padx=0, pady=10)

    def input_form(self):
        self.entry_nombre= tk.Entry(self)
        self.entry_nombre.config(width=50)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan='2')

        self.entry_duracion= tk.Entry(self)
        self.entry_duracion.config(width=50)
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10) #columnspan='2'

        self.entry_genero = ttk.Combobox(self, state="readonly")
        self.entry_genero.config(width=25)
        self.entry_genero.bind("<<ComboboxSelected>>")
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10)

    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos) #creacion variable boton alta- el command se habilita luego de hacer click, por eso no lleva parentesis
        self.btn_alta.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000') #configuracion de esta variable
        self.btn_alta.grid(row=3,column=0, padx=10, pady=10)

        self.btn_modi = tk.Button(self, text='Guardar') #creacion boton modificar
        self.btn_modi.config(width= 20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2AB3', cursor='hand2', activebackground='#7594F5', activeforeground='#000000')
        self.btn_modi.grid(row= 3, column=1, padx=10, pady=10)

        self.btn_cance = tk.Button(self, text= 'Cancelar', command=self.bloquear_campos) #creacion boton cancelar
        self.btn_cance.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_cance.grid(row= 3, column= 2, padx=10, pady=10)

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')

    #ver si poner en init o no: hacer tabla con ttk.Treeview https://github.com/LuisOchoa1495/Python-Tkinter/blob/master/SISTEMA%20DESKTOP/4-CRUD.py
    def tabla_peliculas(self):
        self.tree = ttk.Treeview(height=10, columns=("columna1", "columna2", "columna3"))
        self.tree.heading('#0', text='ID', anchor='center')
        self.tree.column("#0", width=90, minwidth=75, stretch='no')

        self.tree.heading('columna1', text='Nombre', anchor='center')
        self.tree.column("columna1", width=150, minwidth=75, stretch='no')

        self.tree.heading('columna2', text='Genero', anchor='center')
        self.tree.column("columna2", width=150, minwidth=75, stretch='no')

        self.tree.heading('columna3', text='Plataforma', anchor='center')
        self.tree.column("columna3", width=150, minwidth=75, stretch='no')

        self.tree.pack()

    def tabla_series(self):
        self.tree = ttk.Treeview(height=10, columns=("columna1", "columna2", "columna3", "columna4"))
        self.tree.heading('#0', text='ID', anchor='center')
        self.tree.column("#0", width=90, minwidth=75, stretch='no')

        self.tree.heading('columna1', text='Nombre', anchor='center')
        self.tree.column("columna1", width=150, minwidth=75, stretch='no')

        self.tree.heading('columna2', text='Num Temporadas', anchor='center')
        self.tree.column("columna2", width=150, minwidth=75, stretch='no')

        self.tree.heading('columna3', text='Genero', anchor='center')
        self.tree.column("columna3", width=150, minwidth=75, stretch='no')

        self.tree.heading('columna4', text='Plataforma', anchor='center')
        self.tree.column("columna4", width=150, minwidth=75, stretch='no')

        self.tree.pack()

def barrita_menu(root):
    #esto puede ir en otro archivo
    barra = tk.Menu(root)
    root.config(menu = barra, width = 300, height = 300)
    menu_inicio = tk.Menu(barra, tearoff=0)

    # niveles
    #principal
    barra.add_cascade(label='inicio', menu= menu_inicio)
    barra.add_cascade(label='Consultas', menu = menu_inicio)
    barra.add_cascade(label='Acerca de...', menu = 'menu_inicio')
    barra.add_cascade(label='Ayuda', menu = menu_inicio)

    #submenu
    menu_inicio.add_command(label='Conectar DB')
    menu_inicio.add_command(label='Desconectar DB')
    menu_inicio.add_command(label='Salir', command= root.destroy)