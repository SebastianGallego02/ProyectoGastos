from AdministradorControladores import AdministradorControladores
from entidades.Destino import Destino


class ControladorDestino:

    def __init__(self):
        self.__destinos: list[Destino] = []
        self.__administrador_controladores = None

    @property
    def administrador_controladores(self):
        return self.__administrador_controladores

    @administrador_controladores.setter
    def administrador_controladores(self, administrador_controladores: AdministradorControladores):
        self.__administrador_controladores = administrador_controladores

    def obtener_destino(self, nombre):
        for destino in self.__destinos:
            if destino.nombre == nombre:
                return destino

    def crear_destino(self, nombre, moneda):
        destino = Destino(len(self.__destinos)+1, nombre, moneda)
        self.__destinos.append(destino)