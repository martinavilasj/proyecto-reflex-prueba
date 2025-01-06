import reflex as rx

from proyecto_prueba.components.navbar import navbar
from proyecto_prueba.clientes.clientes import *
from proyecto_prueba.routes import Route

@rx.page(
    route=Route.CLIENTES.value,
    title="Gestion de clientes."
)
def index() -> rx.Component:
    return rx.vstack( 
        navbar(),
        clientes(),
        width="100%"
    )