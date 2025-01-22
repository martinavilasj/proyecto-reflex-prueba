import os
import dotenv
from supabase import create_client, Client
import proyecto_prueba.model.Client as Cliente

class SupabaseAPI:
    
    dotenv.load_dotenv()

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url,key)



    def get_clients(self) -> list[Cliente]:

        response = self.supabase.table("clientes").select("*").execute()

        lista_clientes = []

        if len(response.data) > 0:
            for cte in response.data:
                cliente = Cliente.Client(id = cte["id"],
                                         fecha_ingreso = cte["created_at"],
                                         nombre = cte["nombre"],
                                         apellido= cte["apellido"],
                                         documento= cte["documento"],
                                         plan = cte["plan"],
                                         observaciones = cte["observaciones"])
                
                lista_clientes.append(cliente)
     
        return lista_clientes
