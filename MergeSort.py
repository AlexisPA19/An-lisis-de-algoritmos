
def  mergesort(lista):
    left = []
    right = []
    result = []
    if len(lista) <= 1:
        return lista
    else:
        middle = int(len(lista)/2)
        for x in range(middle):
            left.append(lista[x])
        for x in range(middle,len(lista)):
            right.append(lista[x])
        
        left = mergesort(left)
        right = mergesort(right)

        if int(left[-1]) <= int(right[0]):
            left = left + right
            return left
        
        result = merge(left,right)
        return result

def merge(left,right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if int(left[0]) <= int(right[0]):
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]
    if len(left) > 0:
        result = result + left
    if len(right) > 0:
        result = result + right
    return result

print("ORDENAMIENTO POR MEZCLA")

lista = list(input("Ingresa una lista de numeros: "))
result = mergesort(lista)
print("Elementos ordenados: {}".format(result))