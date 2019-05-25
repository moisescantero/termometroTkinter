"""voy a a utilizar la librería tkinter para interfaces gráficas"""
"""Hago un termómetro con Tkinter"""

from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    def __init__(self):#método constructor del objeto
        Tk.__init__(self)#inicializo para que la pantalla Tk sea mi pantalla
        self.title("Termómetro")#doy nombre a mi ventana
        self.geometry("200x150")#doy tamaño a la ventana
        self.configure(bg = "#DED789")#configurar la ventana principal de la APP
        
        
    def start(self):
        self.mainloop()#hacer loop a la ventana, espera a los eventos







if __name__ == "__main__":
    app = mainApp()
    app.start()
    
