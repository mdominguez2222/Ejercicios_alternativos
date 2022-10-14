#2.Algoritmo que pida un número y diga si es positivo, negativo o 0

num = 0

num = int(input("Dime un número: \n"))

if (num==0):
    print ("El número es 0")
elif (num<0):
    print ("El número es negativo")
else:
    print ("El número es positivo")