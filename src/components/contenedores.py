import flet as ft
import datetime

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

@ft.control
class DatePicker(ft.Container):
    def __init__(self, titulo:str):
        super().__init__()

        self.titulo = titulo
        

    def build(self):
        self.col={"xs": 12, "md": 3, "lg":3}

        fecha_defecto = datetime.datetime.now().strftime("%d/%m/%Y")
        today = datetime.datetime.now()
        self.lbl_fecha = ft.Text(value = fecha_defecto, tooltip= "Dia/Mes/Año")

        def handle_change(e: ft.Event[ft.DatePicker]):
            self.lbl_fecha.value = e.control.value.strftime('%d/%m/%Y')

        picker = ft.DatePicker(
                                first_date=datetime.datetime(year=1964, month=1, day=1),
                                last_date=datetime.datetime(year=today.year + 1, month=today.month, day=20),
                                current_date=today,
                                on_change=handle_change
                                )

        self.content = ft.Row(
                              controls=[
                                        ft.Button(
                                                  icon=ft.Icons.CALENDAR_MONTH,
                                                  on_click=lambda e: e.page.show_dialog(picker),
                                                  content= self.titulo,
                                                  tooltip= f"Pica el boton para seleccionar la {self.titulo.lower()}"
                                                  ),
                                        self.lbl_fecha
                                                  ]
                                                  )

        return super().build()