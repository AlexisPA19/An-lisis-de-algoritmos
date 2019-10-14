import math

def multiplica(x,y,n):
    m = int(n/2)
    m1 = m +1
    if n == 1:
        print("N = {}, x = {}, y = {}".format(n,x,y))
        result = int(x[0])*int(y[0])
        return result

    else:
        xi = x[0:m]
        xd = x[m:n]
        yi = y[0:m]
        yd = y[m:n]
        p1 = multiplica(xi,yi,int(n/2))
        p2 = multiplica(xi,yd,int(n/2))
        p3 = multiplica(xd,yi,int(n/2))
        p4 = multiplica(xd,yd,int(n/2))
        print("N = {}, xi = {}, xd = {}, yi = {}, yd = {}".format(n,xi,xd,yi,yd))
        result = (pow(2,n)*p1)+(pow(2,n/2)*p2)+(pow(2,n/2)*p3)+p4
        return int(result)

print("MULTIPLICACION BINARIA\n")
x = list(input("Ingresa el primer numero binario: "))
y = list(input("Ingresa el segundo numero binario: ")) 

if len(x) > len(y):
    while len(x) != len(y):
        y.insert(0,0)
elif len(x) < len(y):
    while len(x) != len(y):
        x.insert(0,0)
if math.log(len(x),2)%1 != 0:
    while math.log(len(x),2)%1 != 0:
        y.insert(0,0)
        x.insert(0,0)

print("\n--------------Numeros ajustados----------------\n")
print("X = {} con {} digitos\n".format(x,len(x)))
print("Y = {} con {} digitos\n".format(y,len(y)))
print("\n--------------Recursividad----------------\n")
resultado = multiplica(x,y,len(x))
print("\n--------------Resultado----------------\n")
print("El resultado es: {}".format(bin(resultado)[2:]))




