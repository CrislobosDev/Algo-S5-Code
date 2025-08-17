class Producto: # Clase Producto que representa un producto con un codigo y stock
    def __init__(self, codigo, stock): # Constructor de la clase Producto
        self.codigo = codigo # Atributo codigo del producto
        self.stock = stock # Atributo stock del producto

    def __str__(self): # Metodo para representar el objeto Producto como una cadena
        return f"{self.codigo} - {self.stock}" # Retorna una cadena con el codigo y stock del producto


class CatalogoProductos: # Clase CatalogoProductos que maneja un catalogo de productos
    def __init__(self): # Constructor de la clase CatalogoProductos
        self.__productos = {} # Atributo privado que almacena los productos en un diccionario

    def agregar(self, codigo, stock): # Metodo para agregar un producto al catalogo
        if codigo in self.__productos: # Verifica si el codigo del producto ya existe
            print(f"El producto con codigo '{codigo}' ya existe.") 
        else:
            self.__productos[codigo] = stock # Agrega el producto al catalogo con su codigo y stock
            print("\n")
            print(f"Producto '{codigo}' agregado con stock de {stock}.")

    def eliminar_producto(self, codigo): # Metodo para eliminar un producto del catalogo
        if codigo in self.__productos: # Verifica si el codigo del producto existe en el catalogo
            self.__productos.pop(codigo)  # Elimina el producto del catalogo
            print(f"Producto '{codigo}' eliminado del catalogo.")
        else:
            print(f"No existe el producto con codigo '{codigo}' .")

    def actualizar_stock(self, codigo, nuevo_stock): # Metodo para actualizar el stock de un producto
        if codigo in self.__productos: # Verifica si el codigo del producto existe en el catalogo
            self.__productos[codigo] = nuevo_stock # Actualiza el stock del producto
            print("\n")
            print(f"Stock del producto'{codigo}' actualizado a '{nuevo_stock}")
        else:
            print(f"El producto '{codigo}' no se encontro")

    def verificar_producto(self, codigo): # Metodo para verificar si un producto existe en el catalogo
        if codigo in self.__productos: # Verifica si el codigo del producto existe en el catalogo
            print("\n")
            print(f"El producto '{codigo}' si existe")
        else:
            print("\n")
            print(f"El producto '{codigo}' no existe")

    def mostrar_productos(self): # Metodo para mostrar todos los productos en el catalogo
        if not self.__productos: # Verifica si el catalogo esta vacio
            print("El catalogo esta vacio")
        else:
            print("\n")
            print("** Catalogo de Productos: ** ")
            for codigo, stock in self.__productos.items(): # Itera sobre los productos en el catalogo
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

if __name__ == "__main__": # Punto de entrada de la aplicacion
    catalogo = CatalogoProductos() # Crea una instancia de CatalogoProductos
    estado = True # Variable para controlar el estado del menu
    while estado: # Bucle para mostrar el menu y procesar las opciones
        menu() # Muestra el menu de opciones
        try: 
            opcion = int(input("Ingrese una opcion: ")) # Solicita al usuario que ingrese una opcion del menu
            if opcion == 1: # Opcion para agregar un producto
                try: 
                    codigo = input("Ingrese el codigo del producto: ") # Solicita el codigo del producto
                    stock = int(input("Ingrese una cantidad de stock: ")) # Solicita el stock del producto
                    producto = Producto(codigo, stock)  # Crea una instancia de Producto
                    catalogo.agregar(codigo, stock) # Agrega el producto al catalogo
                except ValueError: # Captura el error si el stock no es un numero entero
                    print("ERROR")

            elif opcion == 2:
                codigo = input("Que producto desea eliminar, Ingrese el codigo: ")
                catalogo.eliminar_producto(codigo) # Elimina un producto del catalogo

            elif opcion == 3:
                codigo = input("Que producto desea modificar: ")
                try:
                    nuevo_stock = int(input("Cual es el nuevo stock: "))
                    catalogo.actualizar_stock(codigo, nuevo_stock) # Actualiza el stock de un producto
                except ValueError:
                    print("El stock debe ser un numero entero")

            elif opcion == 4:
                codigo = input("Ingrese el codigo del producto a verificar: ")
                catalogo.verificar_producto(codigo) # Verifica si un producto existe en el catalogo

            elif opcion == 5:
                catalogo.mostrar_productos()  # Muestra todos los productos en el catalogo

            elif opcion == 6:
                print("Saliendo de la aplicacion...")
                estado = False # Cambia el estado a False para salir del bucle

            else:
                print("Opcion no valida, ingrese una opcion del 1 al 6")

        except ValueError: # Captura el error si la opcion ingresada no es un numero entero
            print("Ingresa una opcion valida")
