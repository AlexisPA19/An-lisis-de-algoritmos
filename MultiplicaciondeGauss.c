#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define CHAR_BITS .5

char* lecturaCadena();
int multiplica(char* num1,char* num2,int tam, int base);
void binario(int num);

int main(int argc, char const *argv[])
{
    int opt,i,dif,tam;
    char* ptrA = NULL;
    char* ptrB = NULL;
    char* auxA = NULL;
    char* auxB = NULL;
    char* num1 = NULL;
    char* num2 = NULL;
    


    printf("MULTIPLICACION DE GAUSS\n");
    printf(" 2 -> Binaria\n 10 -> Decimal\n 16 -> Hexadecimal\n Seleccione la base: ");
    scanf("%d",&opt);
    printf("Introduce el primer numero: ");
    ptrA = lecturaCadena();
    printf("Introduce el segundo numero: ");
    ptrB = lecturaCadena();

    printf("Numero A: %s, con %d digitos.\n",ptrA,strlen(ptrA));
    printf("Numero B: %s, con %d digitos.\n",ptrB,strlen(ptrB));
    
    if (strlen(ptrA) > strlen(ptrB))
    {   tam = strlen(ptrA);
        auxA = (char*)malloc (tam*sizeof(char));
        auxB = (char*)malloc (tam*sizeof(char));
 
        dif = strlen(ptrA) - strlen(ptrB);
        for (i = 0; i < dif; i++){
            auxB[i] = '0';
        }
        int j=0;
        for ( i = dif; i < strlen(ptrA); i++){
            auxB[i] = ptrB[j];
            j++;   
        }
        printf("\nNum A: ");
        for ( i = 0; i < strlen(ptrA); i++){
            auxA[i] = ptrA[i];
            printf("%c",auxA[i]);
        }
        printf("\nNum B: ");
        for ( i = 0; i < strlen(ptrA); i++){
            printf("%c",auxB[i]);
        }
    }else if (strlen(ptrA) < strlen(ptrB))
    {
        tam = strlen(ptrB);
        auxA = (char*)malloc (tam*sizeof(char));
        auxB = (char*)malloc (tam*sizeof(char));
        dif = strlen(ptrB) - strlen(ptrA);
        for (i = 0; i < dif; i++){
            auxA[i] = '0';
        }
        int j=0;
        for ( i = dif; i < strlen(ptrB); i++){
            auxA[i] = ptrA[j];
            j++; 
        }
        printf("\nNum A: ");
        for ( i = 0; i < strlen(ptrB); i++){
            printf("%c",auxA[i]);
        }
        printf("\nNum B: ");
        for ( i = 0; i < strlen(ptrB); i++){
            auxB[i] = ptrB[i];
            printf("%c",auxB[i]);
        }
        
    }else{
        tam = strlen(ptrB);
        auxA = (char*)malloc (tam*sizeof(char));
        auxB = (char*)malloc (tam*sizeof(char));
        printf("\nNum A: ");
        for ( i = 0; i < strlen(ptrA); i++){
            auxA[i] = ptrA[i];
            printf("%c",auxA[i]);
        }
        printf("\nNum B: ");
        for ( i = 0; i < strlen(ptrB); i++){
            auxB[i] = ptrB[i];
            printf("%c",auxB[i]);   
        }
    }
    int len = tam;
    printf("\nlen aux = %d",len);
    double lg =  log2(len);
    int lg2 = (int)lg;
    
    if ((lg - lg2) != 0)
    {
        printf("\nNo se potencia de 2");
        while ((lg - lg2) != 0)
        {
            len++;
            lg =  log2(len);
            lg2 = (int)lg;
        }
        printf("\nPotencia de 2 mas cercana: %d\n",len);
        num1 = (char*)malloc (len*sizeof(char));
        num2 = (char*)malloc (len*sizeof(char));
        int dif2 = len - tam;
        for (i = 0; i < dif2; i++){
            num1[i] = '0';
            num2[i] = '0';
        }
        int j=0;
        for ( i = dif2; i < len; i++){
            num1[i] = auxA[j];
            num2[i] = auxB[j];
            j++; 
        }
        printf("\nNum A: ");
        for ( i = 0; i < len; i++){
            printf("%c",num1[i]);
        }
        printf("\nNum B: ");
        for ( i = 0; i < len; i++){
            printf("%c",num2[i]);
        }
    }else
    {
        num1 = (char*)malloc (len*sizeof(char));
        num2 = (char*)malloc (len*sizeof(char));
        int i;
        for ( i = 0; i < len; i++)
        {
            num1[i] = ptrA[i];
            num2[i] = ptrB[i];
        }
        
        printf("\nSi es potencia de 2");
    }

    int result = multiplica(num1,num2,len,opt);

    if (opt == 16)
    {
        printf("\nR = %x",result);
    }else if (opt == 2)
    {
        printf("\nR = ");
        binario(result);
    }else{
        printf("\nR = %d",result);
    }
    
    
    free(ptrA);
    free(ptrB);

    return 0;
}
//Lectura de los numeros
char* lecturaCadena(){
    int s=1;
    char* ptrC = NULL;
    char c;
    setbuf(stdin, NULL);
	while((c=getchar())!='\n') 
	{
		ptrC=(char*)realloc(ptrC, sizeof(char)*s); 			
		ptrC[s-1]=(int)c; //asigna el valor de c al arreglo 
		s++; //Aumenta en 1 el contador
	}
    ptrC=(char*)realloc(ptrC, sizeof(char)*s);
    ptrC[s-1]='\0';
    return ptrC;
}
//Divide y venceras
int multiplica(char* num1,char* num2,int tam, int base){
    int ai,bi;
    if (tam == 1)
    {
        if ((int)num1[0] >= 97 && (int)num1[0] <= 102 )
        {
            if (num1[0] == 'a')
            {
                ai = 10;
            }else if (num1[0] == 'b')
            {
                ai = 11;
            }else if (num1[0] == 'c')
            {
                ai = 12;
            }else if (num1[0] == 'd')
            {
                ai = 13;
            }else if (num1[0] == 'e')
            {
                ai = 14;
            }else if (num1[0] == 'f')
            {
                ai = 15;
            }
            
        }else
        {
            char a = num1[0];
            ai= a - '0';
        }
        if ((int)num2[0] >= 97 && (int)num2[0] <= 102 )
        {
            if (num2[0] == 'a')
            {
                bi = 10;
            }else if (num2[0] == 'b')
            {
                bi = 11;
            }else if (num2[0] == 'c')
            {
                bi = 12;
            }else if (num2[0] == 'd')
            {
                bi = 13;
            }else if (num2[0] == 'e')
            {
                bi = 14;
            }else if (num2[0] == 'f')
            {
                bi = 15;
            }
        }else
        {
            char b = num2[0];
            bi= b - '0';
        }
        
        
        printf("\na = %c",ai);
        
        printf("\nb = %c",bi);
        
        int result = ai*bi;
        
        return result;
    }else
    {
        int i;

        char* xi=(char*)malloc ((tam/2)*sizeof(char));
        char* xd=(char*)malloc ((tam/2)*sizeof(char));
        char* yi=(char*)malloc ((tam/2)*sizeof(char));
        char* yd=(char*)malloc ((tam/2)*sizeof(char));
        int j = (int)tam/2;
        for ( i = 0; i < tam/2; i++)
        {
            xi[i] = num1[i];
            xd[i] = num1[j];
            yi[i] = num2[i];
            yd[i] = num2[j];
            j++;
        }

        printf("\nxi: ");
        for ( i = 0; i < tam/2; i++)
        {
            printf("%c",xi[i]);
        }
        printf("\nxd: ");
        for ( i = 0; i < tam/2; i++)
        {
            printf("%c",xd[i]);
        }
        printf("\nyi: ");
        for ( i = 0; i < tam/2; i++)
        {
            printf("%c",yi[i]);
        }
        printf("\nyd: ");
        for ( i = 0; i < tam/2; i++)
        {
            printf("%c",yd[i]);
        }

        int p1 = multiplica(xi,yi,tam/2,base);
        int p2 = multiplica(xi,yd,tam/2,base);
        int p3 = multiplica(xd,yi,tam/2,base);
        int p4 = multiplica(xd,yd,tam/2,base);

        double result = (pow(base, tam)*p1)+(pow(base, tam/2)*p2)+(pow(base, tam/2)*p3)+p4;
        return (int)result;
    }
}

void binario(int num)
{
    int aux; 
   if(num==0) 
      return; 

   aux=num%2; 
   num=num/2; 
   binario(num); 
   
   printf(" %d",aux); 
}