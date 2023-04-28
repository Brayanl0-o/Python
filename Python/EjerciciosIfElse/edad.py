"""System module"""
edad = int(input("Introduce tu edad: "))
if edad >= 60:
    print("Tiene descuento en su ticket.")
elif edad >= 18:
    print("Es mayor de edad.")  # agregar if, typeoff
else:
    print("Es menor de edad, no puede entrar.")

print("Edad comprobada.")
