import flet as ft

class Platillo(ft.TextField):
    def __init__(self, nombre_platillo):
        super().__init__()
        self.label = nombre_platillo
        self.tooltip = 'Ingrese la cantidad del platillo. (No es necesario agregar 0 para los que no se quieren)' 
        self.width = 200
        self.hint_text = 0
        self.filled = True
        self.value = None

class DatosCliente(ft.TextField):
    def __init__(self, texto_mostrado, autofocus = False):
        super().__init__()
        self.label = texto_mostrado
        self.autofocus = autofocus

def main(page):
    page.title = 'CDS Control de pedidos'    

    def borrar_campos(e):
        texto_nombre.autofocus = True
        texto_nombre.value = ''
        texto_direccion.value = ''
        texto_telefono.value = ''
        platillo_1.value = ''
        platillo_2.value = ''
        platillo_3.value = ''
        platillo_4.value = ''
        platillo_5.value = ''
        platillo_6.value = ''
        platillo_7.value = ''
        platillo_8.value = ''
        platillo_9.value = ''

        page.update()

    def agregar_informacion(e):
        if texto_nombre.value != '':    
            estado = '#7FE13B'
            if texto_estado.value == 'NE':
                estado = '#E1613B'
            b=ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(texto_nombre.value)),
                        ft.DataCell(ft.Text(texto_direccion.value)),
                        ft.DataCell(ft.Text(texto_telefono.value)),
                         ft.DataCell(ft.Text(platillo_1.value)),
                         ft.DataCell(ft.Text(platillo_2.value)),
                         ft.DataCell(ft.Text(platillo_3.value)),
                         ft.DataCell(ft.Text(platillo_4.value)),
                         ft.DataCell(ft.Text(platillo_5.value)),
                         ft.DataCell(ft.Text(platillo_6.value)),
                         ft.DataCell(ft.Text(platillo_7.value)),
                         ft.DataCell(ft.Text(platillo_8.value)),
                         ft.DataCell(ft.Text(platillo_9.value)),
                         ft.DataCell(ft.Text(texto_estado.value, color = estado)),
                         ft.DataCell(ft.Text(F'${round(value, 2)}')),
                         ft.DataCell(ft.Text(texto_pedido)),
                         ft.DataCell(boton_editar_registro),
                         ft.DataCell(boton_borrar_registro),
                        ])

            tabla_pedido.rows.insert(0, b)
        borrar_campos(e)
        
        page.update()
        

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
        icon = ft.icons.ADD,
        on_click = agregar_informacion
        )
    boton_borrar_pedido = ft.ElevatedButton(
        text="Borrar campos rellenos", 
        icon = ft.icons.DELETE, 
        bgcolor = '#B4583D',
        on_click = borrar_campos,
        color = '#FFFFFF'
        )
    boton_borrar_registro = ft.IconButton(
        icon = ft.icons.DELETE,
        icon_size = 20,
        tooltip = 'Eliminar registro'
    )
    boton_editar_registro = ft.IconButton(
        icon = ft.icons.EDIT,
        icon_size = 20,
        tooltip = 'Editar registro'
    )
    
    tabla_pedido = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Cliente", size=15)),
                ft.DataColumn(ft.Text("Dir.", size=15)),
                ft.DataColumn(ft.Text("Tel.", size=15), numeric=True),
                ft.DataColumn(ft.Text(f"{platillo_1.label}", size=15)),
                ft.DataColumn(ft.Text(f"{platillo_2.label}", size=15)),
                ft.DataColumn(ft.Text(f"{platillo_3.label}", size=15)),
                ft.DataColumn(ft.Text(f"{platillo_4.label}", size=15)),
                ft.DataColumn(ft.Text(f"{platillo_5.label}", size=15)),
                ft.DataColumn(ft.Text(f"{platillo_6.label}", size=15)),
                ft.DataColumn(ft.Text(f"{platillo_7.label}", size=15)),
                ft.DataColumn(ft.Text(f"{platillo_8.label}", size=15)),
                ft.DataColumn(ft.Text(f"{platillo_9.label}", size=15)),
                ft.DataColumn(ft.Text(f"Estado", size=15)),
                ft.DataColumn(ft.Text(f"Total", size=15)),
                ft.DataColumn(ft.Text(f"Hora Entrega", size=15)),
                ft.DataColumn(ft.Text()),
                ft.DataColumn(ft.Text()),
            ], 
    )

    columna_vista = ft.Column([tabla_pedido],scroll=True)
    fila_vista = ft.Row([columna_vista],expand=1,vertical_alignment=ft.CrossAxisAlignment.START, scroll=True)

    

    value = (platillo_1.value + platillo_2.value) * 60 # BORRAR EN MODIFICACIONES
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

    texto_estado = ft.TextField(
        disabled = True, 
        width = 50, 
        value = 'NE',
        tooltip = 'NE = No entregado\n E   = Entregado',
        text_align = ft.TextAlign.CENTER
    )

    texto_pedido = '12:00'
    
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
                    texto_estado
                ],
                height = 25
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
                    boton_agregar_pedido, boton_borrar_pedido
                ]
                ),
                ]
            )
        )
    page.add(fila_vista)
        
    
    
ft.app(main)