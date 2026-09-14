import flet as ft

# Contenedor base
@ft.control
class TextFieldBase(ft.TextField):
    def build(self):
        self.col={"xs": 12, "md": 3, "lg":3}
        return super().build()
    

@ft.control
class TextFieldForm(TextFieldBase):
    def build(self):
        
        return super().build()