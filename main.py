import flet as ft

class Platillo(ft.TextField):
    def __init__(self, nombre_platillo):
        super().__init__()
        self.label = nombre_platillo
        self.tooltip = 'Ingrese la cantidad del platillo. (No es necesario agregar 0 para los que no se quieren)' 
        self.width = 200
        self.hint_text = 0
        self.filled = True

class DatosCliente(ft.TextField):
    def __init__(self, texto_mostrado, autofocus = False):
        super().__init__()
        self.label = texto_mostrado
        self.autofocus = autofocus

def main(page):
    page.title = 'CDS Control de pedidos'    

    texto_nombre = DatosCliente(
        'Ingresa nombre del cliente',
        autofocus = True
    )
    texto_direccion = DatosCliente(
        'Ingresa dirección del cliente'
    )
    texto_telefono = DatosCliente(
        'Ingresa teléfono del cliente'
    )
    
    platillo_1 = Platillo('Mole')
    platillo_2 = Platillo('Pollo')
    platillo_3 = Platillo('Adobado')
    platillo_4 = Platillo('Calabacitas')
    platillo_5 = Platillo('Costillas')
    platillo_6 = Platillo('Albóndigas')
    platillo_7 = Platillo('Empanizado de pollo')
    platillo_8 = Platillo('Empanizao de res')
    platillo_9 = Platillo('Otro')
    
    texto_cantidad = ft.Container(
        ft.Text(
            'Cantidades', 
            font_family = 'Verdana',
            size = 15
        ),
        padding=20,
        alignment = ft.alignment.bottom_left
    )
    
    boton_agregar_pedido = ft.ElevatedButton(
        text="Agregar pedido", 
        icon = ft.icons.ADD
        )
    boton_borrar_pedido = ft.ElevatedButton(
        text="Borrar campos rellenos", 
        icon = ft.icons.DELETE, 
        bgcolor = '#B4583D'
        )
    
    tabla_pedido = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Cliente")),
                ft.DataColumn(ft.Text("Dir.")),
                ft.DataColumn(ft.Text("Tel."), numeric=True),
                ft.DataColumn(ft.Text(f"{platillo_1.label}")),
                ft.DataColumn(ft.Text(f"{platillo_2.label}")),
                ft.DataColumn(ft.Text(f"{platillo_3.label}")),
                ft.DataColumn(ft.Text(f"{platillo_4.label}")),
                ft.DataColumn(ft.Text(f"{platillo_5.label}")),
                ft.DataColumn(ft.Text(f"{platillo_6.label}")),
                ft.DataColumn(ft.Text(f"{platillo_7.label}")),
                ft.DataColumn(ft.Text(f"{platillo_8.label}")),
                ft.DataColumn(ft.Text(f"{platillo_9.label}")),
                ft.DataColumn(ft.Text(f"Estado")),
                ft.DataColumn(ft.Text(f"Total")),
                ft.DataColumn(ft.Text(f"Hora Entrega")),
            ]
    )
    
    value = 350.00 # BORRAR EN MODIFICACIONES
    subtotal = ft.Container(
                    content=
                        ft.Column(
                            [
                                ft.Text(f'${value}', size=35),
                                ft.Text("Total", size = 25)  
                            ]
                        ),
                    alignment=ft.alignment.center,
                    margin=10,
                    padding=10,
                    bgcolor='#c88d65',
                    width=180,
                    height=120,
                    border_radius=10,
                )
    
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.LOCAL_RESTAURANT),
        leading_width=20,
        title=ft.Text("Barra de selección de pedido"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(
                ft.icons.DELIVERY_DINING,
                        tooltip = 'Botón para cambiar al pánel de control de pedidos a enviar'
                ),
            ft.IconButton(ft.icons.STORE,
                          tooltip = 'Botón para cambiar al pánel de control de pedidos en tienda'
                          ),
                        
            ft.PopupMenuButton(
            ),
        ],
    )
    
    page.add(
        ft.Column(
            [
            ft.Row(
                [
                    texto_nombre, texto_direccion, texto_telefono, subtotal
                ]  
                    ),
            ft.Row(
                [
                    boton_agregar_pedido, boton_borrar_pedido
                ]
                ),
            ft.Row(
                [
                    texto_cantidad
                ]
                ),
            ft.Row(
                [
                    platillo_1, platillo_2, platillo_3, platillo_4, platillo_5, platillo_6, platillo_7, platillo_8, platillo_9
                ]
                    ),
            ft.Row(
                [
                    tabla_pedido
                ])
                ]
            )
        )
        
    
    
ft.app(main)