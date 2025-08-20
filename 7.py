#Ej7

frase : str = str(input("Ingrese una frase: "))
ult = frase[len(frase)-1].lower()

if( ult in "aeiou"):
   print(f"{frase}!")
else:
   print(frase)