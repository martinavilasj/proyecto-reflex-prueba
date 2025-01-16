import reflex as rx

from proyecto_prueba.clientes.formulario import *
from proyecto_prueba.state.PageState import State

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
        #rx.text(State.clientes),
        padding="20px",
        width="50%",
        on_mount=State.obtener_clientes
    )