#Interativo
import time
inicio=time.time()
def burbuja(ref):
    n = len(ref)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if ref[j] > ref[j+1]:
             ref[j], ref[j+1] = ref[j+1], ref[j]

entrada = input("Ingresa una lista de números separados por espacios: ")
lista = [int(x) for x in entrada.split()]

burbuja(lista)

print("Lista ordenada:")
print(lista)

fin=time.time()
tiempoDado=fin-inicio
print(tiempoDado)
    
