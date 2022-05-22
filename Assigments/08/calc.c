#include <stdio.h> 
#include <math.h> 
int main()  
{  
    // declaracion de variables

    char opt;  
    int n1, n2;   
    float res; 
    double squareRoot; 

 // Integrantes: Javier Rehbein; Cristobal Galindo;
 // Asignatura: Lenguajes de Programacion;
 // Profesor: Cristhian Aguilera;
 // Trabajo: Assigment 08
    
    
    printf (" Elige una operacion(+, -, *, /): \n ");  
    scanf ("%c", &opt); // escanea el operador a usar  
    if (opt == '/' )  
    {  
        printf (" Has seleccionado: Division");  
    }  
    else if (opt == '*')  
    {  
        printf (" Has seleccionado: Multiplicacion");  
     }  
       
    else if (opt == '-')  
    {  
        printf (" Has seleccionado: Resta");  
     }  
        else if (opt == '+')  
    {  
        printf (" Has seleccioando: suma");  
     }     
    printf (" \n Ingresa el primero numero: ");  
    scanf(" %d", &n1); // toma primer valor  
    printf (" Ingresa el segundo numero: ");  
    scanf (" %d", &n2); // toma segundo valor  
      
    switch(opt)  // Que operacion se hara con los valores ingresados
    {  
        case '+':  
            res = n1 + n2; // suma  
            printf (" Suma entre %d y %d es: %.2f", n1, n2, res);

            // calculo del sqrt
            squareRoot = sqrt(res);
            printf(" \n La raiz cuadrada del resultado %.2lf es: %.2lf",res , squareRoot);

            break;  
          
        case '-':  
            res = n1 - n2; // resta 
            printf (" Resta entre %d y %d es: %.2f", n1, n2, res);

            // calculo del sqrt
            squareRoot = sqrt(res);
            printf(" \n La raiz cuadrada del resultado %.2lf es: %.2lf",res , squareRoot);

            break;  
              
        case '*':  
            res = n1 * n2; // multiplicacion  
            printf (" Multiplicacion entre %d y %d es: %.2f", n1, n2, res); 

            // calculo del sqrt
            squareRoot = sqrt(res);
            printf(" \n La raiz cuadrada del resultado %.2lf es: %.2lf",res , squareRoot);

            break;            
          
        case '/':  
            if (n2 == 0)   // if n2 == 0, usar otro valor  
            {  
                printf (" \n La division no puede ser de 0. Por favor escoge otro numero! "); 
                printf("\n Ingresa el segundo numero: "); 
                scanf ("%d", &n2);        
                }  
            res = n1 / n2; // division  
            printf (" la Division entre %d y %d es: %.2f", n1, n2, res);

            // calculo del sqrt
            squareRoot = sqrt(res);
            printf(" \n La raiz cuadrada del resultado %.2lf es: %.2lf",res , squareRoot);

            break;  
        default:  // Por si se ingresan valores no correspondidos  
            printf ("\n Ha ocurrido un error, por favor verifica las opciones seleccionadas. \n");               
    }  
    return 0;  
}  



