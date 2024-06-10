from entidades.Moneda import Moneda


class Destino:

    def __init__(self, id: str, nombre: str, moneda: Moneda):
        self.__id = id
        self.__nombre = nombre
        self.__moneda = moneda

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    def obtener_valor_en_cop(self, valor: float) -> float:
        return valor * self.__moneda.obtener_valor_moneda()
