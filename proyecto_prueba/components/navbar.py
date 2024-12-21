import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Clientes",
            font_size="2em"
        ),
        rx.text(
            "Planes",
            font_size="2em"
        ),
        rx.text(
            "Finanzas",
            font_size="2em"
        ),
        position="sticky",
        bg="grey",
        padding="20px"
        width="100%",
        z_index="3",
    )
