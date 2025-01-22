import reflex as rx 
import proyecto_prueba.api.api as api
import proyecto_prueba.model.Client as Client

class State(rx.State):
    planes: list
    clientes: list
    columnas: list[str] = ["ID","Fecha ingreso","Nombre","Apellido","Documento","Plan","Observaciones"]


    async def obtener_planes(self):
        self.planes = await api.planes()
    
    async def obtener_clientes(self):
        self.clientes = await api.get_clientes()
