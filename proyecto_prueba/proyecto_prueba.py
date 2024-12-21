"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from proyecto_prueba.components.navbar import navbar
from proyecto_prueba.clientes.formulario import *

from rxconfig import config

class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.vstack( 
        navbar(),
        form_nuevo_cliente(),
        width="100%"
    )
app = rx.App()
app.add_page(index)