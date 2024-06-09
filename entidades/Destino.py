class Destino:

    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

    @property
    def id(self):
        return self.__id
