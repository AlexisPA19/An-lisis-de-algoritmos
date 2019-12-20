from tkinter import ttk
from tkinter import*

class MultMat:
    def __init__(self,window):
        self.wind = window
        self.wind.title('Multiplicación de Matrices en cadena')

        #Creating a Frame Container
        frame = Frame(self.wind)
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #NumMat Input
        Label(frame, text = 'Número de matrices: ').grid(row = 1, column = 0)
        self.numMat = Entry(frame)
        self.numMat.focus()
        self.numMat.grid(row = 1, column = 1)

        #Button
        ttk.Button(frame, text = 'Aceptar',command =self.dimenMat).grid(row = 1, column = 3)
        
    
    #Creating input size mat
    def dimenMat(self):
        tam = int(self.numMat.get())
        frame1 = LabelFrame(self.wind, text = 'Matrices')
        frame1.grid(row = 1, column = 0, columnspan = 3, pady=20)
        
        self.fila = []
        self.columna = []
        for x in range(tam):
            Label(frame1, text = 'M{}→'.format(x)).grid(row = x+1, column = 0)
            Label(frame1, text = 'Fila: ').grid(row = x+1, column = 1)
            Label(frame1, text = 'Columna: ').grid(row = x+1, column = 3)
            self.fila.append(Entry(frame1))
            self.columna.append(Entry(frame1))
            self.fila[x].grid(row = x+1, column = 2)
            self.columna[x].grid(row = x+1, column = 4)
 
        ttk.Button(frame1, text = 'Calcular',command =self.table).grid(row = tam+1, column = 2)


    def table(self):
        tam = int(self.numMat.get())
        frame2 = LabelFrame(self.wind, text = 'Tabla')
        frame2.grid(row = tam+2, column = 0)
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        self.table = []
        for i in range(tam+1):
            self.table.append([])
            for j in range(tam+1):
                self.table[i].append(Label(frame2,font="arial36",bg="#EEE0DE",relief="ridge",pady=30,padx=30,text="    "))
                self.table[i][j].grid(row = i, column = j)
        
        for i in range(tam+1):
            for j in range(tam-i):
                self.table[j+i+1][i].config(text=" X ")
                
        for i in range(1,tam+1):
            self.table[i][0].config(text="M{}".format(i-1))
            self.table[0][i].config(text="M{}".format(i-1))
            self.table[i][i].config(text=" X ")

        for i in range(1,tam+1):
            for j in range(tam-i):
                self.table[i][j+i+1].config(text=" Z ")
        
 

            
                
        
            
            
                
        for x in range(tam):
            print("Fila{}:{} Columna{}:{}".format(x,int(self.fila[x].get()),x,int(self.columna[x].get())))
        self.multmatcad()
    
    def multmatcad(self):
        tam = int(self.numMat.get())

        self.tamMatList = []
        for i in range(tam):
            self.tamMatList.append((int(self.fila[i].get()),int(self.columna[i].get())))
        
        print(self.tamMatList)

        listM=[]
        for i in range(tam):
            listM.append([])
            for j in range(tam):
                listM[i].append(None)
        
        for i in range(tam):
            listM[i][i]=0
        
        for i in range(tam):
            for j in range(tam-i-1):
                listM[i][j+i+1] = 

        for i in range(tam):
            for j in range(tam):
                print(listM[i][j],end=" ")
            print("\n")
        


        

        

        



if __name__ == '__main__':
    window = Tk()
    application = MultMat(window)
    window.mainloop()