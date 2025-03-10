from proyecto_prueba.model.Client import Client as Cliente
from .MySQL import Mysql

MYSQL_API = Mysql()

def hello():
    return "Hola!"

async def planes():
    planes=["Plan premium", "Plan Medio", "Plan Basico"]
    return planes

async def get_clientes() -> list[Cliente]:
    lista_clientes: list[Cliente] = []

    base_response = MYSQL_API.get_clients()

    for cte in base_response:
        cliente = Cliente(id = cte["id"],
                          fecha_ingreso = cte["fecha_ingreso"].strftime('%Y-%m-%d %H:%M:%S'),
                          nombre = cte["nombre"],
                          apellido= cte["apellido"],
                          documento= cte["documento"],
                          plan = cte["plan"],
                          observaciones = cte["observaciones"])
        lista_clientes.append(cliente)

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

def borrar_cliente(id: int):
    base_reponse = MYSQL_API.delete_client(id)

    if base_reponse:
        print(f"Cliente borrado correctamente: ", id)
    else:
        print("ERROR al borrar el cliente")
