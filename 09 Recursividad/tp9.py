#Ej1
def factorial (num):
  if num == 0:
    return 1
  else :
    return num * factorial(num-1)

print("Se va a calcular el factorial entre 1 y el numero que ingrese:")
res= int(input("Ingrese el numero: "))
for i in range(res):
  fact = factorial(i+1)
  print (f"{i+1}! = {fact}")

#Ej2
def fibonacci(n):
  if n <= 1:
      return n
  else:
      return fibonacci(n-1) + fibonacci(n-2)
pos = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

for i in range(pos + 1):
    print(f"{i}: {fibonacci(i)}")

#Ej3
def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)

print(f"{base} elevado a la {exponente} es: {resultado}")

#Ej4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"

    cociente = n // 2
    resto = n % 2

    return decimal_a_binario(cociente) + str(resto)

numero = int(input("Ingrese un número entero positivo: "))
binario = decimal_a_binario(numero)

print(f"El número {numero} en binario es: {binario}")

#Ej5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True

    if palabra[0] != palabra[-1]:
        return False

    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra sin espacios ni tildes: ").lower()
print("¿Es palíndromo?:", es_palindromo(texto))

#Ej6
def suma_digitos(n):
    if n < 10:
        return n

    ultimo = n % 10
    resto = n // 10

    return ultimo + suma_digitos(resto)

numero = int(input("Ingrese un número entero positivo para sumar sus digitos: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")

#eEj7
def contar_bloques(n):
    if n == 1:
        return 1

    return n + contar_bloques(n - 1)

numero = int(input("Ingrese la cantidad de bloques del nivel más bajo: "))
total = contar_bloques(numero)
print(f"Total de bloques necesarios: {total}")

#Ej8
def contar_digito(numero, digito):
   
    if numero < 10:
        return 1 if numero == digito else 0

    ultimo = numero % 10
    resto = numero // 10

    return (1 if ultimo == digito else 0) + contar_digito(resto, digito)

num = int(input("Ingrese un número entero positivo: "))
d = int(input("Ingrese el dígito a buscar (0-9): "))

resultado = contar_digito(num, d)
print(f"El dígito {d} aparece {resultado} veces en el número {num}.")