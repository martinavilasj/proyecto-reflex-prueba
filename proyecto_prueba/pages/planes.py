import reflex as rx

from proyecto_prueba.components.navbar import navbar
from proyecto_prueba.planes.planes import *
from proyecto_prueba.routes import Route

@rx.page(
    route=Route.PLANES.value,
    title="Planes"
)

def planes() -> rx.Component:
    return rx.vstack( 
        navbar(),
        planes_page(),
        width="100%"
    )