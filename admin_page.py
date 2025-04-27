import flet as ft
from flet import ElevatedButton, Text, Column, Container, alignment

def admin_panel(page: ft.Page, go_back):
        page.title = 'Panel de administración'
        page.clean()

        def logout(e):
            page.clean()
            go_back()
        
        
        select = Text("Seleccione una opcion", size=16, weight="bold")

        def navigate_to_section(section: str):
              select.value = f"{section}"
              page.update()

        def style_button(text,icon,on_click, color=None):
            return Container(
                content=ElevatedButton(text, icon=icon, on_click=on_click, color=color),
                padding=10,
                bgcolor=ft.Colors.BLUE_50,
                border_radius=10,
            )
        
        nav_buttons = Column([
            ft.Divider(height=60, color="transparent"),
            style_button(
                text="Agregar libro",
                icon=ft.Icons.ADD, 
                on_click=lambda e: navigate_to_section("Agregar libro 📚​")
                ),        
            style_button(
                text="Eliminar libro",
                icon=ft.Icons.DELETE, 
                on_click=lambda e: navigate_to_section("Eliminar libro ❌​")),
            
            style_button(
                  text="Ver Inventario",
                  icon=ft.Icons.BOOK,
                  on_click=lambda e: navigate_to_section("Ver inventario 📦​")),

            style_button(
                text="Ver usuarios",
                icon=ft.Icons.PERSON, 
                on_click=lambda e: navigate_to_section("Ver usuarios 👤​")),
            
            
            style_button(text="Cerrar sesión",
                         icon=ft.Icons.LOGOUT,
                         color = "red", on_click=logout)
        ],
        spacing=10
        )
  
        title = ft.Row([
              Container(
                content=Text("Panel de Administracion ⚙️", size=24, weight="bold"),
                padding=20,
                bgcolor=ft.Colors.BLUE_50,
                expand=True,
                )
        ])
            
        content = Column([              
              Container(select),
        ], expand=True)

        page.add(
             ft.Row(
                   controls=[
                        Container(nav_buttons, width=190, padding=10, bgcolor=ft.Colors.BLUE_50),
                        ft.VerticalDivider(width=1),
                         Column(
                               controls=[
                                     Container(title, bgcolor=ft.Colors.BLUE_50),
                                     ft.Divider(height=1),   
                                     Container(content, expand=True),
                               ],
                               
                               expand=True,
                         )                         
                   ],
                   expand=True,
             ) 
    
        )
