from AdministradorControladores import AdministradorControladores
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

    def obtener_tipo_gasto(self, id: str) -> TipoGasto:
        for tipo_gasto in self.__tipos_gasto:
            if id == tipo_gasto.id:
                return tipo_gasto

    def crear_tipo_gasto(self, nombre):
        tipo_nuevo = TipoGasto(str(len(self.__tipos_gasto) + 1), nombre)
        self.__tipos_gasto.append(tipo_nuevo)