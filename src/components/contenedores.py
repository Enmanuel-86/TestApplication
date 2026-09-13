import flet as ft

# Contenedor base
@ft.control
class ContenedorBase(ft.Container):
    def build(self):
        self.bgcolor= ft.Colors.WHITE_10
        self.padding = 20
        self.border_radius= 10
        return super().build()
    

@ft.control
class CardContainer(ContenedorBase):
    def build(self):
        return super().build()