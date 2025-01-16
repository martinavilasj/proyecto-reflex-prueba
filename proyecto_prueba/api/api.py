from .SupabaseAPI import SupabaseAPI

SUPABASE_API = SupabaseAPI()

def hello():
    return "Hola!"

async def planes():
    planes=["Plan premium", "Plan Medio", "Plan Basico"]
    return planes

async def get_clientes() -> list:
    return SUPABASE_API.get_clients()