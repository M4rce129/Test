# Ejemplos de uso de archivos en Python con explicaciones en español

# 1. Abrir un archivo en modo escritura ('w') y escribir contenido
archivo = open('ejemplo.txt', 'w')  # Crea el archivo o lo sobrescribe si ya existe
archivo.write('Primera línea de texto.\n')  # Escribe una línea
archivo.write('Segunda línea de texto.\n')  # Escribe otra línea
archivo.flush()  # Fuerza la escritura inmediata en el disco
archivo.close()  # Cierra el archivo manualmente

# 2. Abrir el archivo en modo lectura ('r') y leer su contenido
archivo = open('ejemplo.txt', 'r')  # Abre el archivo para leer
contenido = archivo.read()  # Lee todo el contenido del archivo
print('Contenido leído del archivo:')
print(contenido)
archivo.close()  # Cierra el archivo después de leer

# 3. Usar 'with open()' para manejar archivos automáticamente
# Esta forma es más segura porque cierra el archivo automáticamente
with open('ejemplo.txt', 'a') as archivo:  # Abre en modo agregar (append)
    archivo.write('Tercera línea agregada con with open().\n')  # Agrega una línea

# 4. Leer línea por línea usando 'with open()'
with open('ejemplo.txt', 'r') as archivo:
    print('Leyendo línea por línea:')
    for linea in archivo:
        print(linea.strip())  # strip() elimina el salto de línea al final
