"""voy a a utilizar la librería tkinter para interfaces gráficas"""
"""Hago un termómetro con Tkinter pero cargar la imagen da problemas, xq?"""
"""Tkinter usa objetos llamados widgets"""
"""arreglar borrar ultimo Nº que siempre queda(if), eliminar introducir espacios en
blanco, arreglar meter Nº negativo, falta conversión de grados"""

from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    __temperaturaAnt = ""
    
    def __init__(self):#método constructor del objeto
        Tk.__init__(self)#inicializo para que la pantalla Tk sea mi pantalla
        self.title("Termómetro")#doy nombre a mi ventana
        self.geometry("210x150")#doy tamaño a la ventana
        self.configure(bg = "#ECECEC")#configurar la ventana principal de la APP
        self.resizable(0,0)
    
        self.temperatura = StringVar(value="")#inicializo objeto stringvar tipo string en variable self.temeratura
        self.temperatura.trace("w", self.validateTemperature)#trazar/seguir para llamar a método validateTemperature cada vez que escribo en self.temperatura
        self.tipoUnidad = StringVar(value="")#inicializo variable tipo stringo con valor "C"

        self.createLayout()
    
    def createLayout(self):
        self.entrada = ttk.Entry(self,textvariable=self.temperatura).place(x=10,y=10)#widget de tipo entry
        
        self.lblUnidad = ttk.Label(self, text="Grados:").place(x=10,y=45)#etiqueta de grados
        self.rb1 = ttk.Radiobutton(self, text="Fahrenheit", variable=self.tipoUnidad, value="F",command=self.selected).place(x=20,y=65)#botón para seleccionar fahrenheit
        self.rb2 = ttk.Radiobutton(self, text="Celsius", variable=self.tipoUnidad, value="C",command=self.selected).place(x=20,y=85)#botón para seleccionar celsius
        
    def start(self):
        self.mainloop()#hacer loop a la ventana, espera a los eventos

    def validateTemperature(self, *args):#*args espera una lista o tupla, vacía o llena
        nuevoValor = self.temperatura.get()#cojo nuevo valor y lo guardo
        print("nuevoValor",nuevoValor,"vs valorAnterior",self.__temperaturaAnt)
        try:
            float(nuevoValor)#intento transformar a float
            self.__temperaturaAnt = nuevoValor#si transforma me guardo valor anterior como nuevo valor
            print("fija valor anterior a",self.__temperaturaAnt)
        
        except:
            self.temperatura.set(self.__temperaturaAnt)#si no se transforma me vuelve a valor anterior
            print("recupera valor anterior",self.__temperaturaAnt)
        
    def selected(self):
        resultado = 0
        toUnidad = self.tipoUnidad.get()
        grados = float(self.temperatura.get())
        
        if toUnidad == "F":
            resultado = grados * 9/5 + 32
        elif toUnidad == "C":
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
            
        self.temperatura.set(resultado)





if __name__ == "__main__":
    app = mainApp()
    app.start()

    
