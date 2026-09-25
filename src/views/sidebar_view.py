import flet as ft
import time
from components import ButtonSideBar
class SideBarView(ft.Container):
    def __init__(self):
        super().__init__()  
        
        self.bgcolor= ft.Colors.WHITE_10
        self.width=47
        self.padding = 2
        self.animate = ft.Animation(200, curve= ft.AnimationCurve.LINEAR)
        self.btn_menu = ButtonSideBar(
                                  titulo= "Menu",
                                  icono = ft.Icons.MENU, 
                                  on_click= self.animarsidebar,
                                  )

        self.btn_principal = ButtonSideBar(titulo= "Principal", icono= ft.Icons.HOME)


        self.btn_form = ButtonSideBar(titulo = "Formulario", icono= ft.Icons.NOTE_ADD)

        self.btn_salir = ButtonSideBar(titulo= "Salir", icono= ft.Icons.ARROW_BACK )
        
        self.content= ft.Column(controls = [
                                        ft.Row(self.btn_menu),
                                        ft.Row(self.btn_principal),
                                        ft.Row(self.btn_form),
                                        ft.Row([self.btn_salir])],
                                spacing= 2
                            )


    def animarsidebar(self):
        if self.width == 200:
            self.width = 47

        elif self.width == 47:
            self.width = 200
            
