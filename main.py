from AdministradorControladores import AdministradorControladores
from controladores.ControladorDestino import ControladorDestino
from controladores.ControladorGasto import ControladorGasto
from controladores.ControladorPersona import ControladorPersona
from controladores.ControladorTipoGasto import ControladorTipoGasto
from controladores.ControladorTipoPago import ControladorTipoPago
from controladores.ControladorViaje import ControladorViaje


def main():
    administrador_controladores = AdministradorControladores()

    controlador_destino = ControladorDestino()
    controlador_gasto = ControladorGasto()
    controlador_persona = ControladorPersona()
    controlador_tipo_gasto = ControladorTipoGasto()
    controlador_tipo_pago = ControladorTipoPago()
    controlador_viaje = ControladorViaje()

    administrador_controladores.registrar_controlador('ControladorDestino', controlador_destino)
    administrador_controladores.registrar_controlador('ControladorGasto', controlador_gasto)
    administrador_controladores.registrar_controlador('ControladorPersona', controlador_persona)
    administrador_controladores.registrar_controlador('ControladorTipoGasto', controlador_tipo_gasto)
    administrador_controladores.registrar_controlador('ControladorTipoPago', controlador_tipo_pago)
    administrador_controladores.registrar_controlador('ControladorViaje', controlador_viaje)


def mostrar_reporte_x_dia(controlador_gastos: ControladorGasto):
    reporte = controlador_gastos.obtener_reporte_de_gastos_por_dia()
    for fecha_gasto, datos_gasto in reporte.items():
        print(f'Fecha: {fecha_gasto}')
        for dato in datos_gasto:
            print(f'- {dato}')


def mostrar_reporte_x_tipo(controlador_gastos: ControladorGasto):
    reporte = controlador_gastos.obtener_reporte_de_gastos_por_tipo()
    for fecha_gasto, datos_gasto in reporte.items():
        print(f'Tipo: {fecha_gasto}')
        for dato in datos_gasto:
            print(f'- {dato}')


if __name__ == '__main__':
    main()
