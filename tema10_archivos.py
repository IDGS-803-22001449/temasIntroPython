from io import open

# COLCA EL TEXTO QUE ESCRIBE EN EL ARCHIVO
texto="una line"

#crea un archivo con el nombre, y el "w" indica que se va a escribir en el archivo (en este caso no se coloca una ruta, lo que hace que lo cree en la misma carpeta del proyeco)
archivo=open("archivo.txt", "w")
#escribe en el archivo
archivo.write(texto)
texto="\nsegunda linea"
archivo.write(texto)
texto="\ntercera linea"
#cierra el flujo del archivo
archivo.close()