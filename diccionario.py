from io import open

class Palabra:
    def __init__(self, palabraEs, palabraEn):
        self.palabraEs = palabraEs
        self.palabraEn = palabraEn

    def __str__(self):
        return f"{self.palabraEs} - {self.palabraEn}"

class Diccionario:
    def __init__(self):
        self.listaPalabras = []
        
    def agregar(self, palabra):
        self.listaPalabras.append(palabra)
        self.guardar_en_archivo()
        
    def mostrar(self):
        for palabra in self.listaPalabras:
            print(palabra)

    def guardar_en_archivo(self):
        with open("diccionario.txt", "w", encoding="utf-8") as archivo:
            for palabra in self.listaPalabras:
                archivo.write(f"{palabra.palabraEs} - {palabra.palabraEn}\n")
            
    def buscar(self, palabraEs):
        for palabra in self.listaPalabras:
            if palabra.palabraEs == palabraEs:
                return palabra
    
    def buscarIngles(self, palabraEn):
        for palabra in self.listaPalabras:
            if palabra.palabraEn == palabraEn:
                return palabra

class Menu:
    def __init__(self):
        self.diccionario = Diccionario()
        
    def opcionesMenu(self):
        while True:
            print("1.- Capturar palabra")
            print("2.- Buscar palabra")

            opcion = int(input("Selecciona una opcion: "))

            if opcion == 1:
                palabraEs = input("Palabra en español: ")
                palabraEn = input("Palabra en ingles: ")
                palabra = Palabra(palabraEs, palabraEn)
                self.diccionario.agregar(palabra)
                print("Palabra agregada exitosamente.")
            elif opcion == 2:
                opcionLenguaje = input("¿En que idioma buscas la palabra? (1=español, 2=ingles): ")
                if opcionLenguaje == "1":
                    palabraEs = input("Palabra a buscar en español: ")
                    resultado = self.diccionario.buscar(palabraEs)
                    if resultado:
                        print(f"Traducción: {resultado.palabraEn}")
                    else:
                        print("Palabra no encontrada.")
                elif opcionLenguaje == "2":
                    palabraEn = input("Palabra a buscar en ingles: ")
                    resultado = self.diccionario.buscarIngles(palabraEn)
                    if resultado:
                        print(f"Traducción: {resultado.palabraEs}")
                    else:
                        print("Palabra no encontrada.")
                else:
                    print("Opcion no valida.")
            elif opcion == 3:
                self.diccionario.mostrar()
            elif opcion == 4:
                print("salio")
                break
            else:
                print("Opción no valida.")

def main():
    menu = Menu()
    menu.opcionesMenu()
    
if __name__ == "__main__":
    main()
