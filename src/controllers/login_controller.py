import flet as ft
from views import LoginView

# Estos usuarios son de a momento ya que no hay base de datos
USUARIOS:dict = {"Enmanuel": "1234", "Juan": "hola123"}

class LoginController(LoginView):
    def __init__(self, sidebar):
        super().__init__()
        self.sidebar = sidebar

        self.btn_ingresar.on_click = self.validacion_de_credenciales

    def validacion_de_credenciales(self, e):
        nombre_usuario = self.txt_nombre_usuario.value.strip()
        contrasenia = self.txt_contrasenia_usuario.value.strip()

        if nombre_usuario == "" and contrasenia == "":
            e.control.page.show_dialog(self.dlg_alerta_campos_vacios)
            print("Debe ingresar nombre de usuario y contrasena")
            return

        if nombre_usuario != "" and nombre_usuario in USUARIOS:
            if USUARIOS[nombre_usuario] == contrasenia:
                e.control.page.show_dialog(ft.SnackBar(content="Inicio de sesion exitoso"))
                self.txt_nombre_usuario.value = ""
                self.txt_contrasenia_usuario.value = ""
                self.sidebar.visible = True
                e.page.update()
                print("Inicio de sesion")
            else:
                e.control.page.show_dialog(self.dlg_contrasenia_incorrecta)
                print("Contraseña Incorrecta")
        else:
            e.control.page.show_dialog(self.dlg_usuario_no_existe)
            print("Usuario no esta registrado")

        
        

       
            
        



