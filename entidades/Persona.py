class Persona:

    def __init__(self, identificacion: str, nombre: str):
        self.__identificacion = identificacion
        self.__nombre = nombre

    @property
    def identificacion(self):
        return self.__identificacion
