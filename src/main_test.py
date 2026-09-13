import flet as ft
from views.login_view import VwLogin

def main(page: ft.Page):
    page.padding = 0
    page.width = 500
    #page.theme_mode = ft.ThemeMode.LIGHT
    controlTest = VwLogin()
 
    page.add(
        ft.Row(
            controls=[controlTest]
            
        )
    )

   

if __name__ == "__main__":
    ft.run(main)
