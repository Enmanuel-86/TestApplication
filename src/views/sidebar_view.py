import flet as ft

class SideBarView(ft.Container):
    def __init__(self):
        super().__init__()  
        
        self.bgcolor= ft.Colors.RED
        self.width=200
        self.animate = ft.Animation(500, curve= ft.AnimationCurve.EASE_IN_OUT_BACK)
        self.boton = ft.Button("Menu", on_click= self.animarsidebar)
        self.content= ft.Column(controls = [
                                        self.boton
                                        
                                    ]
                            )


    def animarsidebar(self):
        if self.width == 200:
            self.width = 100
        elif self.width == 100:
            self.width = 200
        
