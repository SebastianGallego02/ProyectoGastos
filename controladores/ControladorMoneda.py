from AdministradorControladores import AdministradorControladores
from entidades.Dollar import Dollar


class ControladorMoneda:

    def __init__(self):
        self.__monedas = {}
        self.__inicializar_dolar()
        self.__inicializar_euro()
        self.__inicializar_cop()
        self.__administrador_controladores = None

    @property
    def administrador_controladores(self):
        return self.__administrador_controladores

    @administrador_controladores.setter
    def administrador_controladores(self, administrador_controladores: AdministradorControladores):
        self.__administrador_controladores = administrador_controladores

    def __inicializar_dolar(self):
        if self.__monedas.get('Dolar') is not None:
            return
        dolar = Dollar(len(self.__monedas) + 1, 'Dolar')
        self.__monedas['Dolar'] = dolar

    def __inicializar_euro(self):
        if self.__monedas.get('Euro') is not None:
            return
        euro = Dollar(len(self.__monedas) + 1, 'Euro')
        self.__monedas['Euro'] = euro

    def __inicializar_cop(self):
        if self.__monedas.get('COP') is not None:
            return
        cop = Dollar(len(self.__monedas) + 1, 'COP')
        self.__monedas['COP'] = cop

    def obtener_moneda(self, nombre: str):
        return self.__monedas.get(nombre)
