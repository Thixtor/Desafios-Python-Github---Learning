def normal_militar(hora):
    hora_modificada = hora.replace(":", " ").split()
   
    if hora_modificada[2] == "PM":
        hora_modificada[0] = int(hora_modificada[0]) + 12
        print (str(hora_modificada[0])+":"+hora_modificada[1])
    else: 
        print("La hora esta en formato 12 horas.")

normal_militar("10:45 AM")