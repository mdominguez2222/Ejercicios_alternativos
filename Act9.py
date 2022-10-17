#9.Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)

vNumeros = []

num1 = int(input("Dime un número: \n"))
num2 = int(input("Dime otro número: \n"))
num3 = int(input("Dime otro número: \n"))

vNumeros.append(num1)          #o así: vNumeros.append(int(input("Dime un número: \n"))) 
vNumeros.append(num2)
vNumeros.append(num3)
vNumeros.sort(reverse=True)

print (vNumeros)
print("El mayor es", vNumeros[0])  #o así: print(max(vNumeros))

ultimo = len(vNumeros)
print("El menor es", vNumeros[ultimo-1])