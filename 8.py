#Ej8

nombre : str = str(input("Ingrese su nombre: "))
print("1: Nombre en Mayus\n2: Nombre en Minus\n3: Primer letra mayus")
opcion : int = int(input("Ingrese opcion: "))

def casos (arg):
  if arg == 1:
    print(nombre.upper())

  elif arg == 2:
    print(nombre.lower())

  elif arg == 3:
    print(nombre.title())
  else:
    print("opcion no valida")

casos(opcion)