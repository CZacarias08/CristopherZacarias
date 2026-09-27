numero = int(input("Ingresa un número entero: "))

numero = abs(numero)
contador = 0

if numero == 0:
    contador = 1
else:
    while numero > 0:
        numero = numero // 10
        contador = contador + 1

print("El número tiene", contador, "dígitos")