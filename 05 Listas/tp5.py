#Ej1
lista = list(range(0,101, 4))
print (lista)

#Ej2
lista = ["mati", 1, True, False, "dos"]
print (lista[3])

#Ej3
lista = []
lista.append("hola")
lista.append("como")
lista.append("estas")

print(lista)

#Ej4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[len(animales)-1] = "oso"
print(animales)

#Ej5
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)
#Se inicia un array con 5 elementos numericos
#.remove(max(array)) elimina el mayor valor numerico dentro de esa lista.
#al finalizar se imprime la lista sin ese valor eliminado.

#Ej6
lista=list(range(10,31,5))
print(lista[0], lista[1])

#Ej7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = [1, True]
print(autos)

#Ej8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#Ej9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

compras[2].append("jugo")

compras[1][1] = "tallarines"

compras[0].remove("pan")

print(compras)

#Ej10

lista_anidada = []

lista_anidada.append(15)

lista_anidada.append(True)

lista_anidada.append([25.5, 57.9, 30.6])

lista_anidada.append(False)


print(lista_anidada)