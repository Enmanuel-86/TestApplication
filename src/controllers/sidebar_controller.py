from views import SideBarView
from controllers.pantalla_form_controller import PantallaFormController
from controllers.pantalla_de_bienvenida_controller import PantallaDeBienvenidaController


class SideBarController(SideBarView):
    def __init__(self, contenedor_principal):
        super().__init__()
        self.contenedor_principal = contenedor_principal

        self.btn_principal.on_click = lambda: self.cambiar(PantallaDeBienvenidaController())
        self.btn_salir.on_click = lambda: self.cambiar(PantallaFormController())

    def cambiar(self, contenido):
        self.contenedor_principal.content = contenido



    


    
