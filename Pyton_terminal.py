# 1: Negrita o alto brillo
print("\033[1m>>HelloWorld (bold)\033[0m")

# 2: Texto tenue
print("\033[2m>>HelloWorld (dim)\033[0m")

# 3: Cursiva (no siempre funciona)
print("\033[3m>>HelloWorld (italic)\033[0m")

# 4: Subrayado
print("\033[4m>>HelloWorld (underline)\033[0m")

# 5: Parpadeo lento (no funciona en muchas terminales)
print("\033[5m>>HelloWorld (slow blink)\033[0m")

# 6: Parpadeo rápido (rara vez soportado)
print("\033[6m>>HelloWorld (rapid blink)\033[0m")

# 7: Inversión de colores (fondo/texto)
print("\033[7m>>HelloWorld (reverse)\033[0m")

# 8: Oculto (texto invisible)
print("\033[8m>>HelloWorld (hidden)\033[0m")

# 9: Tachado
print("\033[9m>>HelloWorld (strikethrough)\033[0m")

# 10: Fuente predeterminada (sin cambios visibles)
print("\033[10m>>HelloWorld (default font)\033[0m")

# 11–19: Alternativas de fuente (normalmente ignoradas)
print("\033[11m>>HelloWorld (font 1)\033[0m")
print("\033[12m>>HelloWorld (font 2)\033[0m")
print("\033[13m>>HelloWorld (font 3)\033[0m")
print("\033[14m>>HelloWorld (font 4)\033[0m")
print("\033[15m>>HelloWorld (font 5)\033[0m")
print("\033[16m>>HelloWorld (font 6)\033[0m")
print("\033[17m>>HelloWorld (font 7)\033[0m")
print("\033[18m>>HelloWorld (font 8)\033[0m")
print("\033[19m>>HelloWorld (font 9)\033[0m")

# 20: Fraktur (no soportado)
print("\033[20m>>HelloWorld (fraktur)\033[0m")

# 21: Negrita desactivada o doble subrayado (según terminal)
print("\033[21m>>HelloWorld (bold off / double underline)\033[0m")

# 22: Reset de negrita y tenue
print("\033[22m>>HelloWorld (normal intensity)\033[0m")

# 23: Quitar cursiva
print("\033[23m>>HelloWorld (not italic)\033[0m")

# 24: Quitar subrayado
print("\033[24m>>HelloWorld (not underlined)\033[0m")

# 25: Quitar parpadeo
print("\033[25m>>HelloWorld (not blinking)\033[0m")

# 26: No definido / sin efecto visible
print("\033[26m>>HelloWorld (reserved/undefined)\033[0m")

# 27: Quitar inversión de colores
print("\033[27m>>HelloWorld (positive image)\033[0m")

# 28: Mostrar texto (quitar oculto)
print("\033[28m>>HelloWorld (not hidden)\033[0m")

# 29: Quitar tachado
print("\033[29m>>HelloWorld (not strikethrough)\033[0m")

# 30–37: Colores de texto estándar (negro a blanco)
print("\033[30m>>HelloWorld (black text)\033[0m")
print("\033[31m>>HelloWorld (red text)\033[0m")
print("\033[32m>>HelloWorld (green text)\033[0m")
print("\033[33m>>HelloWorld (yellow text)\033[0m")
print("\033[34m>>HelloWorld (blue text)\033[0m")
print("\033[35m>>HelloWorld (magenta text)\033[0m")
print("\033[36m>>HelloWorld (cyan text)\033[0m")
print("\033[37m>>HelloWorld (white/gray text)\033[0m")

# 38: Color extendido (requiere parámetros adicionales, no visible así)
print("\033[38m>>HelloWorld (extended foreground – incomplete)\033[0m")

# 39: Reset del color de texto
print("\033[39m>>HelloWorld (default text color)\033[0m")

# 40–47: Fondo de color estándar (negro a blanco)
print("\033[40m>>HelloWorld (black background)\033[0m")
print("\033[41m>>HelloWorld (red background)\033[0m")
print("\033[42m>>HelloWorld (green background)\033[0m")
print("\033[43m>>HelloWorld (yellow background)\033[0m")
print("\033[44m>>HelloWorld (blue background)\033[0m")
print("\033[45m>>HelloWorld (magenta background)\033[0m")
print("\033[46m>>HelloWorld (cyan background)\033[0m")
print("\033[47m>>HelloWorld (white/gray background)\033[0m")

# 48: Fondo extendido (incompleto si no se dan más argumentos)
print("\033[48m>>HelloWorld (extended background – incomplete)\033[0m")

# 49: Reset de fondo
print("\033[49m>>HelloWorld (default background color)\033[0m")

# 50: Fuente alternativa (muy poco usada)
print("\033[50m>>HelloWorld (alternative font)\033[0m")
