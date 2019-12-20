from tkinter import ttk
from tkinter import*

class SubsecComMax:
    #Definición de la UI
    def __init__(self,window):
        self.wind = window
        self.wind.title('Subsecuencia Común Máxima')

        frame = LabelFrame(self.wind)
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        Label(frame, text = 'Secuencia X:').grid(row = 1, column = 0)
        self.secX = Entry(frame)
        self.secX.grid(row =1, column = 1)
        Label(frame, text = 'Secuencia Y:').grid(row = 2, column = 0)
        self.secY = Entry(frame)
        self.secY.grid(row =2, column = 1)

        ttk.Button(frame,text = 'Calcular', command = self.Subsecuencia).grid(row = 3, column = 1)
        
    #Programación Dinámica
    def Subsecuencia(self):
        x = str(self.secX.get())
        y = str(self.secY.get())
        tamx = len(x) + 1
        tamy = len(y) + 1
        self.lenx = len(x)
        self.leny = len(y)


        print("X: {} tam:{}".format(x,len(x)))
        print("Y: {} tam:{}".format(y,len(y)))

        self.tabla = []
        
        #Crea la tabla (arreglo)
        for i in range(tamy):
            self.tabla.append([])
            for j in range(tamx):
                self.tabla[i].append((0,None))

        for i in range(tamy):
            self.tabla[i][0] = tuple((0," "))
        for i in range(tamx):
            self.tabla[0][i] = tuple((0," "))
        
        #Llenado de la tabla (arreglo)
        for i in range(1,tamy):
            for j in range(1,tamx):
                if y[i-1] == x[j-1] :
                    self.tabla[i][j] = tuple((self.tabla[i -1][j-1][0] + 1,"D")) 
                elif self.tabla[i-1][j][0] >= self.tabla[i][j-1][0]:
                    self.tabla[i][j] = tuple((self.tabla[i-1][j][0],"S"))
                else:
                    self.tabla[i][j]= tuple((self.tabla[i][j-1][0],"I"))

        for i in range(tamy):
            for j in range(tamx):
                print("{}".format(self.tabla[i][j]),end=" ")
            print("\n")
    
        

        #Creacion de la tabla UI

        frame2 = LabelFrame(self.wind, text = 'Tabla de seguimiento')
        frame2.grid(row = 4, column = 0)
        self.table = []
        for i in range(tamy+1):
            self.table.append([])
            for j in range(tamx+1):
                self.table[i].append(Label(frame2,font="arial36",bg="#EEE0DE",relief="ridge",pady=7,padx=8,text="  \n"))
                self.table[i][j].grid(row = i, column = j)
        
        for i in range(2,tamy+1):
            self.table[i][0].config(text=y[i-2]+"\n",bg="gray")
        for i in range(2,tamx+1):
            self.table[0][i].config(text=x[i-2]+"\n",bg="gray")

        for i in range(1,tamy+1):
            self.table[i][1].config(text="0\n")
        for i in range(1,tamx+1):
            self.table[1][i].config(text="0\n")
        
        for i in range(2,tamy+1):
            for j in range(2,tamx+1):
                self.table[i][j].config(text="{}\n{}".format(self.tabla[i-1][j-1][0],self.tabla[i-1][j-1][1]))
        
        len_max = int(self.tabla[tamy-1][tamx-1][0])
        list_sus_max =[]
        list_sus_max.append((tamy-1,tamx-1))
        for i in range(tamy):
            for j in range(tamx):
                if self.tabla[i][j][0]==len_max and self.tabla[i][j][1]=='D' and j != tamx-1:
                    list_sus_max.append((i,j))
        
        print("Caminos posibles:{}".format(list_sus_max))

        

        #Formación de la subsecuencia común máxima
        self.sol=""
        frame3 = Frame(self.wind)
        frame3.grid(row = 5, column = 0)
        for i in range(len(list_sus_max)):
            self.sol=""
            color = "#{1}5{0}826".format((i+2*i*3)%9,(i+2*i*8+16)%9)
            self.Escribir(self.tabla,y,list_sus_max[i][0],list_sus_max[i][1],color)
            Label(frame3, text = 'Subsecuencia común máxima : {}'.format(self.sol)).grid(row = i+1, column = 0)
         
        print("Subsecuencia común máxima: {}".format(self.sol))
        
    #Recursión
    def Escribir(self,tabla,y,i,j,color):

            if i == 0 or j == 0:
                self.sol=""
            elif tabla[i][j][1] == 'D':
                self.Escribir(tabla,y,i-1,j-1,color)
                self.sol = self.sol + y[i-1]
                self.table[i+1][j+1].configure(bg="{}".format(color))
            elif tabla[i][j][1] == 'S':
                self.Escribir(tabla,y,i - 1,j,color)
                self.table[i+1][j+1].configure(bg="{}".format(color))
            else:
                self.Escribir(tabla,y,i,j - 1,color)
                self.table[i+1][j+1].configure(bg="{}".format(color))
        
if __name__ == '__main__':
    window = Tk()
    application = SubsecComMax(window)
    window.mainloop()