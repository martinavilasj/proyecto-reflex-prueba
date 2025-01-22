import reflex as rx
from proyecto_prueba.state.PageState import State

def form_nuevo_cliente() -> rx.Component:
    return rx.vstack( 
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Nombre",
                    name="nombre",
                    required=True,
                ),
                rx.input(
                    placeholder="Apellido",
                    name="apellido",
                    required=True,
                ),
                rx.input(
                    placeholder="Documento",
                    name="documento",
                    required=True,
                ),
                rx.hstack(
                    rx.text("Plan:"),
                    rx.select(
                        ["Basic", "Medium", "Premium"],
                        default_value="Basic",
                        name="plan",
                        required=True,
                    ),
                ),
                rx.text_area(
                    placeholder="Observaciones",
                    name="observaciones",
                    required=False,
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=State.insertar_cliente,
            reset_on_submit=True,
        ),
        width="100%",
        padding="10px",
    ),