# 1. CICLO WHILE
# Ejecuta un bloque de código mientras la condición sea verdadera.

i = 0
while i < 10:           # Mientras i sea menor que 10
    print(i, "While")   # Imprime el valor actual de i y la palabra "While"
    i += 1              # Incrementa i en 1 para evitar ciclo infinito

# 2. CICLO FOR
# Recorre una secuencia o rango de valores.

for v in range(10):      # Recorre desde 0 hasta 9 (10 no incluido)
    print(v, "For")      # Imprime el valor actual de v y la palabra "For"

# El rango puede ser personalizado: range(inicio, fin, paso)
for x in range(5, 15, 2):   # Desde 5 hasta 14, saltando de 2 en 2
    print(x, "For personalizado")

# 3. CICLO FOR sobre listas
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Fruta:", fruta)

# 4. CICLO WHILE con condición de salida
respuesta = ""
while respuesta.lower() != "salir":
    respuesta = input("Escribe 'salir' para terminar: ")
    print("Dijiste:", respuesta)

# 5. CICLO FOR con else
for numero in range(3):
    print("Número:", numero)
else:
    print("¡Bucle for terminado!")

# 6. CICLO WHILE con else
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1
else:
    print("¡Bucle while terminado!")

