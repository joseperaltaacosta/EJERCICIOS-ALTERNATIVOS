#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
nom="pepe"
contr="asdasd"
nom_introducido=str(input("Dime el nombre de usuario:"))
contraseña_introducida=str(input("Dime la contraseña:"))
while (nom!=nom_introducido or contr!=contraseña_introducida):
    if(nom_introducido!=nom):
        print("Usuario incorrecto, intentalo de nuevo")
        nom_introducido=str(input("Dime el usuario:"))
    if (contraseña_introducida!=contr):
        print("Contraseña incorrecta")
        contraseña_introducida=str(input("Dime la contrseña de nuevo:"))
print("Usuario y contraseña correctas")