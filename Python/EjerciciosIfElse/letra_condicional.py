lista = []

n_palabras = int(
    input("Introduce cuantas palabras deseas agregar a la lista:"))

for palabra in range(n_palabras):
    palabra = input("Introduzca la palabra " + str(palabra + 1) + ": ")
    lista.append(palabra)
    for palabra in lista:
        if palabra[0] == "A":
            palabrac = palabra
            print(palabrac)
