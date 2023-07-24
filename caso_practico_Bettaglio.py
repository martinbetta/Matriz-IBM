import random #se importa random para poder utilizarlo en el código junto con randint

def obtener_numero_entero_positivo():#ingreso de N pra armar la matriz 
    while True: #While hasta que sea True segun las condiciones debajo
        N = input("Ingrese un número entero positivo para armar su Matriz: ") #input donde se solicita la matriz
        if N.isdigit() and int(N) > 0: #Validador si es un número y si es un numero mayor a 0
            return int(N) #Los input son string, por lo que lo tenemos que pasar a integer para que sea manipulable matemáticamente
        else:
            print("Error: Por favor, ingrese un número entero positivo válido.")#si es invalido, además de volver a pedir número informa un error

def generar_y_imprimir_matriz(N):
    matriz = [] #Genera lista vacía "matriz" para luego ir ingresando según el input
    for i in range(N): #Loop n sobre range del input N  
        fila = [random.randint(0, 9) for _ in range(N)] #Genera la variable fila donde usando random.randint en forma aleatoria de 0 a 9 N cantidad de filas  
        matriz.append(fila) #con append ingresamos los datos dentro de la lista matriz
    print("*"*50) #separador    
    print(f"\nMatriz generada de: {N} filas y columnas\n") #titulo
    for fila in matriz: #los arreglos se los ubica uno debajo del otro para que forme la Matriz y sus columnas
        print(fila) #para que imprima en filas 
    return matriz # retorno la lista matriz para usarla en otra función
 
def calcular_sumas(matriz): # segunda parte del ejercicio, Sumas filas y columnas de la Matriz
    sumas_filas = [sum(fila) for fila in matriz] #suma filas de la matriz
    sumas_columnas = [sum(columna) for columna in zip(*matriz)] # suma columnas, el zip y el * en matriz me transpone la Matriz para cambiar el sentido del loop y tenes la suma
    print("\nSuma de cada fila:\n")
    print(sumas_filas) # imprimo resultado de suma de filas
    print("\nSuma de cada columna:\n")
    print(sumas_columnas) # imprimo resultado de suma de columnas
    print("\nFin de Ejercicio")
    print("*"*50)  
    

def inicio(): # Función base donde arranca la ejecución
    N = obtener_numero_entero_positivo() #Se ejecuta la función con input y validadores 
    matriz = generar_y_imprimir_matriz(N) #Basado en los datos de N en el input se genera la matriz.
    calcular_sumas(matriz) # Se ejecuta la función para ejecutar la la suma tanto de columnas como de filas.
inicio() #inicio del programa
