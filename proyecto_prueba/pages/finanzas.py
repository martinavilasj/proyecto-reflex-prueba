import reflex as rx

from proyecto_prueba.components.navbar import navbar
from proyecto_prueba.finanzas.finanzas import *
from proyecto_prueba.routes import Route

@rx.page(
    route=Route.FINANZAS.value,
    title="Finanzas"
)

def finanzas() -> rx.Component:
    return rx.vstack( 
        navbar(),
        finanzas_page(),
        width="100%"
    )