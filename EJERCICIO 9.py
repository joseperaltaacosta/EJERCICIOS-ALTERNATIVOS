#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)
num1=0
num2=0
num3=0
num1=int(input("Dime un número:"))
num2=int(input("Dime otro número:"))
num3=int(input("Dime el último número:"))
if (numero1>numero2) and (numero1>numero3):
    if (numero2>numero3):
        print("Los números de mayor a menor serían:", numero1, numero2, numero3)
    else:
        print("Los números de mayor a menor serían:", numero1, numero3, numero2)
if (numero2>numero1) and (numero2>numero3):
    if (numero1>numero3):
        print("Los números de mayor a menor serían:", numero2, numero1, numero3)
    else:
        print("Los números de mayor a menor serían:", numero2, numero3, numero1)        
if (numero3>numero1) and (numero3>numero2):
    if (numero1>numero2):
        print("Los números de mayor a menor serían:", numero3, numero1, numero2)
    else:
        print("Los números de mayor a menor serían:", numero3, numero2, numero1)    