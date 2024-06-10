from AdministadorControladores import AdministradorControladores
from entidades.Gasto import Gasto


class ControladorGasto:
    def __init__(self):
        self.__gastos: list[Gasto] = []
        self.__administrador_controladores = None

    @property
    def administrador_controladores(self):
        return self.__administrador_controladores

    @administrador_controladores.setter
    def administrador_controladores(self, administrador_controladores: AdministradorControladores):
        self.__administrador_controladores = administrador_controladores

    def registrar_gasto(self, id_viaje: str, valor_gastado: float, id_tipo_pago: str, id_tipo_gasto: str):
        pass
