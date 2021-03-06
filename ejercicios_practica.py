#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuante cuantos números ingresados hay y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''

    inicio = int(input("ingrese el primer numero de la secuencia\n")) 
    fin = int(input("ingrese el siguiente numero de la secuencia\n")) 

    cantidad_numeros = 0
    sumatoria = 0
    numero = 0

    lista = list(range(inicio, fin))
    print("la secuencia ingresada es", lista) # agregue la impresion de la lista

    for numero in lista:
        sumatoria += numero    # bucle.....

    for numero in lista:
        cantidad_numeros += 1

    promedio = sumatoria / cantidad_numeros
    print("el promedio de la secuencia es", promedio)   

    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros

    # Imprimir resultado en pantalla


def ej2():
    print("Mi Calculadora (^_^)")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''
    while True:

      numero_1 = float(input("Ingrese el primer numero: \n"))
      numero_2 = float(input("ingrese el segundo numero: \n"))

      print("ingrese la operacion que desea realizar")
  
      operacion = input()
      suma = numero_1 + numero_2
      resta = numero_1 - numero_2
      multiplicacion = numero_1 * numero_2
      division = numero_1 / numero_2
      potencia = numero_1 ** numero_2

      if operacion == "+":
        print("la suma es",suma)
      elif operacion == "-":
        print("la resta es:",resta) 
      elif operacion == "*":
        print("la multiplicacion es:",multiplicacion)
      elif operacion == "/":
        print("la division es:",division)
      elif operacion == "**":
        print(numero_1,"elevado a",numero_2,"es:",potencia)
        
      if operacion == "FIN":
        break

      if operacion != "+" and operacion != "-" and operacion != "*" and operacion !="/" and operacion !="**":
        print("El operador ingresado no es correcto")
        break

      





def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe caluclar el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''
  
    
    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    
    sumatoria = 0           # Ya le hemos inicializado en 0

    cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
    cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo


    for nota in notas:
      if nota >= 0:
        sumatoria += nota
      if nota >+ 0:
        cantidad_notas += 1
      if nota < 0:
        cantidad_ausentes += 1 

    promedio = sumatoria / cantidad_notas
    print("El promedio es:", promedio)

    if promedio >= 90:
        print("A")
    elif promedio >= 80:
        print("B")
    elif promedio >= 70:
        print("C")
    elif promedio >= 60:
        print("D") 
    else:
        print("F")
    
    print("Cantidad de ausentes:", cantidad_ausentes)

    # Realice aquí el bucle para recorrer todas las notas
    
    # y cacular la sumatoria

    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas

    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado

    # Imprima en pantalla al cantidad de ausentes


def ej4():
    print("Mi primer pasito en data analytics")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento

    En este ejercicio se lo provee de una lista de temperaturas,
    esa lista de temperaturas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted
    '''

    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

    # Colocar el bucle aqui......

    for temp in temp_dataloger: # sumatoria de las temperaturas por bucle
      temperatura_sumatoria += temp

    for temp in temp_dataloger:
      temperatura_len += 1  

    for temp in temp_dataloger: # temperatura maxima
      if (temperatura_max is None) or (temp >= temperatura_max):
        temperatura_max = temp
        

    for temp in temp_dataloger: # temperatura inima
      if (temperatura_min is None) or (temp < temperatura_min):
        temperatura_min = temp   

    temperatura_promedio = temperatura_sumatoria / temperatura_len
    
    maxima = max(temp_dataloger)
    minima = min(temp_dataloger)

    print("La temperatura maxima por bucle es", temperatura_max) 
    print("La temperatura maxima con funcion max es", maxima)
    print("La temperatura minima por bucle es", temperatura_min) 
    print("La temperatura minima con funcion min es", minima)
    

    sumatoria = 0
    cuenta_temp = 0
    
    sumatoria = sum(temp_dataloger)
    cuenta_temp = len(temp_dataloger)
    promedio_temp = sumatoria / cuenta_temp
    
    print("La temperatura promedio por bucle es", temperatura_promedio)
    print("La temperatura promedio calculada con max y cuenta es", promedio_temp)

    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp
    
    if (temperatura_min >= 19) and (temperatura_max <= 28):
      print("Nos encontramos en verano")
    elif (temperatura_min >= 11) and (temperatura_max <= 24):
      print("Nos encontramos en otoño")
    elif (temperatura_min >= 8) and (temperatura_max <= 14):
      print("Nos encontramos en invierno")
    elif (temperatura_min >= 10) and (temperatura_max <= 24):
      print("Nos encontramos en primavera")
    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 24
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''

    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")

  '''
    
    while True:

      print("Menu:")
      print("1 - Ordenar por orden alfabético")
      print("2 - Ordenar por cantidad de letras")
      print("3 - Salir del programa")

      print("Elija la operacion que desea realizar")

      numero_menu = int(input())

      if numero_menu == 3:
        print("El programa ha acabado")
        break
      if numero_menu != 1 and numero_menu != 2:
        print("La opcion ingresada no es correcta. Vuelva a intentar")
        continue

      print("Ingrese 4 palabras")

      palabra_1 = str(input())
      palabra_2 = str(input())
      palabra_3 = str(input())
      palabra_4 = str(input())
      lista = []

      lista.append(palabra_1)
      lista.append(palabra_2)
      lista.append(palabra_3)
      lista.append(palabra_4)
      
      palabra_max = None
      palabra_letras = None
    
      if numero_menu == 1:
        for palabra in lista:
          if (palabra_max is None) or (palabra > palabra_max):
            palabra_max = palabra

      if numero_menu == 2:
        for palabra in lista:
          if (palabra_letras is None) or (len(palabra) > len(palabra_letras)):
            palabra_letras = palabra
     
      if numero_menu == 1:
        print("la palabra max es:",palabra_max)
      if numero_menu == 2:
        print("La palabra con mayores letras es:", palabra_letras)      




        


      



      
if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
