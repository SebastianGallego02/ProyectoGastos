from AdministradorControladores import AdministradorControladores
from entidades.Persona import Persona


class ControladorPersona:

    def __init__(self):
        self.__personas: list[Persona] = []
        self.__administrador_controladores = None

    @property
    def administrador_controladores(self):
        return self.__administrador_controladores

    @administrador_controladores.setter
    def administrador_controladores(self, administrador_controladores: AdministradorControladores):
        self.__administrador_controladores = administrador_controladores

    def obtener_persona(self, identificacion: str):
        for persona in self.__personas:
            if persona.identificacion == identificacion:
                return persona

