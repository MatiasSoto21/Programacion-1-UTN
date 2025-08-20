#Ej5

contraseña: str  = str(input("Ingrese la contraseña"))

if (len(contraseña) >= 8 and len(contraseña) <=14 ):
    print("Contraseña valida")

else: print("Por favor, ingrese una contraseña entre 8 y 14")