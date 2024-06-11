from AdministradorControladores import AdministradorControladores
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

    def obtener_tipo_pago(self, id: str) -> TipoPago:
        for tipo_pago in self.__tipos_pago:
            if id == tipo_pago.id:
                return tipo_pago

    def crear_tipo_pago(self, nombre):
        tipo_nuevo = TipoPago(len(self.__tipos_pago) + 1, nombre)
        self.__tipos_pago.append(tipo_nuevo)