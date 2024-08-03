#Instrucciones

#1.   En la lista num_list cree un nuevo bucle for e imprima cada valor de la lista en orden secuencial. OK

#2.  Dentro del bucle for, cree una condición que busque todos los números que sean mayores que 45 e 
# imprima sólo los números que cumplan esa condición OK

#3.  Cambie la sentencia print por "Mayor de 45" y añada una condición else con una 
# sentencia print de "Menor de 45". OK

#4.  Actualice el bucle for para utilizar la función enumerar de forma que pueda obtener y 
# utilizar el índice. Modifique la condición para que busque el número 36 e imprima lo 
# siguiente 'Número encontrado en la posición: ', número índice OK

#5.  A continuación, cree una nueva variable llamada count, asígnele el valor 0 y 
# colóquela fuera del bucle for. OK

#6.  Dentro del bucle for incremente el contador en 1. OK 

#7.  Añada una sentencia print fuera del bucle for para imprimir el valor de la variable count. OK

#8.  Por último, añada una sentencia break directamente después de la 
# sentencia print dentro de la condición if para encontrar el número. OK

num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

def enumerar(n):
    count=0 
    for num in num_list:
        if (num > 45):
            print("Mayor que 45: ", num)
        else:
            print("Menor de 45: ", num)
        #-----------------------------------
        if(num==n):
            print('Número encontrado en la posición: ', num_list.index(num))
            break
        count +=1
    
    print(count)

enumerar(5)
