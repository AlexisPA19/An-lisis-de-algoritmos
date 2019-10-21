
def quickSort(lista):
    if len(lista) <= 1:
        return lista
    else:

        less = []
        greater = []

        pivot = int(lista[0])

        for x in range(1,len(lista)):
            if int(lista[x]) <= pivot:
                less.append(lista[x])
                print(less)
            else:
                greater.append(lista[x])
                print(greater)
        
        list_left = quickSort(less)
        list_right = quickSort(greater)

        list_final = list_left + [pivot] + list_right

        return list_final


print("QUICK SORT")
lista = list(input("Ingresa una lista de numeros: "))
result = list(quickSort(lista))

print("La lista ordenad es: {}".format(result))