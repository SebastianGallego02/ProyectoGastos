from AdministadorControladores import AdministradorControladores
from entidades.TipoPago import TipoPago


class ControladorTipoPago:

    def __init__(self):
        self.__tipos_pago: list[TipoPago] = []
        self.__administrador_controladores = None

    @property
    def administrador_controladores(self):
        return self.__administrador_controladores

    @administrador_controladores.setter
    def administrador_controladores(self, administrador_controladores: AdministradorControladores):
        self.__administrador_controladores = administrador_controladores

    def validar_tipo_pago(self, id: str):
        pass
