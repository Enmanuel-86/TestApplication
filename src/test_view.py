
import flet as ft
from views.pantalla_form_view import PantallaFormView

def main(page: ft.Page):
    page.padding = 0
    page.locale_configuration = ft.LocaleConfiguration(
        supported_locales=[ft.Locale("es", "ES")],
        current_locale=ft.Locale("es", "ES")
    )
    #page.width = 300
    #page.theme_mode = ft.ThemeMode.LIGHT
    controlTest = PantallaFormView()

    print(f"Ancho inicial: {page.width}px")

    # Función que se ejecuta al cambiar el tamaño de la ventana
    def al_redimensionar(e):
        print(f"Ancho actual: {page.width}px")

    # Escucha el evento de redimensionado
    #page.on_resized = lambda e: al_redimensionar(e)
    
 
    page.add(
        ft.Column(
            controls=[controlTest],
            expand= True
            
        )
    )

   

if __name__ == "__main__":
    ft.run(main)
