numero = int(input("Ingresa un número para generar la tabla de multiplicar: "))

for multiplicador in range(1, 11):
    print(numero, "x", multiplicador, "=", numero * multiplicador)
