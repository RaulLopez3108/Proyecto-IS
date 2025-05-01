import flet as ft
from flet import ElevatedButton, Text, Column, Container, TextField, Row, alignment, Image
import database_utils
from libros_ui import mostrar_inventario_ui, mostrar_info_libro_ui

def admin_panel(page: ft.Page, go_back):
    page.title = 'Panel de administración'
    page.clean()

    def logout(e):
        page.clean()
        go_back()

    select = Text("Seleccione una opción", size=16, weight="bold")
    content = Column([], expand=True)

    def navigate_to_section(section: str):
        select.value = section
        content.controls.clear()

        if section == "Agregar libro 📚​":
            mostrar_formulario_agregar_libro()
        elif section == "Eliminar libro ❌​":
            mostrar_formulario_eliminar_libro()
        elif section == "Ver inventario 📦​":
            mostrar_inventario()
        elif section == "Ver usuarios 👤​":
            content.controls.append(Text("Funcionalidad de ver usuarios aún no implementada.", color="blue"))

        page.update()

    def style_button(text, icon, on_click, color=None):
        return Container(
            content=ElevatedButton(text, icon=icon, on_click=on_click, color=color),
            padding=10,
            bgcolor=ft.Colors.BLUE_50,
            border_radius=10,
        )

    def mostrar_inventario():
        def ver_info_libro(nombre_libro):
            mostrar_info_libro_ui(page, content, nombre_libro, mostrar_inventario)
        mostrar_inventario_ui(page, content, ver_info_libro)


    def mostrar_formulario_agregar_libro():
        titulo_field = TextField(label="Título")
        autor_field = TextField(label="Autor")
        fecha_field = TextField(label="Fecha de publicación (YYYY-MM-DD)")
        genero_field = TextField(label="Género")
        sinopsis_field = TextField(label="Sinopsis", multiline=True, min_lines=3)
        portada_field = TextField(label="Nombre del archivo de portada (ej: portada1.jpg)")
        mensaje = Text("")

        def guardar_libro(e):
            if not all([titulo_field.value, autor_field.value, fecha_field.value, genero_field.value, sinopsis_field.value, portada_field.value]):
                mensaje.value = "❗ Todos los campos son obligatorios."
                mensaje.color = "red"
            else:
                success, response = database_utils.agregar_libro(
                    titulo_field.value, autor_field.value, fecha_field.value,
                    genero_field.value, sinopsis_field.value, portada_field.value
                )
                mensaje.value = "✅ Libro agregado exitosamente." if success else "❗ Error: " + response
                mensaje.color = "green" if success else "red"

                if success:
                    for field in [titulo_field, autor_field, fecha_field, genero_field, sinopsis_field, portada_field]:
                        field.value = ""

            page.update()

        content.controls.append(Column([
            titulo_field, autor_field, fecha_field, genero_field,
            sinopsis_field, portada_field,
            ElevatedButton("Guardar libro", on_click=guardar_libro),
            mensaje
        ], spacing=10))

    def mostrar_formulario_eliminar_libro():
        nombre_field = TextField(label="Nombre del libro a eliminar")
        mensaje = Text("")

        def eliminar_libro(e):
            if not nombre_field.value:
                mensaje.value = "❗ El nombre del libro es obligatorio."
                mensaje.color = "red"
            else:
                success, response = database_utils.eliminar_libro(nombre_field.value)
                mensaje.value = "✅ Libro eliminado exitosamente." if success else "❗ Error: " + response
                mensaje.color = "green" if success else "red"
                if success:
                    nombre_field.value = ""

            page.update()

        content.controls.append(Column([
            nombre_field,
            ElevatedButton("Eliminar libro", on_click=eliminar_libro),
            mensaje
        ], spacing=10))

    nav_buttons = Column([
        ft.Divider(height=60, color="transparent"),
        style_button("Agregar libro", ft.Icons.ADD, lambda e: navigate_to_section("Agregar libro 📚​")),
        style_button("Eliminar libro", ft.Icons.DELETE, lambda e: navigate_to_section("Eliminar libro ❌​")),
        style_button("Ver Inventario", ft.Icons.BOOK, lambda e: navigate_to_section("Ver inventario 📦​")),
        style_button("Ver usuarios", ft.Icons.PERSON, lambda e: navigate_to_section("Ver usuarios 👤​")),
        style_button("Cerrar sesión", ft.Icons.LOGOUT, logout, color="red")
    ], spacing=10)

    title = ft.Row([
        Container(Text("Panel de Administración ⚙️", size=24, weight="bold"), padding=20, bgcolor=ft.Colors.BLUE_50, expand=True)
    ])

    page.add(ft.Row([
        Container(nav_buttons, width=190, padding=10, bgcolor=ft.Colors.BLUE_50),
        ft.VerticalDivider(width=1),
        Column([
            Container(title, bgcolor=ft.Colors.BLUE_50),
            ft.Divider(height=1),
            Container(select),
            Container(content, expand=True),
        ], expand=True)
    ], expand=True))
