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

    self.CTN_ESPACIO_PRINCIPAL = None
    self.SIDEBAR = None

    self.PANTALLAS_CONTROLLERS:dict = {
                    "Login": LoginController(),
                    "PantallaDeBienvenida": PantallaDeBienvenidaController(),
                    "PantallaForm": PantallaFormController()
                  }


  

  def cambiar_a_la_pantalla(self, e, nombre_pantalla:str, visibilidad_sidebar:bool = True):
      """
          Funcion para cambiar entre pantallas.

          Solo se tiene que para el nombre de la pantalla para poder acceder a ella

          Pantallas disponibles:
          - Login
          - PantallaDeBienvenida
          - PantallaForm
      """

      self.CTN_ESPACIO_PRINCIPAL.content = self.PANTALLAS_CONTROLLERS[nombre_pantalla]
      self.SIDEBAR.visible = visibilidad_sidebar
      e.page.update()

      print(f"Estamos en el/la: {nombre_pantalla}")


funciones_sistema = FuncionesSistema()
