# 1. Función sin parámetros
def saludar():
    print("¡Hola, mundo!")

saludar()


# 2. Función con parámetros
def saludar_persona(nombre):
    print(f"Hola, {nombre}!")

saludar_persona("Ana")


# 3. Función que retorna un valor
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print("Resultado de sumar:", resultado)


# 4. Función con valor por defecto
def saludar_con_default(nombre="invitado"):
    print(f"Bienvenido, {nombre}")

saludar_con_default()
saludar_con_default("Luis")


# 5. Función que pide datos al usuario
def pedir_datos_usuario():
    nombre = input("¿Cómo te llamas? ")
    edad = int(input("¿Cuántos años tienes? "))
    return nombre, edad

nombre_usuario, edad_usuario = pedir_datos_usuario()
print(f"Tu nombre es {nombre_usuario} y tienes {edad_usuario} años.")
