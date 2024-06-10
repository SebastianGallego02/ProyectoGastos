class TipoGasto:

    def __init__(self, id: int, nombre: str):
        self.__id = id
        self.__nombre = nombre

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre
