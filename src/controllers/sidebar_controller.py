from views import SideBarView
from controllers.pantalla_form_controller import PantallaFormController
from controllers.pantalla_de_bienvenida_controller import PantallaDeBienvenidaController
from utils import funciones_sistema


class SideBarController(SideBarView):
    def __init__(self, contenedor_principal):
        super().__init__()
        self.contenedor_principal = contenedor_principal

        self.btn_principal.on_click = lambda e: funciones_sistema.cambiar_pantalla("PantallaDeBienvenida", self.contenedor_principal, e)
        self.btn_form.on_click = lambda e: funciones_sistema.cambiar_pantalla("PantallaForm", self.contenedor_principal, e)
        self.btn_salir.on_click = lambda e: self.volver_al_login(e)

    def volver_al_login(self, e):
        funciones_sistema.cambiar_pantalla("Login", self.contenedor_principal, e)
        self.visible = False
        e.page.update()

    
    


    
