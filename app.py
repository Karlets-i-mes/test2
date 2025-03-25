import flet as ft

def main(page: ft.Page):
    page.title = "Ejemplo de Flet"

    def boton_click(e):
        texto.value = "¡Botón clickeado!"
        page.update()

    texto = ft.Text("Haz clic en el botón")
    boton = ft.ElevatedButton("Clic aquí", on_click=boton_click)

    page.add(
        ft.Column([
            texto,
            boton,
        ])
    )

ft.app(target=main, view=ft.WEB_BROWSER)