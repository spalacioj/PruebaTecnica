class Item:
    def __init__(self, nombre, unidades, prestados):
        self.nombre = nombre
        self.unidades = unidades
        self.prestados = prestados
        
class Libro(Item):
    def disponibles(self):
        disponibles = self.unidades - self.prestados
        print(f"El libro {self.nombre} tiene {disponibles} disponibles")
    
    def prestarItem(self):
        if self.prestados == self.unidades:
            print(f"No quedan unidades del libro {self.nombre}")
        else:
            self.prestados += 1
            print("Libro prestado")
    
    def devolverItem(self):
        if self.prestados == 0:
            print(f"No se han prestado unidades del libro {self.nombre}")
            return
        self.prestados -= 1
        print("Libro retornado con exito")
    
class Revista(Item):
    def disponibles(self):
        disponibles = self.unidades - self.prestados
        return f"El libro {self.nombre} tiene {disponibles} disponibles"
    
    def prestarItem(self):
        if self.prestados == self.unidades:
            print(f"No quedan unidades de la revista {self.nombre}")
        else:
            self.prestados += 1
            print("Revista prestada")

    def devolverItem(self):
        if self.prestados == 0:
            print(f"No se han prestado unidades de la revista {self.nombre}")
            return
        self.prestados -= 1
        print("Revista retornada con exito")

class Biblioteca:
    def __init__(self):
        self.items = []

    def agregarItem(self, item):
        self.items.append(item)

    def listarItems(self):
        if(len(self.items) == 0):
            print("La biblioteca no tiene items, agrega uno nuevo")
            return
        print("Nombre Unidades Prestados")
        for i in range(0, len(self.items)):
            print(f"{self.items[i].nombre} {self.items[i].unidades} {self.items[i].prestados}") 
    
    def prestarItems(self, nombre):
        for i in range(len(self.items)):
            if self.items[i].nombre == nombre:
               return self.items[i].prestarItem()
        print("Ese item no esta en la biblioteca")

    def devolverItems(self, nombre):
        for i in range(len(self.items)):
            if self.items[i].nombre == nombre:
               return self.items[i].devolverItem()
        print("Ese item no esta en la biblioteca")

    def itemMasPrestado(self):
        name = ""
        value = 0
        for i in range(len(self.items)):
            if self.items[i].prestados > value:
                name = self.items[i].nombre
                value = self.items[i].prestados
        print(f"El item mas prestado es {name}")

    
def main():
    miniBiblioteca = Biblioteca()
    opciones = ["Salir", "Agregar Items", "Listar Items", "Prestar item", "Devolver item"]

    for i, value in enumerate(opciones):
        print(i, value)
    while True:
        opcion = int(input("Ingrese la opcion a usar: "))
        if opcion == 0:
            break
        elif opcion == 1:
            tipo = int(input("Eliga entre 1.libro o 2.revista (escriba el numero): "))
            if tipo != 1 and tipo != 2:
                print("opcion no valida")
                break
            nombre = input("Escriba el nombre del item: ")
            unidades = input("Cuantas unidades va a tener disponible: ")
            if tipo == 1:
                nuevoLibro = Libro(nombre, unidades, 0)
                miniBiblioteca.agregarItem(nuevoLibro)
            else:
                nuevaRevista = Revista(nombre, unidades, 0)
                miniBiblioteca.agregarItem(nuevaRevista)
        elif opcion == 2:
            miniBiblioteca.listarItems()
        elif opcion == 3:
            nombre = input("Nombre del item a prestar: ")
            miniBiblioteca.prestarItems(nombre)
        elif opcion == 4:
            nombre = input("Nombre del item a devolver: ")
            miniBiblioteca.devolverItems(nombre)
        else:
            print("Opcion invalida")


main()
