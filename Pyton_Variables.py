# Ejemplo de variables en Python
print(" STRING") # Variables de texto
texto = "Hola mundo"                            # Seteado
texto_usr = input("Escribe un texto: ")         # Desde usuario
print("Seteado:", texto, "| Usuario:", texto_usr, "| Tipo:", type(texto_usr))

print("\n INT (entero)") # Variables numéricas enteras
numero = 25                                      # Seteado
numero_usr = int(input("Escribe un número entero: "))
print("Seteado:", numero, "| Usuario:", numero_usr, "| Tipo:", type(numero_usr))

print("\n FLOAT (decimal)") # Variables numéricas decimales
decimal = 3.14
decimal_usr = float(input("Escribe un número decimal: "))
print("Seteado:", decimal, "| Usuario:", decimal_usr, "| Tipo:", type(decimal_usr))

print("\n BOOL (booleano)") # Variables booleanas (True/False)
valor_bool = True
entrada = input("¿Es cierto o falso? (True/False): ")
bool_usr = entrada.strip().capitalize() == "True"
print("Seteado:", valor_bool, "| Usuario:", bool_usr, "| Tipo:", type(bool_usr))

print("\n LIST (lista)") # Variables de tipo lista
mi_lista = ["rojo", "verde", "azul"]
lista_usr = input("Escribe 3 elementos separados por coma: ").split(",")
lista_usr = [e.strip() for e in lista_usr]
print("Seteado:", mi_lista, "| Usuario:", lista_usr, "| Tipo:", type(lista_usr))

print("\n TUPLE (tupla)") # Variables de tipo tupla (inmutables)
mi_tupla = (1, 2)
tupla_usr = tuple(input("Escribe dos valores separados por espacio: ").split())
print("Seteado:", mi_tupla, "| Usuario:", tupla_usr, "| Tipo:", type(tupla_usr))

print("\n DICT (diccionario)") # Variables de tipo diccionario (clave:valor)
mi_dict = {"nombre": "Ana", "edad": 16}
clave = input("Clave: ")
valor = input("Valor: ")
dict_usr = {clave: valor}
print("Seteado:", mi_dict, "| Usuario:", dict_usr, "| Tipo:", type(dict_usr))

print("\n SET (conjunto)") # Variables de tipo conjunto (sin duplicados)
mi_set = {1, 2, 3}
valores = input("Escribe números separados por espacio: ").split()
set_usr = {int(v) for v in valores}
print("Seteado:", mi_set, "| Usuario:", set_usr, "| Tipo:", type(set_usr))

print("\n NONE (nulo)") # Variables de tipo nulo (None)
mi_nulo = None
nulo_usr = input("¿Escribe algo o deja vacío?: ")
nulo_usr = nulo_usr if nulo_usr != "" else None
print("Seteado:", mi_nulo, "| Usuario:", nulo_usr, "| Tipo:", type(nulo_usr))


