from .SupabaseAPI import SupabaseAPI
from proyecto_prueba.model.Client import Client as Cliente
from .MySQL import Mysql

SUPABASE_API = SupabaseAPI()
MYSQL_API = Mysql()

def hello():
    return "Hola!"

async def planes():
    planes=["Plan premium", "Plan Medio", "Plan Basico"]
    return planes

async def get_clientes() -> list:
    lista_clientes = []
    lista: list[Cliente] = MYSQL_API.get_clients()
    for cliente in lista:
        lista_clientes.append(cliente.to_dict())

    return lista_clientes

def insertar_cliente(client_data):
    print(client_data)
    
    cliente = Cliente(nombre = client_data["nombre"],
                      apellido = client_data["apellido"],
                      documento = client_data["documento"],
                      plan = client_data["plan"],
                      observaciones = client_data["observaciones"])
    
    reponse = MYSQL_API.insert_client(cliente)

    if reponse:
        print (f"Cliente ingresado correctamente")
    else:
        print("ERROR: Al ingresar al cliente")
