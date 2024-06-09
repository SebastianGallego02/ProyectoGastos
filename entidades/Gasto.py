from datetime import date


class Gasto:

    def __init__(self, fecha_gasto: date, valor_gastado: float):
        self.__fecha_gasto = fecha_gasto
        self.__valor_gastado = valor_gastado
