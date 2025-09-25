#Ej1
def holamundo():
    print("Hola Mundo!")

holamundo()

#Ej2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Ingresa tu nombre:")
saludar_usuario(nombre)

#Ej3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingresa tu nombre:")
apellido = input("Ingresa tu apellido:")
edad = input("Ingresa tu edad:")
residencia = input("Ingresa tu residencia:")

informacion_personal(nombre, apellido, edad, residencia)

#Ej4
import math
def calcular_area_circulo(radio):
    area = math.pi * (radio**2)
    print(f"El area del circulo es : {area:.2f}")
def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perimetro del circulo es : {perimetro:.2f}")

radio = float(input("Ingrese el radio del circulo"))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#Ej5
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"Los segundos ingresados convertido a horas es: {horas} horas")

segundos = int(input("Ingresa la cantidad de segundos"))    
segundos_a_horas(segundos)

#Ej6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingresa el numero para conocer su tabla de multiplicacion"))
tabla_multiplicar(numero)

#Ej7
def operaciones_basicas(a, b):
    print(f"""
Suma: {a} + {b} = {a+b}
Resta: {a} - {b} = {a-b}
Multiplicacion: {a} x {b} = {a*b}
Division: {a} / {b} = {a/b}
""")

num1 = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el segundo numero"))    
operaciones_basicas(num1, num2)

#Ej8
def calcular_imc(peso, altura):
    print(f"IMC = {(peso / (altura**2)):.2f}")

peso = float(input("Ingrese el peso en kg"))
altura = float(input("Ingrese la altura en metros"))
calcular_imc(peso,altura)

#Ej9
def celsius_a_fahrenheit(celsius):
    print(F"La temperatura convertida a fahrenheit es de : {((celsius * (9/5)) + 32):.2f}")

temp = float(input("Ingrese la temperatura en celsius, ej: 26.5"))
celsius_a_fahrenheit(temp)    

#Ej10
def calcular_promedio(a, b, c):
    print(F"El promedio de los numeros ingresado es de : {(a+b+c) / 3}")

num1 = int(input("A continuacion ingresa 3 numeros \n num1: \n"))
num2 = int(input("num2: \n"))
num3 = int(input("num3: \n"))
calcular_promedio(num1, num2, num3)
