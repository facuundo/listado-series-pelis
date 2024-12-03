import tkinter as tk
from cliente.vista import Frame, barrita_menu

def main():
    ventana = tk.Tk()
    ventana.title("Mis pelis y series")
    ventana.iconbitmap('img/videocamara.ico')
    ventana.resizable(False, False)

    barrita_menu(ventana)
    app = Frame(root = ventana) #instanciamos la clase Frame

    ventana.mainloop()

if __name__ == '__main__':
    main()