"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from proyecto_prueba.pages.clientes import index
from proyecto_prueba.pages.finanzas import finanzas
from proyecto_prueba.pages.planes import planes

class State(rx.State):
    pass


app = rx.App()
#app.add_page(index, finanzas)