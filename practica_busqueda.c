#include <stdio.h>
#include <stdlib.h>

struct nodo{
    struct nodo *padre;
    struct nodo *izquierdo;
    struct nodo *derecho;
    int valor;
};
struct nodo *crear_nodo(struct nodo *padre,int valor);
struct nodo *agregar_valor(struct nodo* arbol, int valor);
struct nodo *buscar_nodo(struct nodo *arbol,int valorAbuscar);

void BusquedaSecuencial(int* ptr_array, int tam, int dato);
void BusquedaBinaria(int* ptr_array,int tam, int dato );

int main(int argc, char const *argv[])
{
    struct nodo *arbol=NULL;
    

    
    int tam,i,valor,dato;
    int opt = 1;

    printf("Tam del arreglo: ");
    scanf("%d",&tam);

    int *ptr_array = NULL;
    ptr_array = (int*)malloc(tam*sizeof(int));

    for ( i = 0; i < tam; i++)
    {
        printf("Ingrese el valor %d: ",i);
        scanf("%d",&valor);
        ptr_array[i]= valor;
        arbol = agregar_valor(arbol,valor);
    }
    printf("\nArreglo: ");
    for ( i = 0; i < tam; i++)
    {
        printf("%d ",ptr_array[i]);
    }
    while (opt == 1)
    {
        printf("\n\nIndique el valor a buscar: ");
        scanf("%d",&dato);

        printf("\n--BUSQUEDA SECUENCIAL--\n");
        BusquedaSecuencial(ptr_array,tam,dato);

        printf("\n\n--BUSQUEDA BINARIA--\n");
        BusquedaBinaria(ptr_array,tam,dato);

        printf("\n\n--ARBOL BUSQUEDA BINARIA--\n");
        buscar_nodo(arbol,dato);

        printf("\n\nHacer otra busqueda? ");
        scanf("%d",&opt);
    } 
    return 0;
}
struct nodo *crear_nodo(struct nodo *padre,int valor){
    struct nodo *n = calloc(sizeof(struct nodo),1);
    n->padre = padre;
    n->valor = valor;
    return n;
}
struct nodo *agregar_valor(struct nodo* arbol, int valor){
    struct nodo *temp,*pivote;
    int derecho = 0;
    if (arbol)
    {
        temp=arbol;
        while (temp != NULL)
        {
            pivote = temp;
            if (valor>temp->valor)
            {
                temp = temp->derecho;
                derecho = 1;
            }else
            {
                temp=temp->izquierdo;
                derecho = 0;
            }
        }
        temp = crear_nodo(pivote,valor);
        if (derecho)
        {
            printf("Insertando %i del lado derecho\n",valor,pivote->valor);
            pivote->derecho=temp;
        }else
        {
            printf("Insertando %i del lado izquierdo\n",valor,pivote->valor);
            pivote->izquierdo=temp;
        }
        return arbol;
    }else
    {
        printf("Insertando %i como nodo raiz del arbol\n",valor,pivote->valor);
        temp = crear_nodo(NULL,valor);
        return temp;
    } 
}
struct nodo *buscar_nodo(struct nodo *arbol,int valorAbuscar){
        struct nodo *temp = NULL,*pivote = NULL;
        int entrar=1,count=0;
        temp=arbol;

        while (entrar == 1 && temp != NULL)
        {
            count++;
            pivote = temp;
            if (valorAbuscar == temp->valor)
            {
                printf("Dato encontrado\n");
                printf("\nLa cantidad de pasos realizados es: %d",count);

                entrar = 0;
            }else
            {
                 if (valorAbuscar > temp->valor)
                {
                    temp = temp->derecho;
                }else
                {
                    temp=temp->izquierdo;
                }
            }
        }
        if(entrar == 1){
            printf("Dato no encontrado\n");
            printf("\nLa cantidad de pasos realizados es: %d",count);
        }
        return temp;
}
void BusquedaSecuencial(int* ptr_array, int tam, int dato){
    
    int flag = 0, count = 0;

    while (flag == 0 && count < tam)
    {  
        if(ptr_array[count] == dato){
            flag = 1;
            printf("El dato esta en la posicion %d",count);
            printf("\nLa cantidad de pasos realizados es: %d",count+1);
        }
        count++;  
    }
    if (flag == 0){
            printf("No se encontro el valor");
            printf("\nLa cantidad de pasos realizados es: %d",count);
    }
}
void BusquedaBinaria(int* ptr_array,int tam, int dato ){
    int ini=0,fin=tam,count=0;
    int mitad=(ini+fin)/2;
    int s=-1;
    while (ini>=0&&ini<=fin&&fin<=tam&&s==-1)
    {
        count++;
        if (ptr_array[mitad]<dato)
        {
            ini = mitad+1;
            mitad=(ini+fin)/2;
            
        }
        else
        {
            if(ptr_array[mitad]==dato){
                s=mitad;
            }
            else
            {
                fin=mitad-1;
                mitad = (ini+fin)/2;
            }
        }  
    }
    if (s == -1)
    {
        printf("No se encontro el valor");
        printf("\nLa cantidad de pasos realizados es: %d",count);
    }else
    {
        printf("El dato esta en la posicion %d",s);
        printf("\nLa cantidad de pasos realizados es: %d",count);
    }
}