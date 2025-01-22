from .SupabaseAPI import SupabaseAPI
import proyecto_prueba.model.Client as Cliente

SUPABASE_API = SupabaseAPI()

def hello():
    return "Hola!"

async def planes():
    planes=["Plan premium", "Plan Medio", "Plan Basico"]
    return planes

async def get_clientes() -> list:
    lista_clientes = []
    lista: list[Cliente] = SUPABASE_API.get_clients()
    for cliente in lista:
        lista_clientes.append(cliente.to_dict())

    return lista_clientes