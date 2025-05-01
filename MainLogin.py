import flet as ft
import re
from flet import TextField, Checkbox, ElevatedButton, Text, Column, ControlEvent, Container, alignment
from database_utils import verificar_usuario, agregar_usuario,buscar_libro,buscar_autor

def main(page: ft.Page):
    page.title = 'Librería Búho​'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    def show_landing():
        page.clean()

        text_username = TextField(label='Usuario/Correo', width=200)
        text_password = TextField(label='Contraseña', width=200, password=True)
        message = Text("", color="red")

        def login(e: ControlEvent):
            if text_username.value and text_password.value:
                success, result = verificar_usuario(text_username.value, text_password.value)
                if success:
                    page.clean()
                    show_main_app(result)
                else:
                    message.value = result
                    page.update()
            else:
                message.value = "Por favor, complete todos los campos."
                page.update()

        content = Column(
            [
                Text("Librería Búho 🦉📚​​", size=30, weight="bold"),
                Text("¡Conecta todas las bibliotecas Unison!", size=15),
                text_username,
                text_password,
                ElevatedButton("Iniciar sesión", on_click=login),
                ElevatedButton("Admin ⚙️", on_click=lambda e: show_main_app("admin")),
                ElevatedButton("¿No tienes cuenta? Regístrate", on_click=lambda e: show_signup()),
                message
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        page.add(Container(content=content, alignment=alignment.center, expand=True))

    def show_signup():
        page.clean()

        text_username = TextField(label='Usuario', width=200)
        text_email = TextField(label='Correo electronico', width=200)
        text_password = TextField(label='Contraseña', width=200, password=True)
        text_password_confirm = TextField(label='Confirmar contraseña', width=200, password=True)
        checkbox_agree = Checkbox(label='Acepto los términos', value=False)
        button_submit = ElevatedButton(text='Registrarse', width=200, disabled=True)
        message = Text("", color="red")

        def validate(e: ControlEvent):
            password_valid = text_password.value == text_password_confirm.value
            all_filled = all([
                  text_username.value,
                  text_email.value,
                  text_password.value, 
                  text_password_confirm.value, 
                  checkbox_agree.value
                  ])
            button_submit.disabled = not (all_filled and password_valid)
            message.value = "" if password_valid else "Las contraseñas no coinciden."    

            if not validate_email(text_email.value):
                message.value = "Correo inválido."
                button_submit.disabled = True
                page.update()
                return
            page.update()

        def submit(e: ControlEvent):
            if text_password.value != text_password_confirm.value:
                message.value = "Las contraseñas no coinciden."
                page.update()
                return
            
            success, msg = agregar_usuario(text_username.value,text_email.value, text_password.value)
            if success:
                page.clean()
                show_main_app(text_username.value)
            else:
                message.value = msg
                page.update()

        def validate_email(email: str) -> bool:
            regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            return re.match(regex, email) is not None
        
        
        text_username.on_change = validate
        text_email.on_change = validate
        text_password.on_change = validate
        text_password_confirm.on_change = validate
        checkbox_agree.on_change = validate
        button_submit.on_click = submit

        content = Column([
            Text("Registrarse", size=24, weight="bold"),
            text_username,
            text_email,
            text_password,
            text_password_confirm,
            checkbox_agree,
            button_submit,
            ElevatedButton("Volver", on_click=lambda e: show_landing()),
            message
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        page.add(Container(content=content, alignment=alignment.center, expand=True))

    # Main app function
    # This function will be called after successful login
    def show_main_app(username: str):
        page.clean()

        selected_section = Text("Seleccione una opcion ;P", size=16, weight="bold")
        
        def navigate_to_section(section: str):
            selected_section.value = f"{section}"
            page.update()
        
        def logout(e):
            page.clean()
            show_landing()

        nav_buttons = Column([
            ElevatedButton("Home", on_click=lambda e: navigate_to_section("Home")),
            ElevatedButton("Buscar libros", on_click=lambda e: show_search_books("Buscar libros")),
            ElevatedButton("Mis libros", on_click=lambda e: navigate_to_section("Mis libros")),
            ElevatedButton("Cerrar sesión", color = "red", on_click=logout),
        ],
        spacing=10
        )

        content = Column([
            Text(f"Bienvenid@, {username}! 🦉​", size=24, weight="bold"),
            selected_section
        ])

        page.add(
            Container(
                content=ft.Row(
                    controls=[
                        Container(nav_buttons, width=150,padding=10),
                        Container(content, expand=True, padding=10),
                    ],
                    expand=True,
                ),
                expand=True,
            )
        )

        def show_search_books(e):
            page.clean()
            search_text = TextField(label='Buscar libros o autor', width=200)
            search_button = ElevatedButton("Buscar", on_click=lambda e: search_books(search_text.value))
            message = Text("", color="red")

            def search_books(query):               
              libro_info = buscar_libro(query) or buscar_autor(query)
              if libro_info:
                  message.value = f"Libro encontrado: {libro_info}"     
              else:
                  message.value = "Libro no encontrado"                                          
              page.update()            
            
            content = Column([
                Text("Buscar libros", size=24, weight="bold"),
                search_text,
                search_button,
                message
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)

            page.add(Container(content=content, alignment=alignment.center, expand=True))





    show_landing()

if __name__ == "__main__":
    ft.app(target=main)
