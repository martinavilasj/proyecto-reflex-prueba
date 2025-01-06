import reflex as rx
from proyecto_prueba.routes import Route

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.text(
            "Clientes",
            font_size="0.8em",
            ),
            href=Route.CLIENTES.value,
        ),
        rx.link(
            rx.text(
                "Planes",
                font_size="0.8em",
            ),
            href=Route.PLANES.value,
        ),
        rx.link(
            rx.text(
                "Finanzas",
                font_size="0.8em",
            ),
            href=Route.FINANZAS.value,
        ),
        position="sticky",
        bg="grey",
        padding="20px",
        width="100%",
        z_index="3",
    )
