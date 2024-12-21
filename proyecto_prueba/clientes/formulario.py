import reflex as rx

class FormState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data

def form_nuevo_cliente() -> rx.Component:
    return rx.center( 
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
                rx.flex(
                    rx.text("Plan:"),
                    rx.select(
                        ["Basic", "Medium", "Premium"],
                        default_value="Basic",
                        name="planes",
                        required=True,
                    ),
                ),
                rx.input(
                    placeholder="Observaciones",
                    name="observaciones",
                    required=False,
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
        width="50%",
    ),