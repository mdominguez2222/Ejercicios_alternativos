#9.Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)

vNumeros = []

num1 = int(input("Dime un número: \n"))
num2 = int(input("Dime otro número: \n"))
num3 = int(input("Dime otro número: \n"))

vNumeros.append(num1)
vNumeros.append(num2)
vNumeros.append(num3)
vNumeros.sort(reverse=True)

print (vNumeros)