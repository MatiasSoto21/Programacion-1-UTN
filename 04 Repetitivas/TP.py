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