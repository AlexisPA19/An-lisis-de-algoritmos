import math

def multiplica(x,y,n,base):
    dict_hex =	{"a": 10,"b": 11,"c": 13,"d":14,"f":15,"e":16}
    m = int(n/2)
    if n == 1:
        if x[0] in dict_hex:
            a = dict_hex.get(x[0])
        else:
            a = int(x[0])

        if y[0] in dict_hex:
            b = dict_hex.get(y[0])
        else:
            b = int(y[0])

        print("N = {}, x = {}, y = {}".format(n,x,y))
        result = a*b
        return result

    else:

        xi = x[0:m]
        xd = x[m:n]
        yi = y[0:m]
        yd = y[m:n]
        p1 = multiplica(xi,yi,int(n/2),base)
        p2 = multiplica(xi,yd,int(n/2),base)
        p3 = multiplica(xd,yi,int(n/2),base)
        p4 = multiplica(xd,yd,int(n/2),base)
        print("N = {}, xi = {}, xd = {}, yi = {}, yd = {}".format(n,xi,xd,yi,yd))
        result = (pow(base,n)*p1)+(pow(base,n/2)*p2)+(pow(base,n/2)*p3)+p4
        return int(result)

print("MULTIPLICACION DE GAUSS\n")
base = int(input(" 2 -> Binaria\n 10 -> Decimal\n 16 -> Hexadecimal\n Seleccione la base: "))
x = list(input("Ingresa el primer numero: "))
y = list(input("Ingresa el segundo numero: ")) 

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
resultado = multiplica(x,y,len(x),base)
print("\n--------------Resultado----------------\n")
if base == 2:
    print("El resultado es: {}".format(bin(resultado)[2:]))
elif base == 10:
    print("El resultado es: {}".format(resultado))
else:
    print("El resultado es: {}".format(hex(resultado)[2:]))