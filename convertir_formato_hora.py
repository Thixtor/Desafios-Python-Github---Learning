def normal_militar(hora):
    hora_modificada = hora.split(":")
   
    if "PM" in hora_modificada[1]:
        if int(hora_modificada[0]) != 12:
            hora_modificada[0] = int(hora_modificada[0]) + 12
            print (str(hora_modificada[0])+":"+hora_modificada[1][0:2])
        else: 
            print ("00"+":"+hora_modificada[1][0:2])

normal_militar("12:45PM")