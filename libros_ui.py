import flet as ft
from flet import Text, ElevatedButton, Column, Container, alignment, Image
import database_utils

def mostrar_inventario_ui(page, content_column: Column, on_libro_click):
    libros = database_utils.consultar_inventario()
    content_column.controls.clear()

    if not libros or libros == False:
        content_column.controls.append(Text("❗ No se pudieron cargar los libros.", color="red"))
    else:
        lista_libros = Column(spacing=10)
        for nombre, autor in libros:
            btn = ElevatedButton(
                text=f"{nombre} - {autor}",
                on_click=lambda e, nombre=nombre: on_libro_click(nombre)
            )
            lista_libros.controls.append(btn)

        content_column.controls.append(lista_libros)
    
    page.update()



def mostrar_info_libro_ui(page, content_column: Column, nombre_libro: str, on_back):
    libro = database_utils.consultar_info_libro(nombre_libro)
    content_column.controls.clear()

    if not libro or libro == False:
        content_column.controls.append(Text("❗ No se pudo cargar la información del libro.", color="red"))
    else:
        nombre, autor, publicacion, genero, sinopsis, portada = libro

        detalle = Column([
            Container(
                width=200,
                height=300,
                bgcolor=ft.Colors.GREY_300,
                border_radius=10,
                alignment=alignment.center,
                content=Image(
                    src=f"images/{portada}",
                    fit=ft.ImageFit.COVER,
                ) if portada else Text("Sin portada")
            ),
            Text(f"Título: {nombre}", size=20, weight="bold"),
            Text(f"Autor: {autor}"),
            Text(f"Fecha de publicación: {publicacion}"),
            Text(f"Género: {genero}"),
            Text(f"Sinopsis:", weight="bold"),
            Text(sinopsis, max_lines=10, overflow="ellipsis"),
            ElevatedButton("Volver", on_click=lambda e: on_back())
        ], spacing=10)

        content_column.controls.append(detalle)

    page.update() 
    
