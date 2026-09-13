import flet as ft
from components import CardContainer

class PantallaDeBienvenidaView(ft.Container):
    def __init__(self):
        super().__init__()

        #self.bgcolor = ft.Colors.RED
        self.expand = True
        self.padding = 10
        

        self.lbl_titulo = ft.Text(value = "Bienvenido al sistema hecho con flet",
                                  size= 20)
        self.lbl_descripcion = ft.Text(value= "Este mini proyecto consiste en la elaboracion de un sistema sencillo para aprender a usar flet")


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
                                                                              ft.Image(src="icon.png",
                                                                                       width= 300,
                                                                                       height= 200)
                                                                              )
                                                         )
                                         )


        self.content = ft.Column(
                                 scroll= ft.ScrollMode.AUTO,
                                 controls = [self.cnt_presentacion, self.cnt_enlaces],)