class AdministradorControladores:
    def __init__(self):
        self.controladores = {}

    def registrar_controlador(self, name, controlador):
        self.controladores[name] = controlador
        controlador.administrador_controladores = self

    def get_controlador(self, nombre):
        return self.controladores.get(nombre)
