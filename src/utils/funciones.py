import flet as ft
from controllers.login_controller import LoginController
from controllers.pantalla_de_bienvenida_controller import PantallaDeBienvenidaController
from controllers.pantalla_form_controller import PantallaFormController


"""
login = LoginController()
pantalla_de_bienvenida =PantallaDeBienvenidaController()
pantalla_form = PantallaFormController()

PANTALLAS:dict = {
                  "Login": login,
                  "PantallaDeBienvenida": pantalla_de_bienvenida,
                  "PantallaForm": pantalla_form
                }
"""


class FuncionesSistema:
  def __init__(self):
    
    self.SIDEBAR = None
    self.ESPACIO_PRINCIPAL = None

    self.PANTALLAS:dict = {
                    "Login": LoginController,
                    "PantallaDeBienvenida": PantallaDeBienvenidaController,
                    "PantallaForm": PantallaFormController
                  }

  

  def cambiar_pantalla(self, nombre_pantalla:str, contenedor_principal, e):
      """
          Funcion para cambiar entre pantallas.

          Pantalla disponibles:
          - Login
          - PantallaDeBienvenida
          - PantallaForm
      """

      contenedor_principal.content = self.PANTALLAS[nombre_pantalla]()
      e.page.update()

      print(f"Estamos en el/la: {nombre_pantalla}")


funciones_sistema = FuncionesSistema()
