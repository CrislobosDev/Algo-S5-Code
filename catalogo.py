class Producto:
    def __init__(self, codigo, stock):
        self.codigo = codigo
        self.stock = stock

    def __str__(self):
        return f"{self.codigo} - {self.stock}"


class CatalogoProductos:
    def __init__(self):
        self.__productos = {}

    def agregar(self, codigo, stock):
        if codigo in self.__productos:
            print(f"El producto con codigo '{codigo}' ya existe.")
        else:
            self.__productos[codigo] = stock
            print("\n")
            print(f"Producto '{codigo}' agregado con stock de {stock}.")

    def eliminar_producto(self, codigo):
        if codigo in self.__productos:
            self.__productos.pop(codigo)
            print(f"Producto '{codigo}' eliminado del catalogo.")
        else:
            print(f"No existe el producto con codigo '{codigo}' .")

    def actualizar_stock(self, codigo, nuevo_stock):
        if codigo in self.__productos:
            self.__productos[codigo] = nuevo_stock
            print("\n")
            print(f"Stock del producto'{codigo}' actualizado a '{nuevo_stock}")
        else:
            print(f"El producto '{codigo}' no se encontro")

    def verificar_producto(self, codigo):
        if codigo in self.__productos:
            print("\n")
            print(f"El producto '{codigo}' si existe")
        else:
            print("\n")
            print(f"El producto '{codigo}' no existe")

    def mostrar_productos(self):
        if not self.__productos:
            print("El catalogo esta vacio")
        else:
            print("\n")
            print("** Catalogo de Productos: ** ")
            for codigo, stock in self.__productos.items():
                print(f" Codigo: {codigo} | Stock: {stock}")


def menu():  # Funcion para mostrar el menu de opciones
    print("\n")
    print("**************************")
    print("** MENU DE OPCIONES  **")
    print("     1. Agregar producto")
    print("     2. Eliminar producto")
    print("     3. Actualizar producto")
    print("     4. Verificar producto")
    print("     5. Ver productos")
    print("     6. Salir de la aplicacion")


# Aplicacion

if __name__ == "__main__":
    catalogo = CatalogoProductos()
    estado = True
    while estado:
        menu()
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                try:
                    codigo = input("Ingrese el codigo del producto: ")
                    stock = int(input("Ingrese una cantidad de stock: "))
                    producto = Producto(codigo, stock)
                    catalogo.agregar(codigo, stock)
                except ValueError:
                    print("ERROR")

            elif opcion == 2:
                codigo = input("Que producto desea eliminar, Ingrese el codigo: ")
                catalogo.eliminar_producto(codigo)

            elif opcion == 3:
                codigo = input("Que producto desea modificar: ")
                try:
                    nuevo_stock = int(input("Cual es el nuevo stock: "))
                    catalogo.actualizar_stock(codigo, nuevo_stock)
                except ValueError:
                    print("El stock debe ser un numero entero")

            elif opcion == 4:
                codigo = input("Ingrese el codigo del producto a verificar: ")
                catalogo.verificar_producto(codigo)

            elif opcion == 5:
                catalogo.mostrar_productos()

            elif opcion == 6:
                print("Saliendo de la aplicacion...")
                estado = False

            else:
                print("Opcion no valida, ingrese una opcion del 1 al 6")

        except ValueError:
            print("Ingresa una opcion valida")
