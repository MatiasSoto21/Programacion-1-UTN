#Ej1
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva':1450
    }

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ej2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#Ej3
lista_frutas = []

for clave, valor in precios_frutas.items():
  lista_frutas.append(clave)

#Ej4
contactos = {}

def agregar_contacto(name, num):
  contactos[name] = num

def existe(consulta):
  if consulta in contactos.keys():
    print(f" {consulta}: {contactos[consulta]}")
  else: print("El contacto no existe")

nombre = input("Ingresa el nombre de la persona: ")
numero = input("Ingresa su numero telefonico: ")

agregar_contacto(nombre, numero)

consulta = input("Ingresa el nombre del contacto para consultar su numero: ")

existe(consulta)  

#Ej5
frase = input("Escriba una frase: ").split()
palabras_unicas = set(frase)
dicc = {}

print(f"Palabras unicas: {palabras_unicas}")

for i in palabras_unicas:
  dicc[i] = frase.count(i)

print(f"Recuento, {dicc}")

#Ej6
nombres = []
alumnos = {}

for i in range(3):
  alumno = input("Ingrese el nombre del alumno: ")
  nombres.append(alumno)
  aux = []

  for x in range(3):
    nota = input(f"Ingrese la nota numero{x+1}: ")
    aux.append(float(nota))

  alumnos[alumno] = tuple(aux)

print(alumnos)

for clave, valor in alumnos.items():
  promedio = sum(valor) / len(valor)
  print(f"El promedio de {clave} es : {promedio:.2f}")


#Ej7 No entendi la consigna, la encontre confusa.

#Ej8
stock = {
    "coca": 23,
    "pesi": 20,
    "lays": 25,
    "pan lactal": 15
}
bandera: bool = True

def consultar():
  consulta = input("Ingrese el producto a consultar: ")
  while consulta == "":
    print("Error ingrese un nombre valido")
    consulta = input("Ingrese el producto a consultar: ")
  if consulta in stock:
    return f"{consulta}: {stock[consulta]}"
  else: return "El producto ingresado no existe"

def agregar():
  consulta = input("Ingrese el producto a añadir unidades: ")
  if consulta in stock:
    añadir = input("Ingrese la cantidad de unidades para agregar al stock: ")
    while añadir == "" or añadir.isalpha() or int(añadir) < 1:
      print("Error añadir un valor positivo")
      añadir = input("Ingrese la cantidad de unidades para agregar al stock: ")
    stock[consulta] += int(añadir)
    return print(f"{consulta} ahora tiene {stock[consulta]} unidades.")
  else: return print("El producto ingresado no esta en stock. ")


while bandera:
  respuesta = input("""
  Opciones
  1)Consultar stock de un producto
  2)Agregar unidades a stock de un producto
  3)Agregar un nuevo producto
  4)Salir
  """)

  if respuesta == "1":
    print(consultar())

  elif respuesta == "2":
    agregar()

  elif respuesta == "3":
    nuevo = input("Ingresa el nuevo producto: ")
    if nuevo not in stock:
      stock[nuevo] = 0
      cantidad= input("Ingresa la cantidad de unidades: ")
      stock[nuevo] = int(cantidad)
    else: print("El producto ya esta en stock.")

  elif respuesta == "4":
    bandera = False
    print("ADIOS!")

  else: print("Opcion no valida, intente de nuevo")

#Ej9

agenda = {
    ("lunes", "14:30"): "Clase",
    ("lunes", "17:00"): "ingles",
    ("sabado", "10:00"): "Asado",
    ("domingo", "9:00"): "Iglesia"
}

def consultar_actividad(dia, hora):
  if (dia, hora) in agenda:
    print(f"La actividad de la consulta es: {(dia,hora)} : {agenda[(dia,hora)]}")
  else: print("No hay ninguna actividad para la hora y dia.")

dia = input("Ingresa el dia para la consulta: ")
hora = input("Ingresa la hora para la consulta: ")

consultar_actividad(dia,hora)

#Ej10
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia"
}

invertido = {}
for clave,valor in paises_capitales.items():
  invertido[valor] = clave

print(invertido)