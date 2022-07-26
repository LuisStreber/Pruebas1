

class bebibas:
    def __init__(self, tipo, nombre, cantidad):
        self.__tipo = tipo
        self.__nombre = nombre
        self.__cantidad = cantidad

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor 

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def cantidad(self):
        return self.__cantidad 

    @cantidad.setter
    def cantidad(self, valor):
        self.__cantidad = valor 

    def __str__(self):
        return 'tipo' + str(self.__tipo) + ', nombre' + str(self.__nombre) + ', cantidad' + str(self.__cantidad)

    p1 = ("Whiskey", "Jack Daniels", 10)
    p2 = ("Vodka", "Smirnoff", 67)
    p3 = ("Cerveza", "Imperial", 285)

    print(p1, p2, p3)
         