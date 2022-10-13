#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
letra=str(input("Escribe una letra:"))

if letra.isupper()==True:
    print("El carácter introducido es mayúcula")
else:
    print("El carácter introducido es minúscula")