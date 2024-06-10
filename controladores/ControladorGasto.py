from datetime import date

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

    def registrar_gasto(self, id_viaje: str, fecha_gasto: date, valor_gastado: float, id_tipo_pago: str,
                        id_tipo_gasto: str):
        controlador_viaje = self.__administrador_controladores.get_controlador('ControladorViaje')
        viaje = controlador_viaje.obtener_viaje(id_viaje)
        if not viaje.validar_fecha_gasto(fecha_gasto):
            return
        valor_en_cop = viaje.destino.obtener_valor_en_cop()
        controlador_tipo_pago = self.__administrador_controladores.get_controlador('ControladorTipoPago')
        tipo_pago = controlador_tipo_pago.obtener_tipo_pago(id_tipo_pago)
        controlador_tipo_gasto = self.__administrador_controladores.get_controlador('ControladorTipoGasto')
        tipo_gasto = controlador_tipo_gasto.obtener_tipo_gasto(id_tipo_gasto)
        gasto_nuevo = Gasto(fecha_gasto, valor_en_cop, tipo_pago, tipo_gasto)
        self.__gastos.append(gasto_nuevo)
