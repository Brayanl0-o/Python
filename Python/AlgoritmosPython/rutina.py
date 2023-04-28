import datetime

hora_levantarme = datetime.time(7, 0)
entresemana = "si"
salir = datetime.time(7, 30)
hora_almuerzo = datetime.time(2, 0)
hora_volver = datetime.time(3, 0)
hora_salida = datetime.time(6, 0)

if hora_levantarme == datetime.time(7, 0) and entresemana.lower() == "si":
    print("Son las 7:00 am. Es Hora de levantarse!")
    print("Alistarme, desayunar y lavarme los dientes.")
    if salir == datetime.time(7, 30):
        print("Bajar la bicicleta e irme a trabajar.")
        print("Trabajar hasta las 2:00 pm")
        if hora_almuerzo == datetime.time(2, 0):
            print("Salir a almorzar y descansa hasta las 3:00 pm")
            if hora_volver == datetime.time(3, 0):
                print("Son las 3:00 pm. Vuelve al trabajo y trabaja hasta las 6:00 pm")
                if hora_salida == datetime.time(6, 0):
                    print("Puedes salir del trabajo")
                elif hora_salida > datetime.time(6, 30):
                    print(
                        "Ya termino tu hora de trabajo, comienzas a cobrar horas extras.")
                else:
                    print("Espera a que llegue la hora de salida.")
            elif hora_volver > datetime.time(3, 0):
                print("Corre a trabajar, ya paso tu hora de descanso.")
            else:
                print("Descansa hasta las 3:00 pm")
        else:
            print("Sigue trabajando hasta las 2:00 pm")
    else:
        print("Esperar hasta las 7:30 am")
elif hora_levantarme > datetime.time(7, 5):
    print("Levantarse que se hace tarde.")
elif entresemana.lower() == "no":
    print("Puedes seguir durmiendo es fin de semana.")
else:
    print("Puedes seguir durmiendo hasta las 7:00 am")
