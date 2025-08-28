#Ej1
for i in range (0, 101):
  print(i)

#Ej2
num:int = int(input("Ingrese un num"))
digitos:int = 0
if(num == 0):
  digitos = 1

while num >= 1:
  num = num / 10
  digitos += 1
print(f"La cantidad de digitos del numero es de: {digitos}")  

#Ej3
num1: int = int(input("Ingrese el número 1:"))
num2 : int = int(input("Ingrese el número 2:"))
suma : int = 0

if (num1 < num2):
  menor = num1
  mayor = num2
else:
  menor = num2
  mayor = num1

for i in range (menor+1, mayor):
  suma += i

print(f"La suma de los enteros comprendidos entre los 2 valores es de: {suma}")


#Ej4
opcion: int = 1
suma: int = 0

while opcion != 0:
  #VALIDAMOS QUE SEA UN ENTERO
 while True:
   resp= input("Ingrese numero entero a sumar:")
   try:
    num = int(resp)
    break
   except ValueError:
    print("Numero inválido, ingrese un entero: ")
 suma += num
  #VALIDAMOS QUE SEA UN ENTERO
 while True:
    resp = input("¿Seguir sumando? Digite numero correspondiente: 1)Si 0)No\n")
    try:
     opcion = int(resp)
     break
    except ValueError:
      print("Error, escriba 1 o 0")

print(f"La suma total es de: {suma}")


#Ej5
import random
intentos:int = 0
num_aleatorio: int = random.randint(0,9)

while True:
  #TRY/EXCEPT PARA VALIDAR QUE SEA UN ENTERO
  try:
   resp = input("Adivina el numero entre 0 y 9: ")
   adivinanza = int(resp)
   intentos += 1
   if(adivinanza == num_aleatorio):
    print (f"FELICITACIONES adivinaste el numero {num_aleatorio} en {intentos} intentos")
    break
   elif(adivinanza < num_aleatorio):
     print ("Mas grande!")
   elif(adivinanza > num_aleatorio):
     print ("Mas bajo!")
   else: print ("Intentalo de nuevo")
  except ValueError:
    print("Error, ingresa num entero")


 #Ej6
for i in range (100,-1, -2):
  print(i)


  