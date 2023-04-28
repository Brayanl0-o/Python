import datetime

hora_levantarme = datetime.time(7, 0)
entresemana = "si"
salir = datetime.time(7, 30)
hora_almuerzo = datetime.time(13, 0)
hora_volver = datetime.time(15, 0)
hora_salida = datetime.time(18, 0)

levantarse = hora_levantarme == datetime.datetime.now(
).time() and entresemana.lower() == "si"
trabajar = salir <= datetime.datetime.now().time(
) < hora_almuerzo or hora_volver <= datetime.datetime.now().time() < hora_salida
descansar = hora_almuerzo <= datetime.datetime.now().time() < hora_volver

if levantarse:
    print("Son las 7:00 am. Es Hora de levantarse!")
    print("Alistarme, desayunar y lavarme los dientes.")
elif trabajar:
    if salir <= datetime.datetime.now().time() < hora_almuerzo:
        print("Bajar la bicicleta e irme a trabajar.")
        print("Trabajar hasta las 2:00 pm")
    else:
        print("Son las 3:00 pm. Vuelve al trabajo y trabaja hasta las 6:00 pm")
        if datetime.datetime.now().time() >= hora_salida:
            print("Puedes salir del trabajo")
        else:
            print("Espera a que llegue la hora de salida.")
elif descansar:
    print("Salir a almorzar y descansa hasta las 3:00 pm")
else:
    print("Puedes seguir durmiendo")
