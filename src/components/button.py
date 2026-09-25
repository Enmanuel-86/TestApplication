import flet as ft

@ft.control
class ButtonBase(ft.Button):
    def build(self):
        return super().build()

@ft.control
class ButtonSideBar(ft.TextButton):
    def __init__(self, titulo, icono, **kwargs):
        super().__init__(**kwargs)

        self.titulo = ft.Text(
                              value= titulo,
                              no_wrap= True,
                              color= ft.Colors.WHITE)

        self.icon = ft.Icon(icon = icono, color= ft.Colors.WHITE, size= 20)

    def build(self):
        self.content = ft.Row(controls = [self.titulo])
        self.expand= True
        #self.height = 40
        
        
        
        return super().build()