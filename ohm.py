#este programacalcula le ley de ohm
print("ley de ohm")
print("selecciona la opcion")
opcion=int(input("1=voltaje,2=corriente,3=reistencia"))
try:
    if opcion==1:
        corriente=float(input("ingresa la corriente en (ohm)(amperios)"))
        resistencia=float(input("ingresa la resistencia en ohmios"))
        voltaje=corriente*resistencia
        print("el voltaje es",voltaje,"voltios")
    elif opcion==2:
        voltaje=float(input("ingresa el voltaje en voltios"))
        resistencia=float(input("ingresa la resistencia en ohmios"))
        corriente=voltaje/resistencia
        print("la corriente es",corriente,(amperios))
    elif opcion==3:
        voltaje=float(input("ingresa el voltaje en voltios"))
        corriente=float(input("ingresa la corriente en (amperios):"))
        resistencia=voltaje/corriente
        print("la resistencia es",resistencia,"ohm")
    else:
        print("opcion no valida")
except ValueError:
    print("entrada no valida, por favor ingresa un numero")