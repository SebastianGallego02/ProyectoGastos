from datetime import date

from AdministadorControladores import AdministradorControladores
from entidades.Viaje import Viaje


class ControladorViaje:

    def __init__(self):
        self.__viajes: list[Viaje] = []
        self.__administrador_controladores = None

    @property
    def administrador_controladores(self):
        return self.__administrador_controladores

    @administrador_controladores.setter
    def administrador_controladores(self, administrador_controladores: AdministradorControladores):
        self.__administrador_controladores = administrador_controladores

    def registrar_viaje(self,  identificacion: str, nombre_destino: str,  fecha_inicio: date, fecha_fin: date, presupuesto_x_dia):
        """
        Método que manejará la mayoría de la lógica del registro de un viaje
        :return: booleano indicando si se registró correctamente el viaje
        """
        controlador_viaje = self.__administrador_controladores.get_controlador('ControladorViaje')
        persona = controlador_viaje.obtener_persona()
        destino = controlador_viaje.obtener_destino()

        if self.validar_fecha(fecha_inicio, fecha_fin):
            id = str(len(self.__viajes) + 1)
            nuevo_viaje = Viaje(id, fecha_inicio, fecha_fin, presupuesto_x_dia, destino, persona)
            self.__viajes.append(nuevo_viaje)

    def validar_fecha(self, fecha_inicio: date, fecha_fin: date) -> bool:
        for viaje in self.__viajes:
            if viaje.fecha_inicio == fecha_inicio and viaje.fecha_fin == fecha_fin:
                return False
        return True


    def obtener_viaje(self, id_viaje) -> Viaje:
        for viaje in self.__viajes:
            if id_viaje == viaje.id:
                return viaje


def validar_viaje(self):

    pass
