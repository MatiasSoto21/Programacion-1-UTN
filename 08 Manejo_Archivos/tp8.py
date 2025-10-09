#Ej1
with open("productos.txt", "w") as archivo:
  texto = [
      "nombre,precio,cantidad\n",
      "lapiz,$15.00,20\n",
      "libro,$20.00,10\n",
      "goma,$5.00,100\n",
      "tijera,$15.50,17\n"
  ]
  archivo.writelines(texto)

#Ej2
with open ("productos.txt", "r") as archivo:
  columna = archivo.readline().strip().split(",")
  lineas = archivo.readlines()

  for i in lineas:
    valor = i.strip().split(",")
    for c,v in zip(columna, valor):
      print(c.capitalize()+":",v, end=" | ")
    print()

#Ej3
print("A continuacion agrege un nuevo producto: ")
nombre = input("nombre del producto: \n")
precio = input("precio del producto:$ \n")
cantidad = input("cantidad del producto: \n")
nuevo = f"{nombre},${precio},{cantidad}\n"

print(nuevo)
with open("productos.txt", "a") as archivo:
  archivo.write(nuevo)

with open ("productos.txt", "r") as archivo:
  columna = archivo.readline().strip().split(",")
  lineas = archivo.readlines()
  
  for i in lineas:
    linea = i.strip().split(",")
    print(f"{columna[0].capitalize()}: {linea[0]} | {columna[1].capitalize()}: {linea[1]} | {columna[2].capitalize()}: {linea[2]}") 


#Ej4
productos=[]

with open("productos.txt", "r")as archivo:
  columna = archivo.readline().strip().split(",")
  lineas = archivo.readlines()

  for i in lineas:
    linea = i.strip().split(",")
    dic = {}
    for c,v in zip(columna,linea):
      dic[c] = v
    productos.append(dic)  


#Ej5
busqueda = input("Ingrese un producto para buscar: \n")
encontrado = False
for i in productos:
  if busqueda in i.values():
    print("Producto Encontrado: ")
    print("Nombre:",i['nombre'], "| Precio:",i['precio'] ,"| Cantidad:",i['cantidad'])
    encontrado = True
    break
if not encontrado: print("ERROR, el producto no existe")


#Ej6
actualizacion = [
    "nombre,precio,cantidad\n"
]

for i in productos:
  linea = f"{i['nombre']},{i['precio']},{i['cantidad']}\n"
  actualizacion.append(linea)

with open("productos.txt", "w")as archivo:
  archivo.writelines(actualizacion)

with open("productos.txt", "r")as archivo:
  print(archivo.read())  