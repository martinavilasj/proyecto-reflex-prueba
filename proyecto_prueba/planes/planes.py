import reflex as rx

def planes_page() -> rx.Component:
    return rx.vstack(
        rx.text("Planes"),
        padding="20px",
        width="50%",
    )