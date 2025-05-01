import flet as ft
from flet import Page, TextField, ElevatedButton, Text, Column, Container, alignment
from libros_ui import mostrar_inventario_ui, mostrar_info_libro_ui

def show_main_app(page: Page, username: str, go_back):

    page.title = 'Aplicación Principal'
    page.clean()

    def logout(e):
        page.clean()
        go_back()

    selected_section = Text("Seleccione una opción ;P", size=16, weight="bold")
    content = Column([Container(selected_section)], expand=True)

    def navigate_to_section(section: str):
        selected_section.value = f"{section}"
        content.controls.clear()
        content.controls.append(Container(selected_section))
        page.update()

    def style_button(text, icon, on_click, color=None):
        return Container(
            content=ElevatedButton(text, icon=icon, on_click=on_click, color=color),
            padding=10,
            bgcolor=ft.Colors.BLUE_50,
            border_radius=10,
        )

    def show_search_books(e=None):
        content.controls.clear()
        selected_section.value = "Buscar libros 🔎​"

        def ver_detalle_libro(nombre_libro):
            mostrar_info_libro_ui(page, content, nombre_libro, show_search_books)

        mostrar_inventario_ui(page, content, ver_detalle_libro)


    nav_buttons = Column([
        ft.Divider(height=80, color="transparent"),
        style_button("Home", ft.Icons.HOME, lambda e: navigate_to_section("Home 🏠​")),
        style_button("Buscar libros", ft.Icons.SEARCH, show_search_books),
        style_button("Mis libros", ft.Icons.BOOK, lambda e: navigate_to_section("Mis libros 📚​")),
        style_button("Cerrar sesión", ft.Icons.LOGOUT, logout, color="red")
    ], spacing=10)

    title = ft.Row([
        Container(
            content=Text(f"Bienvenid@, {username}! 🦉​", size=24, weight="bold"),
            padding=20,
            bgcolor=ft.Colors.BLUE_50,
            expand=True,
        )
    ])

    page.add(
        ft.Row(
            controls=[
                Container(nav_buttons, width=190, padding=10, bgcolor=ft.Colors.BLUE_50, border_radius=10),
                ft.VerticalDivider(width=1),
                Column(
                    controls=[
                        Container(title, bgcolor=ft.Colors.BLUE_50),
                        ft.Divider(height=1),
                        Container(content, expand=True)
                    ],
                    expand=True,
                )
            ],
            expand=True,
        )
    )
