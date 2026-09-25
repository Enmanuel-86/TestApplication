import flet as ft
from controllers import (SideBarController)
from utils.funciones import funciones_sistema




def main(page: ft.Page):
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK
    page.locale_configuration = ft.LocaleConfiguration(
        supported_locales=[ft.Locale("es", "ES")],
        current_locale=ft.Locale("es", "ES")
    )

    ctn_espacio_principal = ft.Container(expand= True)
    sidebar = SideBarController()

    ctn_espacio_principal.content = funciones_sistema.PANTALLAS_CONTROLLERS["Login"]

    funciones_sistema.CTN_ESPACIO_PRINCIPAL = ctn_espacio_principal
    funciones_sistema.SIDEBAR = sidebar


    sidebar.visible = False
 
    page.add(
        ft.Row(
            controls=[sidebar, ctn_espacio_principal],
            expand=True,
            spacing= 0
        )
    )
    

if __name__ == "__main__":

    ft.run(main)

    """
    ft.run(main,
           host = "0.0.0.0",
           port = 8080 ,
           view= ft.AppView.WEB_BROWSER)
    """