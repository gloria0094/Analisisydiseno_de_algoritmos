# Analisisydiseno_de_algoritmos
Códigos de la materia 
def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

numero = 5
resultado = factorial(numero)
print("El factorial de 5 es: ", resultado)
