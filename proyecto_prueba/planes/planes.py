import reflex as rx
from proyecto_prueba.state.PageState import State

def planes_page() -> rx.Component:
    return rx.vstack(
        rx.text("Planes"),
        rx.unordered_list(
            rx.foreach(State.planes, lambda item: rx.list.item(rx.text(item))),
        ),
        padding="20px",
        width="50%",
        on_mount=State.obtener_planes
    )