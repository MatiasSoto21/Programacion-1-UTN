#Ej4

edad:int = int(input("ingrese su edad"))

if (edad >=0 and edad < 12):
    print("Niño/a")

elif (edad >= 12 and edad < 18):
    print("Adolescente")

elif (edad >= 18 and edad < 30):
    print("Adulto/a joven")

elif (edad >= 30 and edad < 100):
    print("Adulto/a")

else: print("Ingrese una edad valida")