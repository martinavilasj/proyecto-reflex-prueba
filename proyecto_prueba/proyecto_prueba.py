"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

class State(rx.State):
    pass
    
def index() -> rx.Component:
    return rx.center(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Clientes", value="clientes"),
                rx.tabs.trigger("Planes", value="planes"),
                rx.tabs.trigger("Finanzas", value="finanzas"),
            ),
            rx.tabs.content(
                rx.text("Acá van los clientes xd"),
                rx.accordion.root(
                    rx.accordion.item(
                        header="Nuevo cliente",
                        content="Acá se agregaria un cliente",
                        ),
                    collapsible=True,
                    width=300px,
                    type="single",
                    variant="soft",
                ),
                value="clientes",
            ),
            rx.tabs.content(
                rx.text("Acá van los planes xd"),
                value="planes",
            ),
            rx.tabs.content(
                rx.text("Acá van las finanzas xd"),
                value="finanzas",
            ),
        )
    )

app = rx.App()
app.add_page(index)