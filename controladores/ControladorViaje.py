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

    def registrar_viaje(self):
        pass

    def validar_viaje(self):
        pass

    def validar_fecha(self):
        pass

    def obtener_viaje(self, id_viaje) -> Viaje:
        for viaje in self.__viajes:
            if id_viaje == viaje.id:
                return viaje
