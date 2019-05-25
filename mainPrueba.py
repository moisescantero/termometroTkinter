"""voy a a utilizar la librería tkinter para interfaces gráficas"""
"""Hago un termómetro con Tkinter pero cargar la imagen da problemas, xq?"""
"""Tkinter usa objetos llamados widgets"""

from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    def __init__(self):#método constructor del objeto
        Tk.__init__(self)#inicializo para que la pantalla Tk sea mi pantalla
        self.title("Termómetro")#doy nombre a mi ventana
        self.geometry("200x150")#doy tamaño a la ventana
        self.configure(bg = "#DED789")#configurar la ventana principal de la APP
    
        self.temperatura = StringVar(value="")#inicializo variable tipo string
        self.tipoUnidad = StringVar(value="C")#inicializo variable tipo stringo con valor "C"

        self.createLayout()
    
    def createLayout(self):
        self.entrada = ttk.Entry(self, variable=self.temperatura)#widget de tipo entry
         
        
    def start(self):
        self.mainloop()#hacer loop a la ventana, espera a los eventos







if __name__ == "__main__":
    app = mainApp()
    app.start()
    
