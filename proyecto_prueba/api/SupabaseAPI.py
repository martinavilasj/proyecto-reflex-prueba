import os
import dotenv
from supabase import create_client, Client

class SupabaseAPI:
    
    dotenv.load_dotenv()

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url,key)



    def get_clients(self) -> list:

        response = self.supabase.table("clientes").select("*").execute()

        clientes = []

        if len(response.data) > 0:
            for cliente in response.data:
                clientes.append(cliente)
     
        return clientes
