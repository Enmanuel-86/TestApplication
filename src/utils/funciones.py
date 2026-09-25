import importlib
import flet as ft


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

  def cambiar_pantalla(self, nombre_pantalla:str, contenedor_principal, e):
      """
          Funcion para cambiar entre pantallas.

          Pantalla disponibles:
          - Login
          - PantallaDeBienvenida
          - PantallaForm
      """

      contenedor_principal.content = self.obtener_controller_pantalla(nombre_pantalla)()
      e.page.update()

      print(f"Estamos en el/la: {nombre_pantalla}")
    
  def obtener_controller_pantalla(self, nombre_pantalla: str) -> object:
    """
      Función para obtener a partir de un string
      la clase del controller sin generar una importación circular
      
      Separando la ruta del módulo.py de la clase que se quiera obtener
    """
    
    RUTA_CONTROLLERS = {
      "Login": "controllers.login_controller.LoginController",
      "PantallaDeBienvenida": "controllers.pantalla_de_bienvenida_controller.PantallaDeBienvenidaController",
      "PantallaForm": "controllers.pantalla_form_controller.PantallaFormController"
    }
    
    ruta_elegida = RUTA_CONTROLLERS[nombre_pantalla]
    
    # Separamos el módulo de la clase
    ruta_modulo, nombre_controller = ruta_elegida.rsplit(".", 1)
    
    # Importamos dinámicamente el controller
    modulo = importlib.import_module(ruta_modulo)
    nombre_clase = getattr(modulo, nombre_controller)
    
    return nombre_clase


funciones_sistema = FuncionesSistema()