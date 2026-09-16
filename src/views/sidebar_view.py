import flet as ft
import time
class SideBarView(ft.Container):
    def __init__(self):
        super().__init__()  
        
        self.bgcolor= ft.Colors.WHITE_10
        self.width=50
        self.padding = 2
        self.animate = ft.Animation(200, curve= ft.AnimationCurve.LINEAR)
        self.btn_menu = ft.Button(
                                  content= ft.Text("Menu", no_wrap= True), 
                                  on_click= self.animarsidebar,
                                  icon = ft.Icons.MENU,
                                    expand= True,
                                    
                                    )

        self.btn_principal = ft.Button(
                                       content= ft.Text("Principal", no_wrap= True),
                                       icon = ft.Icons.HOME,
                                       expand= True
                                       )


        self.btn_form = ft.Button(
                            content= ft.Text("Formulario", no_wrap= True),
                            icon= ft.Icons.FOUR_MP,
                            expand= True
                            )

        self.btn_salir = ft.Button(
                                   content= ft.Text("Salir", no_wrap= True),
                                   icon= ft.Icons.ARROW_BACK,
                                    expand= True,
                                    
                                    
                                   )
        
        self.content= ft.Column(controls = [
                                        ft.Row(self.btn_menu),
                                        ft.Row(self.btn_principal),
                                        ft.Row(self.btn_form),
                                        ft.Row([self.btn_salir])
                                        
                                        
                                    ]
                            )


    def animarsidebar(self):
        if self.width == 200:
            self.width = 50

        elif self.width == 50:
            self.width = 200
            
