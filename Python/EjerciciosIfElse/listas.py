def main():
    lista1 = []
    lista2 = []

    nlist = int(
        input("Introduce cuantos numeros deseas agregar a las listas: "))

    for numero1 in range(nlist):
        numero1 = int(input("Introduce el numero " + str(numero1+1) + ":"))
        lista1.append(numero1)

    for numero2 in range(nlist):
        numero2 = int(input("Introduce el numero " + str(numero2+1) + ":"))
        lista2.append(numero2)
    lista3 = [x + y for x, y in zip(lista1, lista2)]
    print("La suma de las dos listas es:", lista3)


if __name__ == '__main__':
    main()
