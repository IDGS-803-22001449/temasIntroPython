from io import open

# 
texto=""

# abre el archivo en modo lectura "r"
archivo=open("archivo.txt", "r")
#.read() lee todo el archivo y crea un String con el contenido
texto=archivo.read()
print(texto)
#se coloca el puntero al inicio del archivo
archivo.seek(0)
texto=archivo.read()
print(texto)

#Devielve una lista de strings, y cada linea es un elemento de la lista
archivo.readline()

#cierra el flujo del archivo
archivo.close()