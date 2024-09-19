import os
import re

# Ruta del directorio que contiene los archivos PDF.
directorio = '.'

# Expresión regular para encontrar números en los nombres de archivo
patron_numero = re.compile(r'\b(\d+)\b')

# Inicializa un contador para los nombres de archivo
contador = 1

# Recorre todos los archivos en el directorio especificado
for nombre_archivo in os.listdir(directorio):
    # Verifica si el archivo es un PDF
    if nombre_archivo.endswith('.pdf'):
        # Crea un nuevo nombre del archivo de forma iterativa
        nuevo_nombre = f'nuevo_nombre{contador}.pdf'
        
        # Renombra el archivo solo si no existe un archivo con el nuevo nombre
        nuevo_path = os.path.join(directorio, nuevo_nombre)
        if not os.path.exists(nuevo_path):
            os.rename(os.path.join(directorio, nombre_archivo), nuevo_path)
            print(f'Archivo renombrado: {nombre_archivo} -> {nuevo_nombre}')
        else:
            print(f'El archivo {nuevo_nombre} ya existe. Saltando...')
        
        # Incrementa el contador
        contador += 1
