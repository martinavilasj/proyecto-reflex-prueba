"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from proyecto_prueba.pages.clientes import index
from proyecto_prueba.pages.finanzas import finanzas
from proyecto_prueba.pages.planes import planes

import proyecto_prueba.api.api as api

class State(rx.State):
    pass


app = rx.App()
#app.add_page(index, finanzas)

app.api.add_api_route("/hello", api.hello)