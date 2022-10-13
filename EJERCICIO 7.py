'''Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. 
Pueden ocurrir tres cosas:
-El exponente sea positivo, sólo tienes que imprimir la potencia.
-El exponente sea 0, el resultado es 1.
-El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.'''
base=0
exp=0
base=int(input("Dime el valor de la base:"))
exp=int(input("Dime el valor del exponente:"))
if exp>0:
    print(base,"^",exp,"=",base**exp) 
if exp==0:
    print(base,"^",exp,"= 1")
if exp<0:
    print(base,"^",exp,"= (1 /",base**-exp,")")