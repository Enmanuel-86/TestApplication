from views import SideBarView
from controllers.pantalla_form_controller import PantallaFormController
from controllers.pantalla_de_bienvenida_controller import PantallaDeBienvenidaController
from utils import funciones_sistema


class SideBarController(SideBarView):
    def __init__(self):
        super().__init__()

        self.btn_principal.on_click = lambda e: funciones_sistema.cambiar_a_la_pantalla(e, "PantallaDeBienvenida")
        self.btn_form.on_click = lambda e: funciones_sistema.cambiar_a_la_pantalla(e, "PantallaForm")
        self.btn_salir.on_click = lambda e: funciones_sistema.cambiar_a_la_pantalla(e, "Login", False)



    
    


    
