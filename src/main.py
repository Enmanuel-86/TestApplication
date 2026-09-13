import flet as ft
from controllers import (LoginController, SideBarController)

def main(page: ft.Page):
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK
    espacio_principal = ft.Container(expand= True)
    sidebar = SideBarController(espacio_principal)
    login = LoginController(sidebar, espacio_principal)
    espacio_principal.content = login


    sidebar.visible = False
 
    page.add(
        ft.Row(
            controls=[sidebar, espacio_principal],
            expand=True,
            spacing= 0
        )
    )
    

if __name__ == "__main__":
    ft.run(main)
