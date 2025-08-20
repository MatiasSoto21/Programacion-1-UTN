#Ej 6

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"moda={moda}, mediana={mediana}, media={media}")

if (moda == mediana and moda == media):
    print("Sin sesgo")

elif (media > mediana and mediana > moda):
    print("Sesgo positivo o a la derecha")

elif (media < mediana and mediana < moda):
    print("Sesgo negativo o a la izquierda")