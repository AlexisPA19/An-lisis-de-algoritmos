import math

def calcularFFT(signal):
    if len(signal) == 1:
        return signal
    else:    
        s_par = []
        s_impar = []

        for j in range(len(signal)):
            if (j%2) == 0:
                s_par.append(signal[j])
            else:
                s_impar.append(signal[j])

        A = calcularFFT(s_par)
        B = calcularFFT(s_impar)

        F = []
        n = int(len(signal)/2)
        b = -(2*math.pi)/len(signal)
        W_n = complex(math.cos(b),math.sin(b))
        W = 1

        for k in range(n):
            F.insert(k,A[k] + W*B[k])
            F.insert(k+n,A[k] - W*B[k])
            W = W*W_n
        return F

tam = int(input("Ingresa el total de mustras: "))
signal = []
for i in range(tam):
    d = int(input("Ingrese dato {}: ".format(i)))
    signal.append(d)

print("Sen: {}".format(signal))
result = calcularFFT(signal)
print("Resultado: {}".format(result))


