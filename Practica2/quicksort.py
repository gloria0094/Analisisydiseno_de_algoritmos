import random
import numpy as np
import matplotlib.pyplot as plt
import timeit

def arreglo_aleatorio(tamano):
    return [random.randint(1, 1000) for _ in range(tamano)]       

def quicksort(arr):
    if len(arr)<=1:
        return arr
    
    pivote = sum(arr) / len(arr)
    menor = []
    mayor = []
    igual =[]

    for i in range(len(arr)):
        if arr[i]<pivote:
            menor.append(arr[i])
        elif arr[i]==pivote:
            igual.append(arr[i])
        else:
            mayor.append(arr[i])
    return quicksort(menor) + igual + quicksort(mayor)
    

n = 100
longitud_Arreglos = [random.randint(1,n ) for i in range(100)]
x_valores = []
y_valores = []


for i, tamano in enumerate(longitud_Arreglos,1):
    arr=arreglo_aleatorio(tamano)
    print(f"Arreglo {i} original {tamano}: {np.array(arr)}")
    time= timeit.timeit(lambda:quicksort(arr),number=1000)
    x_valores.append(tamano)
    y_valores.append(time)
    print(f"Arreglo {i} ordenado {tamano}:{np.array(quicksort(arr))}")
    print(f"Tiempo del arreglo: {time} ")

plt.plot(x_valores)
plt.xlabel('Longitud del arreglo')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento de Quicksort para los arreglos')
plt.show()
