from AdministadorControladores import AdministradorControladores
from entidades.TipoGasto import TipoGasto


class ControladorTipoGasto:

    def __init__(self):
        self.__tipos_gasto: list[TipoGasto] = []
        self.__administrador_controladores = None

    @property
    def administrador_controladores(self):
        return self.__administrador_controladores

    @administrador_controladores.setter
    def administrador_controladores(self, administrador_controladores: AdministradorControladores):
        self.__administrador_controladores = administrador_controladores

    def validar_tipo_gasto(self, id: str):
        pass
