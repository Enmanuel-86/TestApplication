import flet as ft
import datetime

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

@ft.control
class TextFieldDatePicker(TextFieldForm):

    def build(self):
        
        fecha_defecto = datetime.datetime.now().strftime("%d/%m/%Y")
        today = datetime.datetime.now()

        self.suffix_icon= ft.IconButton(icon = ft.Icons.CALENDAR_MONTH, on_click=lambda e: e.page.show_dialog(self.picker))
        self.hint_text = "Haz click al boton del calendario"
        self.hint_style = ft.TextStyle(size=12)
        self.read_only = True
        self.tooltip= f"Haz click al boton del calendario"

        self.picker = ft.DatePicker(
                                        first_date=datetime.datetime(year=1964, month=1, day=1),
                                        last_date=datetime.datetime(year=today.year + 1, month=today.month, day=20),
                                        current_date=today,
                                        on_change= self.handle_change
                                        )


        return super().build()

    def handle_change(self, e: ft.Event[ft.DatePicker]):
        self.value = e.control.value.strftime('%d/%m/%Y')
    
            