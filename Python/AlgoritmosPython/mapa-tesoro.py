print("Inicio")
print("Bienvenido a la isla del tesoro perdido apreciado viajero")
print("Tu primer desafío será elegir tu camino ")


camino = input("Camino subterraneo o terrestre? ")
if camino.lower() == "terrestre":
    print("Camino correcto!")
    print("Un elefante viene corriendo en tu direccion!! :OOO")
    correr_esconderse = input("Prefieres correr o esconderte? ")
    if correr_esconderse.lower() == "esconderse":
        print("El elefante sigue corriendo en esa dirección y se aleja.")
        direccion = input("Prefieres seguirlo o ir en sentido contrario? ")
        if direccion.lower() == "seguirlo":
            print("Hay un templo escondido en la vegetación y unas escaleras hacia abajo")
            decision_final = input(
                "Prefieres bajar las escaleras o entrar al templo? (Bajar/Entrar)")
            if decision_final.lower() == "bajar":
                print("Has Encontrado el tesoro. Enhorabuena!")
            elif decision_final.lower() == "entrar":
                print("Hay un jaguar, te ataca y te come. Game Over")
            else:
                print("Introduce un camino valido(bajar/ entrar)")
        elif direccion.lower() == "sentido contrario":
            print("Te pierdes y mueres. Game over")
        else:
            print("Introduce un camino valido(Seguirlo/ Sentido contrario)")
    elif correr_esconderse.lower() == "correr":
        print("El elefante te alcanza y te pisa. Game over")
    else:
        print("Introduce un camino valido(correr/ esconderse)")
elif camino.lower() == "subterraneo":
    print("Caes a varios metros de profundidad y mueres. Game Over")

else:
    print("Introduce un camino valido(Subterraneo/ Terrestre)")
