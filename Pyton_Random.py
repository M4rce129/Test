import random

# Ejemplos de uso de la librería random en Python con explicaciones en español

# 1. random.random(): genera un número flotante aleatorio entre 0.0 y 1.0
numero_aleatorio = random.random()
print("Número aleatorio entre 0 y 1:", numero_aleatorio)

# 2. random.randint(a, b): genera un número entero aleatorio entre a y b (inclusive)
entero_aleatorio = random.randint(1, 10)
print("Número entero aleatorio entre 1 y 10:", entero_aleatorio)

# 3. random.choice(lista): selecciona un elemento aleatorio de una lista
colores = ['rojo', 'verde', 'azul', 'amarillo'] 
color_elegido = random.choice(colores)
print("Color elegido aleatoriamente:", color_elegido)

# 4. random.shuffle(lista): mezcla los elementos de una lista en orden aleatorio
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print("Lista mezclada aleatoriamente:", numeros)

# 5. random.sample(lista, k): selecciona k elementos únicos aleatorios de una lista
muestra = random.sample(colores, 2)
print("Muestra aleatoria de 2 colores:", muestra)
