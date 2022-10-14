#1.Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

num1 = 0
num2 = 0

num1 = int (input("Dime un número: \n"))
num2 = int (input("Dime otro número: \n"))

if (num1<num2):
    print (f"{num2} es mayor que {num1}")
else:
    print (f"{num1} es mayor que {num2}")