import flet as ft
from views.sidebar_view import SideBarView
from controllers import LoginController

def main(page: ft.Page):
    page.padding = 0
    #page.theme_mode = ft.ThemeMode.LIGHT
    sidebar = SideBarView()
    login = LoginController(sidebar)


    espacio_principal = ft.Container(bgcolor= ft.Colors.GREEN,
                                     expand= True,
                                     content= login)

    



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
