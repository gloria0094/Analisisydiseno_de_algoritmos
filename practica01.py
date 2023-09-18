#Liga del archivo reporte.pdf

import time
inicio=time.time()
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
fin=time.time()
tiempo1=fin-inicio
iniciol=time.time()
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
finl=time.time()
tiempo2=finl-iniciol
def menu():
    print("1. Ordenar con Burbuja")
    print("2. Ordenar con Selección")
    choice = input("Selecciona un método de ordenamiento (1 o 2): ")
    return choice

def main():
    choice = menu()
    size = int(input("Ingresa el tamaño de la lista: "))
    elements = [int(input(f"Ingresa el elemento {i+1}: ")) for i in range(size)]

    if choice == '1':
        bubble_sort(elements)
        print(tiempo1)
    elif choice == '2':
        selection_sort(elements)
        print(tiempo2)
    else:
        print("Opción no válida")
        return

    print("Lista ordenada:")
    print(elements)

if __name__ == "__main__":
    main()
