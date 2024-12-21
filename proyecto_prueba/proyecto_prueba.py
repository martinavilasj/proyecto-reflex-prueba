"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

class State(rx.State):
    pass

def prueba():
    rx.text("Hola Reflex", color="red")
    rx.button("Click me.", color_scheme="grass", variant="soft")

def index() -> rx.Component:
    return prueba()

app = rx.App()
app.add_page(index)