#12.Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto
#que también sea divisible por 400.

año = 0

año = int(input("Dime un año: \n"))

if ((año%4) and (año%400)):
    print ("Es año bisiesto")
elif (año%100):
    print ("No es año bisiesto")
