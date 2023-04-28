"""System module"""
edad = input("Introduce tu edad: ")
if edad.isdigit():
    edad = int(edad)
    if edad >= 60:
        print("Tiene descuento en su ticket.")
    elif edad >= 18:
        print("Es mayor de edad.")
    else:
        print("Es menor de edad, no puede entrar.")

    print("Edad comprobada.")
else:
    print("La edad comprobada no es un numero.")
