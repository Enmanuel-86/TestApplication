import flet as ft
from components import CardContainer, TextFieldForm, TextFieldDatePicker


class PantallaFormView(ft.Container):
    def __init__(self):
        super().__init__()

        #self.bgcolor = ft.Colors.RED
        self.expand = True
        self.padding = 10
        

        self.lbl_titulo = ft.Text(value = "Formulario de prueba",
                                  size= 30,
                                  weight= ft.FontWeight.BOLD
                                  #expand= True,
                                  #bgcolor= "red"
                                  )
        self.lbl_descripcion = ft.Text(value= "Este formulario es para probar como obtener los valores de los controls")


        self.cnt_presentacion = CardContainer(
                                              
                                              content= ft.Column(
                                                                 ft.Row(controls = [self.lbl_titulo], alignment= ft.MainAxisAlignment.CENTER)
                                                                 )                
                                              )

        self.txt_primer_nombre = TextFieldForm(label= "Primer Nombre",
                                                tooltip= "Escribe tu nombre",
                                                on_change= lambda e: self.campos_tipo_texto(e),
                                                )
        self.txt_segundo_nombre = TextFieldForm(label= "Segundo Nombre", )
        self.txt_primero_apellido = TextFieldForm(label= "Primer Apellido")
        self.txt_segundo_apellido = TextFieldForm(label= "Segundo Apellido")
        self.txt_tercer_apellido = TextFieldForm(label= "Tercer Apellido")
        self.txt_cedula = TextFieldForm(label="Cédula")

        self.dd_genero = ft.DropdownM2(label= "Genero",
                                     col={"xs": 12, "md": 3, "lg":3},
                                     expand= True,
                                     options= [
                                         ft.DropdownOption("Masculino"),
                                         ft.DropdownOption("Femenino")
                                     ]
                                        )

        self.txt_fecha_nacimiento = TextFieldDatePicker(label = "Fecha de nacimiento" )

        self.btn_validar = ft.Button(content= "Validar")

        self.cnt_form_datos_personales = CardContainer(
                                                       content= ft.ResponsiveRow(
                                                                       
                                                                       
                                                                       controls=[
                                                                                 self.txt_primer_nombre,
                                                                                 self.txt_segundo_nombre,
                                                                                 self.txt_primero_apellido,
                                                                                 self.txt_segundo_apellido,
                                                                                 self.txt_tercer_apellido,
                                                                                 self.dd_genero,
                                                                                 self.txt_cedula,
                                                                                 self.txt_fecha_nacimiento
                                                                                 
                                                                                 ]
                                                                       )
                                                       )


        self.cnt_enlaces = CardContainer(
                                         content= ft.Row(
                                                         controls = ft.Column(
                                                                              [self.btn_validar]   
                                                                              ),
                                                        alignment= ft.MainAxisAlignment.END
                                                         )
                                         )


        self.content = ft.Column(
                                 scroll= ft.ScrollMode.AUTO,
                                 controls = [
                                             self.cnt_presentacion, 
                                             self.cnt_form_datos_personales, 
                                             self.cnt_enlaces],)


    def campos_tipo_texto(self, e):
        """
            Metodo para verificar que el texto no contenga numeros
        """

        valor = e.control.value

        if valor and valor.isdigit():
            e.control.error = "No puede ingresar numeros"
        else:
            e.control.error = None
        e.page.update()

