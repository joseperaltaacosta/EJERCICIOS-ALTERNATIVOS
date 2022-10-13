#Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.
num1=0
num2=0
num1=int(input("Dime un número: "))
num2=int(input("Dime otro número: "))
if num1>num2:
    print("El número", num1, "es mayor que el número", num2)
else:
    print("El número", num2, "es mayor que el número", num1)