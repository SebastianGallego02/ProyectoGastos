from datetime import date

from entidades.TipoGasto import TipoGasto
from entidades.TipoPago import TipoPago


class Gasto:

    def __init__(self, fecha_gasto: date, valor_gastado: float, tipo_pago: TipoPago, tipo_gasto: TipoGasto):
        self.__fecha_gasto = fecha_gasto
        self.__valor_gastado = valor_gastado
        self.__tipo_pago = tipo_pago
        self.__tipo_gasto = tipo_gasto
