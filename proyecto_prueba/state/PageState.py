import reflex as rx 
import proyecto_prueba.api.api as api

class State(rx.State):
    planes: list
    clientes: list


    async def obtener_planes(self):
        self.planes = await api.planes()
    
    async def obtener_clientes(self):
        self.clientes = await api.get_clientes()
