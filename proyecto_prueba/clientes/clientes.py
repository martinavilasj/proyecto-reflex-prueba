import reflex as rx

from proyecto_prueba.clientes.formulario import *
from proyecto_prueba.state.PageState import State
from proyecto_prueba.model.Client import Client

def delete_alert_dialog(user: Client):
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button("Borrar", color_scheme="red"),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title("Confirmar Borrado"),
            rx.alert_dialog.description(
                rx.vstack(
                    rx.text("¿Está seguro que desea borrar al cliente?", size="3", weight="bold"),
                    rx.text(f"{user.nombre} {user.apellido}"),
                    rx.text(f"Documento: {user.documento}"),
                    spacing="2",
                ),
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button("Cancelar", variant="soft"),
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Confirmar",
                        color_scheme="red",
                        on_click=State.borrar_cliente(user.id),
                    ),
                ),
                spacing="3",
                justify="end",
            ),
        ),
    )

def mostrar_cliente(user: Client):
    return rx.table.row(
        rx.table.cell(user.id),
        rx.table.cell(user.fecha_ingreso),
        rx.table.cell(user.nombre),
        rx.table.cell(user.apellido),
        rx.table.cell(user.documento),
        rx.table.cell(user.plan),
        rx.table.cell(user.observaciones),
        rx.table.cell(delete_alert_dialog(user)),
    )

def clientes() -> rx.Component:
    return rx.vstack(
        rx.accordion.root(
            rx.accordion.item(
                header = "Nuevo Cliente",
                content = form_nuevo_cliente(),
                disabled=False,
            ),
            collapsible=True,
            width="300px",
            color_scheme="grass",
            variant="soft",
        ),
        rx.input(
            placeholder="Buscar acá...",
            on_change=lambda value: State.buscar_cliente(value),
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("id"),
                    rx.table.column_header_cell("Fecha ingreso"),
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell("Apellido"),
                    rx.table.column_header_cell("Documento"),
                    rx.table.column_header_cell("Plan"),
                    rx.table.column_header_cell("Observaciones"),
                    rx.table.column_header_cell("Acciones"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    State.clientes, mostrar_cliente
                )
            )
        ),
        padding="20px",
        width="100%",
        on_mount=State.obtener_clientes
    )