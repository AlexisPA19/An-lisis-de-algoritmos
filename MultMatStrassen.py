import math
'''--------------------------------Método Convencional-------------------------------------'''
def multMat(matrizA,matrizB,n):
  #Caso base
  if n == 2:
    m = []
    #Inicialización y llenado de la matriz resultante
    for i in range(2):
      m.append([])
      for j in range(2):
        m[i].append(0)
        for k in range(2):
          m[i][j] += int(matrizA[i][k])*int(matrizB[k][j])

    return m
  else:
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    
    t = int(n/2)
    #División de la ambas matrices en sub matrices
    for i in range(t):
      a.append([])
      b.append([])
      c.append([])
      d.append([])
      e.append([])
      f.append([])
      g.append([])
      h.append([])
      for j in range(t):
        a[i].append(int(matrizA[i][j]))
        e[i].append(int(matrizB[i][j]))

        b[i].append(int(matrizA[i][t+j]))
        f[i].append(int(matrizB[i][t+j]))

        c[i].append(int(matrizA[t+i][j]))
        g[i].append(int(matrizB[t+i][j]))

        d[i].append(int(matrizA[t+i][t+j]))
        h[i].append(int(matrizB[t+i][t+j]))
    
    #Cálculo de los productos
    p1 = list(multMat(a,e,t))
    p2 = list(multMat(b,g,t))
    p3 = list(multMat(a,f,t))
    p4 = list(multMat(b,h,t))
    p5 = list(multMat(c,e,t))
    p6 = list(multMat(d,g,t))
    p7 = list(multMat(c,f,t))
    p8 = list(multMat(d,h,t))

    m1 = list(sumaMatriz(p1,p2,t))
    m2 = list(sumaMatriz(p3,p4,t))
    m3 = list(sumaMatriz(p5,p6,t))
    m4 = list(sumaMatriz(p7,p8,t))

    #Inicialización de la matriz resultante
    matRes = []
    for i in range(n):
      matRes.append([])
      for j in range(n):
        matRes[i].append(None)

    #Llenado de la matriz resultante
    for i in range(t):
      for j in range(t):
        matRes[i][j] = m1[i][j]
        matRes[i][t+j] = m2[i][j]
        matRes[t+i][j] = m3[i][j] 
        matRes[t+i][t+j] = m4[i][j]
              
    return matRes
'''--------------------------------Método Strassen-------------------------------------'''
def multMatStrassen(matrizA,matrizB,n):
  #Caso base
  if n == 2:
    m = []
    #Inicialización y llenado de la matriz resultante
    for i in range(2):
      m.append([])
      for j in range(2):
        m[i].append(0)
        for k in range(2):
          m[i][j] += int(matrizA[i][k])*int(matrizB[k][j])

    return m
  else:
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    
    t = int(n/2)
    #División de la ambas matrices en sub matrices
    for i in range(t):
      a.append([])
      b.append([])
      c.append([])
      d.append([])
      e.append([])
      f.append([])
      g.append([])
      h.append([])
      for j in range(t):
        a[i].append(int(matrizA[i][j]))
        e[i].append(int(matrizB[i][j]))

        b[i].append(int(matrizA[i][t+j]))
        f[i].append(int(matrizB[i][t+j]))

        c[i].append(int(matrizA[t+i][j]))
        g[i].append(int(matrizB[t+i][j]))

        d[i].append(int(matrizA[t+i][t+j]))
        h[i].append(int(matrizB[t+i][t+j]))
    
    #Cálculo de los productos
    p1 = list(multMatStrassen(a,restaMatriz(f,h,t),t))
    p2 = list(multMatStrassen(sumaMatriz(a,b,t),h,t))
    p3 = list(multMatStrassen(sumaMatriz(c,d,t),e,t))
    p4 = list(multMatStrassen(d,restaMatriz(g,e,t),t))
    p5 = list(multMatStrassen(sumaMatriz(a,d,t),sumaMatriz(e,h,t),t))
    p6 = list(multMatStrassen(restaMatriz(b,d,t),sumaMatriz(g,h,t),t))
    p7 = list(multMatStrassen(restaMatriz(a,c,t),sumaMatriz(e,f,t),t))


    m1 = list(sumaMatriz(p5,sumaMatriz(p4,restaMatriz(p6,p2,t),t),t))
    m2 = list(sumaMatriz(p1,p2,t))
    m3 = list(sumaMatriz(p3,p4,t))
    m4 = list(sumaMatriz(restaMatriz(p1,p3,t),restaMatriz(p5,p7,t),t))
    
    #Inicialización de la matriz resultante
    matRes = []
    for i in range(n):
      matRes.append([])
      for j in range(n):
        matRes[i].append(None)

    #Llenado de la matriz resultante
    for i in range(t):
      for j in range(t):
        matRes[i][j] = m1[i][j]
        matRes[i][t+j] = m2[i][j]
        matRes[t+i][j] = m3[i][j] 
        matRes[t+i][t+j] = m4[i][j]
              
    return matRes

