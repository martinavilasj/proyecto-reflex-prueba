import reflex as rx

from proyecto_prueba.clientes.formulario import *
from proyecto_prueba.state.PageState import State
from proyecto_prueba.model.Client import Client

def mostrar_cliente(user: Client):
    return rx.table.row(
        rx.table.cell(user.id),
        rx.table.cell(user.fecha_ingreso),
        rx.table.cell(user.nombre),
        rx.table.cell(user.apellido),
        rx.table.cell(user.documento),
        rx.table.cell(user.plan),
        rx.table.cell(user.observaciones),
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