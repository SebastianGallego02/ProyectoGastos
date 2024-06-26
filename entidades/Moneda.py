from abc import ABC, abstractmethod


class Moneda(ABC):

    def __init__(self, id: int, nombre: str):
        self.__id = id
        self.__nombre = nombre

    @abstractmethod
    def obtener_valor_moneda(self) -> float:
        pass
