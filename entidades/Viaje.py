from datetime import date

from entidades.Destino import Destino
from entidades.Persona import Persona


class Viaje:

    def __init__(self, id: str, fecha_inicio: int, fecha_fin: date, presupuesto_x_dia: float, destino: Destino,
                 persona: Persona):
        self.__id = id
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__presupuesto_x_dia = presupuesto_x_dia
        self.destino = destino
        self.persona = persona

    @property
    def id(self):
        return self.__id

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @property
    def fecha_fin(self):
        return self.__fecha_fin
