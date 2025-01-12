import reflex as rx
import proyecto_prueba.api.api as api

class State(rx.State):
    planes = api.planes()

def planes_page() -> rx.Component:
    return rx.vstack(
        rx.text("Planes"),
        rx.unordered_list(
            rx.foreach(State.planes, lambda item: rx.list.item(rx.text(item))),
        ),
        padding="20px",
        width="50%",
    )