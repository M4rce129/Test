# 1. if (si)
x = 10
if x > 5:
    print("x es mayor que 5")

# 2. if...else (si...sino)
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 3. if...elif...else (si...sino si...sino)
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bueno")
else:
    print("Necesitas mejorar")

# 4. Condicional simple en una línea (operador ternario)
estado = "aprobado" if nota >= 70 else "reprobado"
print("Estado:", estado)

# 5. Condicionales anidados
num = 15
if num > 0:
    if num % 2 == 0:
        print("Número positivo y par")
    else:
        print("Número positivo e impar")
else:
    print("Número no positivo")


