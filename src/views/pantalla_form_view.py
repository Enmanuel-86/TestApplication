import flet as ft
from components import CardContainer, TextFieldForm

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

        self.txt_primer_nombre = TextFieldForm(label= "Primer Nombre", tooltip= "Escribe tu nombre")
        self.txt_segundo_nombre = TextFieldForm(label= "Segundo Nombre", )
        self.txt_primero_apellido = TextFieldForm(label= "Primer Apellido")
        self.txt_segundo_apellido = TextFieldForm(label= "Segundo Apellido")
        self.txt_tercer_apellido = TextFieldForm(label= "Tercer Apellido")

        self.cnt_form_datos_personales = CardContainer(
                                                       content= ft.ResponsiveRow(
                                                                       
                                                                       
                                                                       controls=[
                                                                                 self.txt_primer_nombre,
                                                                                 self.txt_segundo_nombre,
                                                                                 self.txt_primero_apellido,
                                                                                 self.txt_segundo_apellido,
                                                                                 self.txt_tercer_apellido
                                                                                 ]
                                                                       )
                                                       )


        self.cnt_enlaces = CardContainer(
                                         content= ft.Row(
                                                         controls = ft.Column(
                                                                              [ft.Image(src="icon.png",
                                                                                       width= 300,
                                                                                       height= 200)]
                                                                                       
                                                                              )
                                                         )
                                         )


        self.content = ft.Column(
                                 scroll= ft.ScrollMode.AUTO,
                                 controls = [
                                             self.cnt_presentacion, 
                                             self.cnt_form_datos_personales, 
                                             self.cnt_enlaces],)

