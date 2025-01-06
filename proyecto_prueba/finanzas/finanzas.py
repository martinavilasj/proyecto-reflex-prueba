import reflex as rx

def finanzas_page() -> rx.Component:
    return rx.vstack(
        rx.text("Finanzas"),
        padding="20px",
        width="50%",
    )