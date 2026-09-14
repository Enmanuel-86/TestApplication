import flet as ft
from controllers import (LoginController, SideBarController)
from utils.funciones import funciones_sistema



def main(page: ft.Page):
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK

    espacio_principal = ft.Container(expand= True)
    sidebar = SideBarController(espacio_principal)
    funciones_sistema.SIDEBAR = sidebar
    funciones_sistema.ESPACIO_PRINCIPAL = espacio_principal

    espacio_principal.content = funciones_sistema.PANTALLAS["Login"]()

    


    sidebar.visible = False
 
    page.add(
        ft.Row(
            controls=[sidebar, espacio_principal],
            expand=True,
            spacing= 0
        )
    )
    

if __name__ == "__main__":

    #ft.run(main)

    #"""
    ft.run(main,
           host = "0.0.0.0",
           port = 8080 ,
           view= ft.AppView.WEB_BROWSER)
    #"""