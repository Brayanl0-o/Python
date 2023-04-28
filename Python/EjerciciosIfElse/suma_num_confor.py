def main():
    lista = []
    suma = 0
    nlist = int(input("Introduce cuantos numeros deseas agregar a la lista: "))
    for numero in range(nlist):
        numero = int(input("Introduce el numero " + str(numero+1) + ":"))
        lista.append(numero)
    for numero in lista:
        suma += numero
    print("La suma de la lista es: ", suma)


if __name__ == '__main__':
    main()
