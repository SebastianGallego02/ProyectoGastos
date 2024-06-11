class TipoPago:

    def __init__(self, id: str, nombre: str):
        self.__id = id
        self.__nombre = nombre

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre
