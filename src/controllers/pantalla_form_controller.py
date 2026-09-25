from views import PantallaFormView
from utils import funciones_sistema
datos_persona = []

class PantallaFormController(PantallaFormView):
    def __init__(self):
        super().__init__()

        self.btn_validar.on_click = lambda e: self.preguntar(e)
        self.btn_dlg_si.on_click = lambda e: self.guardar_informacion(e)

    def preguntar(self, e):
        e.control.page.show_dialog(self.dlg_aviso)
        e.page.update()

    def guardar_informacion(self, e):
        e.control.page.pop_dialog()
        e.page.update()
        datos_persona.append(self.txt_primer_nombre.value)
        print("Se guarda esta guardando la información")
        print(datos_persona)
        funciones_sistema.cambiar_pantalla("PantallaForm", self, e)