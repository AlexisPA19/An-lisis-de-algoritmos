from tkinter import ttk
from tkinter import*

class problemaMochila:
    #Definición de la UI
    def __init__(self,window):
        self.wind = window
        self.wind.title('Problema de la Mochila')

        frame = Frame(self.wind)
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        Label(frame, text = 'Cantidad de objetos:').grid(row = 1, column = 0)
        self.cantObjetos = Entry(frame)
        self.cantObjetos.grid(row =1, column = 1)

        ttk.Button(frame,text = 'Siguiente', command=self.listObjetos).grid(row = 1, column = 2)
    
    def listObjetos(self):
        self.wind.quit()

        self.cantObj = int(self.cantObjetos.get())
        self.wind_objetos = window
        self.wind_objetos.title('Problema de la Mochila')

        frame = Frame(self.wind_objetos)
        frame.grid(row=0, column=0, columnspan = 3, pady = 20)

        self.nombreObjeto = []
        self.beneficio = []
        self.peso = []

        for x in range(self.cantObj):
            Label(frame, text = 'Nombre objeto {}:'.format(x)).grid(row = x+1, column = 0)
            Label(frame, text = 'Beneficio:').grid(row = x+1, column = 2)
            Label(frame, text = 'Peso: ').grid(row = x+1, column = 4)
            self.nombreObjeto.append(Entry(frame))
            self.beneficio.append(Entry(frame))
            self.peso.append(Entry(frame))
            self.nombreObjeto[x].grid(row = x+1, column = 1)
            self.beneficio[x].grid(row = x+1, column = 3)
            self.peso[x].grid(row = x+1, column = 5)

        Label(frame, text = 'Capacidad de la mochila:').grid(row = self.cantObj+4, column = 0)
        self.capacidadMochila = Entry(frame)
        self.capacidadMochila.grid(row = self.cantObj+4,column = 1)
 
        ttk.Button(frame, text = 'Calcular',command=self.dibujaTabla).grid(row = self.cantObj+4, column = 2)
    
        self.wind_objetos.mainloop()
    

    def dibujaTabla(self):

        self.wind_objetos.quit()

        self.calculoTabla()

        self.window_tabla = window
        self.window_tabla.title('Problema de la Mochila 3')

        frame = Frame(self.window_tabla)
        frame.grid(row=0, column=0, columnspan = 3, pady = 20)

        self.tabla = []

        for i in range(3):
            self.tabla.append([])
            for j in range(self.cantObj+1):
                self.tabla[i].append(Label(frame).grid(row = i+1, column = j+1))
        
        
        self.tabla[0][0].config(text="NOMBRE")
        self.tabla[0][1].config(text="BENEFICIO")
        self.tabla[0][2].config(text="PESO")

        for i in range(self.cantObj):
            

        self.window_tabla.mainloop()

    def calculoTabla(self):
        self.nomObjetos = []
        self.benfic = []
        self.pes = []
        self.capMochila = int(self.capacidadMochila.get())
        for i in range(self.cantObj):
            self.nomObjetos.append(self.nombreObjeto[i].get())
            self.benfic.append(self.beneficio[i].get())
            self.pes.append(self.peso[i].get())
        
        print("Nombre     Beficio     Peso\n")
        for i in range(self.cantObj):
            print("   {}     {}     {}\n".format(self.nomObjetos[i],self.benfic[i],self.pes[i]))
        print("Capacidad Mochilla: {}".format(self.capMochila))


if __name__ == '__main__':
    window = Tk()
    application = problemaMochila(window)
    window.mainloop()