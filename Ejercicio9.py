n = int(input("Ingresa un número: "))

pares = 0
impares = 0

for numero in range(1, n + 1):
    if numero % 2 == 0:
        pares = pares + numero
    else:
        impares = impares + numero

print("La suma de los pares es:", pares)
print("La suma de los impares es:", impares)