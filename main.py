from datetime import date

from AdministradorControladores import AdministradorControladores
from controladores.ControladorDestino import ControladorDestino
from controladores.ControladorGasto import ControladorGasto
from controladores.ControladorMoneda import ControladorMoneda
from controladores.ControladorPersona import ControladorPersona
from controladores.ControladorTipoGasto import ControladorTipoGasto
from controladores.ControladorTipoPago import ControladorTipoPago
from controladores.ControladorViaje import ControladorViaje


def main():
    administrador_controladores = AdministradorControladores()

    controlador_destino = ControladorDestino()
    controlador_gasto = ControladorGasto()
    controlador_moneda = ControladorMoneda()
    controlador_persona = ControladorPersona()
    controlador_tipo_gasto = ControladorTipoGasto()
    controlador_tipo_pago = ControladorTipoPago()
    controlador_viaje = ControladorViaje()

    administrador_controladores.registrar_controlador('ControladorDestino', controlador_destino)
    administrador_controladores.registrar_controlador('ControladorGasto', controlador_gasto)
    administrador_controladores.registrar_controlador('ControladorMoneda', controlador_moneda)
    administrador_controladores.registrar_controlador('ControladorPersona', controlador_persona)
    administrador_controladores.registrar_controlador('ControladorTipoGasto', controlador_tipo_gasto)
    administrador_controladores.registrar_controlador('ControladorTipoPago', controlador_tipo_pago)
    administrador_controladores.registrar_controlador('ControladorViaje', controlador_viaje)

    controlador_destino.crear_destino('Estados Unidos', controlador_moneda.obtener_moneda('Dolar'))

    controlador_tipo_pago.crear_tipo_pago('Tarjeta')
    controlador_tipo_pago.crear_tipo_pago('Efectivo')

    controlador_tipo_gasto.crear_tipo_gasto('Transporte')
    controlador_tipo_gasto.crear_tipo_gasto('Alojamiento')
    controlador_tipo_gasto.crear_tipo_gasto('Alimentacion')
    controlador_tipo_gasto.crear_tipo_gasto('Entretenimiento')
    controlador_tipo_gasto.crear_tipo_gasto('Compras')

    controlador_persona.crear_persona('12345', 'Pepito')
    ids_viaje = []
    ids_viaje.append(controlador_viaje.registrar_viaje('12345', 'Estados Unidos', date(2024, 6, 1), date(2024, 6,
                                                                                                         20),
                                                       200000))

    controlador_gasto.registrar_gasto(ids_viaje[0], date(2024, 6, 9), 25000, '1', '1')
    controlador_gasto.registrar_gasto(ids_viaje[0], date(2024, 6, 9), 50000, '1', '3')
    controlador_gasto.registrar_gasto(ids_viaje[0], date(2024, 6, 10), 2000, '2', '3')
    controlador_gasto.registrar_gasto(ids_viaje[0], date(2024, 6, 13), 5000, '1', '5')
    controlador_gasto.registrar_gasto(ids_viaje[0], date(2024, 6, 15), 30000, '2', '5')
    controlador_gasto.registrar_gasto(ids_viaje[0], date(2024, 6, 16), 100000, '1', '4')
    controlador_gasto.registrar_gasto(ids_viaje[0], date(2024, 6, 19), 200000, '2', '1')
    controlador_gasto.registrar_gasto(ids_viaje[0], date(2024, 6, 19), 45000, '2', '3')

    mostrar_reporte_x_tipo(controlador_gasto)
    print()
    mostrar_reporte_x_dia(controlador_gasto)


def mostrar_reporte_x_dia(controlador_gastos: ControladorGasto):
    print('** Reporte por dia **')
    reporte = controlador_gastos.obtener_reporte_de_gastos_por_dia()
    for fecha_gasto, datos_gasto in reporte.items():
        print(f'Fecha: {fecha_gasto}')
        for dato in datos_gasto:
            print(f'- {dato}')
    print()


def mostrar_reporte_x_tipo(controlador_gastos: ControladorGasto):
    print('** Reporte por tipo **')
    reporte = controlador_gastos.obtener_reporte_de_gastos_por_tipo()
    for fecha_gasto, datos_gasto in reporte.items():
        print(f'Tipo: {fecha_gasto}')
        for dato in datos_gasto:
            print(f'- {dato}')
    print()


if __name__ == '__main__':
    main()
