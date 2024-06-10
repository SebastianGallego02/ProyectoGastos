from datetime import date

from entidades.TipoGasto import TipoGasto
from entidades.TipoPago import TipoPago


class Gasto:

    def __init__(self, fecha_gasto: date, valor_gastado: float, tipo_pago: TipoPago, tipo_gasto: TipoGasto):
        self.__fecha_gasto = fecha_gasto
        self.__valor_gastado = valor_gastado
        self.__tipo_pago = tipo_pago
        self.__tipo_gasto = tipo_gasto

    @property
    def fecha_gasto(self):
        return self.__fecha_gasto

    @property
    def tipo_gasto(self):
        return self.__tipo_gasto

    def __str__(self):
        return f'Fecha: {self.__fecha_gasto}. Valor gastado: {self.__valor_gastado}. Tipo de pago:' \
               f' {self.__tipo_pago.nombre}. Tipo ' \
               f'de ' \
               f'gasto: ' \
               f'{self.__tipo_gasto.nombre}'
