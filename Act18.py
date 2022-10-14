#18.Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.

numero = 0

numero = int (input("Dime un número:\n"))

if (numero==1):
    print ("Es lunes")
elif (numero==2):
    print ("Es martes")
elif (numero==3):
    print ("Es miércoles")
elif (numero==4):
    print ("Es jueves")
elif (numero==5):
    print ("Es viernes")
elif (numero==6):
    print ("Es sábado")
elif (numero==7):
    print ("Es domingo")
else:
    print("ERROR")