#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
nom_introducido=str(input("Dime el nombre de usuario:"))
contraseña_introducida=str(input("Dime la contraseña:"))
if(nom_introducido=="pepe" and (contraseña_introducida=="asdasd")):
    print("Has entrado al sistema")
else:
    print("Usuario o contraseña incorrectos")