huevo = input("Tiene el ingrediente?(Sí/No)")
aceite = input("Tiene el aceite?(Sí/No)")
tiempoE = "no"
tiempoC = 0

if huevo.lower() == "si" and aceite.lower() == "si":
    print("1. Poner el aceite a calentar en la sarten y espera a que caliente")
    tiempoE = input("La sarten esta caliente?(Sí/No)")
    if tiempoE.lower() == "si":
        print("2.Rompe el huevo y sueltalo al interior de la sarten cuidadosamente")
        tiempoC = int(input("Cuantos minutos pasaron?"))
        if tiempoC >= 3:
            print("Saca el huevo de la sarte y sirvelo")
            print("El huevo esta listo.")
        else:
            print("Espera a que pasen 3 minutos")
    elif tiempoE.lower() == "no":
        print("Espera a que el aceite caliente")
    else:
        print("Respuesta invalida, responda si o no")

elif huevo.lower() == "no" or aceite.lower() == "no":
    print("Ve a la tienda mas cercana y compra lo necesario")
else:
    print("Respuesta invalida, responda si o no")
