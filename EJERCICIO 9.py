#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)
num1=0
num2=0
num3=0
num1=int(input("Dime un número:"))
num2=int(input("Dime otro número:"))
num3=int(input("Dime el último número:"))
if (num1>num2) and (num1>num3 and num2>num3):
    
    print("Los números ordenados de mayor a menor son: ", num1,",",num2,",",num3)

elif (num2>num1) and (num2>num3 and num1>num3):
    print("Los números ordenados de mayor a menor son: ", num2,",",num1,",",num3)

else:
    print("Los números ordenados de mayor a menor son: ", num3,",",num1,",",num2)