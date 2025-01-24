import reflex as rx 
import proyecto_prueba.api.api as api
from proyecto_prueba.model.Client import Client
from proyecto_prueba.routes import Route

class State(rx.State):
    form_data: dict = {}
    planes: list
    clientes: list[Client]
    # Variable para evitar realizar consulta nuevamente a la base
    clientes_todos: list[Client]
    usuario_borrar: int = -1


    async def obtener_planes(self):
        self.planes = await api.planes()
    
    async def obtener_clientes(self):
        self.clientes = await api.get_clientes()
        self.clientes_todos = self.clientes
    
    @rx.event
    async def insertar_cliente(self, form_data: dict):
        api.insertar_cliente(form_data)
        await self.obtener_clientes()
    
    @rx.event
    def buscar_cliente(self,texto_buscar):
        self.clientes = self.clientes_todos
        if texto_buscar:
            resultado = [
                obj for obj in self.clientes
                if any(texto_buscar.lower() in str(getattr(obj, prop, "")).lower() for prop in vars(obj))
            ]
            self.clientes = resultado

    @rx.event
    async def borrar_cliente(self, id):
        api.borrar_cliente(id)
        await self.obtener_clientes()