'''-----------------------Suma y resta de matrices----------------'''
def sumaMatriz(matrizA,matrizB,n):
  mat = []
  for i in range(n):
    mat.append([])
    for j in range(n):
      mat[i].append(int(matrizA[i][j]) + int(matrizB[i][j]))
  
  return mat

def restaMatriz(matrizA,matrizB,n):
  mat = []
  for i in range(n):
    mat.append([])
    for j in range(n):
      mat[i].append(int(matrizA[i][j]) - int(matrizB[i][j]))
  
  return mat
'''----------------------------------------------------------------'''

print("\nMULTIPLICACIÓN DE MATRICES\n")
ordenMatriz = 3
estrategia = 0
metods =	{
  8: "MÉTODO CONVENCIONAL",
  7: "MÉTODO STRASSEN"
}
name_file1 = str(input("Nombre del archivo de la Matriz A: "))
name_file2 = str(input("Nombre del archivo de la Matriz B: "))
while math.log(ordenMatriz,2)%1 != 0:
  ordenMatriz = int(input("Orden de la matriz: "))
  if math.log(ordenMatriz,2)%1 != 0:
    print("¡Debe ser un número potencia de 2!, intentalo nuevamete.")
while estrategia != 8 and estrategia != 7:
  estrategia = int(input("8 -> 8 productos (Método convencional) 7-> 7 productos (Método Strassen): "))
  if estrategia != 8 and estrategia != 7:
    print("¡Opción no valida!, intentalo nuevamete.")

print("\n{}".format(metods[estrategia]))

'''Lectura y almacenamiento en una matriz del archivo A'''
matA = []
f1 = open(name_file1, "r")
for x in f1:
  line = str(x)
  line = line.rstrip('\n')
  a = line.split((" "))
  matA.append(a)
f1.close()

print("\nMatriz A:")
for i in range(ordenMatriz):
  for j in range(ordenMatriz):
    print("{:^6}".format(matA[i][j]),end="")
  print("")

'''Lectura y almacenamiento en una matriz del archivo B'''
matB = []
f2 = open(name_file2,"r")
for x in f2:
  line = str(x)
  line = line.rstrip('\n')
  a = line.split((" "))
  matB.append(a)

f2.close()

print("\nMatriz B:")
for i in range(ordenMatriz):
  for j in range(ordenMatriz):
    print("{:^6}".format(matB[i][j]),end="")
  print("")

'''Tipo de estrategia'''
if estrategia == 8:
  AB = list(multMat(matA,matB,ordenMatriz))
else:
  AB = list(multMatStrassen(matA,matB,ordenMatriz))

'''Impresión de la matriz resultante'''
print("\nMatriz resultante:")
for i in range(len(AB)):
  for j in range(len(AB)):
    print("{:^5}".format(AB[i][j]),end="")
  print("")