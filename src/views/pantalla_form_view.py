import flet as ft
from components import CardContainer

class PantallaFormView(ft.Container):
    def __init__(self):
        super().__init__()

        #self.bgcolor = ft.Colors.RED
        self.expand = True
        self.padding = 10
        

        self.lbl_titulo = ft.Text(value = "Formulario",
                                  size= 20)
        self.lbl_descripcion = ft.Text(value= "Formuario")


        self.cnt_presentacion = CardContainer(
                                            content= ft.Row(
                                                             controls = [
                                                                         ft.Column(
                                                                                   controls= [self.lbl_titulo, self.lbl_descripcion]
                                                                                   )
                                                                         ]
                                                             )
                                             )


        self.cnt_enlaces = CardContainer(
                                         content= ft.Row(
                                                         controls = ft.Column(
                                                                              [ft.Image(src="icon.png",
                                                                                       width= 300,
                                                                                       height= 200),
                                                                                ft.TextField(),
                                                                                ft.TextField(),
                                                                                ft.TextField(),
                                                                                ft.TextField(),
                                                                                ft.TextField(),]
                                                                                       
                                                                              )
                                                         )
                                         )


        self.content = ft.Column(
                                 scroll= ft.ScrollMode.AUTO,
                                 controls = [self.cnt_presentacion, self.cnt_enlaces],)