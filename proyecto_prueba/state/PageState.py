import reflex as rx 
import proyecto_prueba.api.api as api
import proyecto_prueba.model.Client as Client
from proyecto_prueba.routes import Route

class State(rx.State):
    form_data: dict = {}
    planes: list
    clientes: list
    columnas: list[str] = ["ID","Fecha ingreso","Nombre","Apellido","Documento","Plan","Observaciones"]


    async def obtener_planes(self):
        self.planes = await api.planes()
    
    async def obtener_clientes(self):
        self.clientes = await api.get_clientes()
    
    @rx.event
    async def insertar_cliente(self, form_data: dict):
        api.insertar_cliente(form_data)
        # no estaria funcionando
        rx.redirect(Route.CLIENTES.value)


