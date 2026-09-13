"""
import flet as ft
from views import PantallaDeBienvenidaView

def main(page: ft.Page):
    page.padding = 0
    page.width = 500
    #page.theme_mode = ft.ThemeMode.LIGHT
    controlTest = PantallaDeBienvenidaView()
 
    page.add(
        ft.Column(
            controls=[controlTest],
            expand= True
            
        )
    )

   

if __name__ == "__main__":
    ft.run(main)
"""