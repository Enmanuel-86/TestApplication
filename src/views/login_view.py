import flet as ft


class LoginView(ft.Container):
    def __init__(self):
        super().__init__()

        # Configuracion
        #self.bgcolor = ft.Colors.BLUE
        self.padding = 20
        self.border_radius = 10
        self.expand = True
        
        self.lbl_titulo = ft.Text(value= "Login", size= 25)
        self.txt_nombre_usuario = ft.TextField(label= "Usuario",
                                           icon= ft.Icons.PERSON
                                           )
        self.txt_contrasenia_usuario = ft.TextField(label= "Contraseña",
                                                password= True,
                                                icon= ft.Icons.LOCK,
                                                can_reveal_password= True
                                                )
        self.btn_ingresar = ft.Button("Ingresar")

        self.dlg_alerta_campos_vacios = ft.AlertDialog(title= ft.Text("Aviso para el usuario"),
                                                   content= ft.Text("Por favor debe ingresar su nombre de usuario y contraseña"),
                                                   actions= [ft.Button(content = "ok", on_click= lambda e: e.control.page.pop_dialog())],
                                                   modal= True
                                     )

        self.dlg_contrasenia_incorrecta = ft.AlertDialog(title= ft.Text("Aviso para el usuario"),
                                                           content= ft.Text("Contraseña incorrecta"),
                                                           actions= [ft.Button(content = "ok", on_click= lambda e: e.control.page.pop_dialog())],
                                                           modal= True
                                             )

        self.dlg_usuario_no_existe = ft.AlertDialog(title= ft.Text("Aviso para el usuario"),
                                                                   content= ft.Text("El Usuario no esta registrado en el sistema"),
                                                                   actions= [ft.Button(content = "ok", on_click= lambda e: e.control.page.pop_dialog())],
                                                                   modal= True
                                                     )

        self.cnt_espacio_principal = ft.Container(bgcolor= ft.Colors.BLUE_900,
                                              border_radius= 30,
                                              padding= 30,
                                              content= ft.Column(controls= [self.lbl_titulo,
                                                                            self.txt_nombre_usuario,
                                                                            self.txt_contrasenia_usuario,
                                                                            self.btn_ingresar],
                                                                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                                                            alignment= ft.MainAxisAlignment.CENTER
                                          
                                                                )
                                            )


        self.content = ft.Column(controls = [self.cnt_espacio_principal],
                                 alignment= ft.MainAxisAlignment.CENTER,
                                 horizontal_alignment= ft.CrossAxisAlignment.CENTER)

        
        
        