import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column, ControlEvent
from database import verificar_usuario,agregar_usuario

def main(page: ft.Page):
    page.title = 'Pagina de bienvenida'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False


    def show_landing():
        page.clean()
        
        text_username = ft.TextField(label='Usuario', width=200)
        text_password = ft.TextField(label='Contraseña', width=200, password=True)

        def login(e: ft.ControlEvent):
            if text_username.value and text_password.value:
                if verificar_usuario(text_username.value,text_password.value):
                    print(f"Usuario:, {text_username.value}")
                    print(f"Contraseña:, {text_password.value}")
                    page.clean()
                    page.add(ft.Text(f"Bienvenido, {text_username.value}!", size=20))
                else:
                    show_signup()                    
            else:
                print("Por favor, ingrese su usuario y contraseña.")
                page.snack_bar.open = True
                page.update()

        text_password.on_submit = login


        page.add(
            ft.Column(
                [
                ft.Text("Librería Búho {O,O}", size=30, weight="bold"),
                ft.Text("¡La aplicacion que conecta todas las bibliotecas Unison!", size=15),
                text_username,
                text_password,
                ft.ElevatedButton("Iniciar sesión", on_click=login),
                ft.ElevatedButton("¿No tienes cuenta? Registrate", on_click=lambda e: show_signup()),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )


    def show_signup():
        page.title = "Sign Up"

        text_username = TextField(label='Usuario', width=200)
        text_password = TextField(label='Contraseña', width=200, password=True)
        checkbox_agree = Checkbox(label='Estoy de acuerdo con los terminos y condiciones', value=False)
        button_submit = ElevatedButton(text='Registrarse', width=200, disabled=True)

        def validate(e: ControlEvent):
            button_submit.disabled = not all([text_username.value, text_password.value, checkbox_agree.value])
            page.update()

        def submit(e: ControlEvent):
            if agregar_usuario(text_username.value,text_password.value):
                print("Registrado:", text_username.value)
            else:
                print("Fallo al registrar el usuario")
            page.clean()
            page.add( Text(f"Gracias por registrarte, {text_username.value}!", size=20))

        text_username.on_change = validate
        text_password.on_change = validate
        checkbox_agree.on_change = validate
        button_submit.on_click = submit

        page.clean()
        page.add(
            Column([
                Text("Registrarse", size=24, weight="bold"),
                text_username,
                text_password,
                checkbox_agree,
                button_submit,
                ElevatedButton("Atras", on_click=lambda e: show_landing())
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )


    show_landing()


if __name__ == "__main__":
    ft.app(target=main)
