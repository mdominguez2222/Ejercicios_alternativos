#19.Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

numero = 0

numero = int(input("Dime un número: \n"))

if (numero==1 or 3 or 5 or 7 or 8 or 10 or 12):
    print ("El mes tiene 31 días")
elif (numero==4 or 6 or 9 or 11):
    print("El mes tiene 30 días")
elif (numero==2):
    print ("El mes puede tener 28 o 29 días")
else:
    print ("ERROR")