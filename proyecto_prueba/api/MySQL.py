import os, dotenv
import mysql.connector as mysql 

from proyecto_prueba.model.Client import Client as Cliente

class Mysql:
    
    dotenv.load_dotenv()

    database: str = os.environ.get("MYSQL_DATABASE")
    db_host:str = os.environ.get("MYSQL_HOST")
    db_user:str = os.environ.get("MYSQL_USER")
    db_pass:str = os.environ.get("MYSQL_PASS")

    mydb = mysql.connect(
        host = db_host,
        user = db_user,
        password = db_pass
    )

    conn = mydb.cursor()
    
    def get_connection(self):
        return self.mydb
    
    def create_database(self, db_name) -> bool:
        try:
            self.conn.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            return True
        except:
            return False
    
    def show_databases(self):
        self.conn.execute("SHOW DATABASES")

        for db in self.conn:
            print(db)

    def select_all_from(self, table_name) -> list:
        self.conn.execute(f"SELECT * FROM {self.database}.{table_name}")
        result = self.conn.fetchall()

        return result
    
    def get_clients(self) -> dict:

        cursor = self.mydb.cursor(dictionary=True)

        cursor.execute(f"SELECT * FROM {self.database}.clientes")
        result = cursor.fetchall()
        
        return result
    
    def insert_client(self, data:Cliente) -> bool:
        try:
            sql = f"INSERT INTO {self.database}.clientes (nombre, apellido, documento, plan, observaciones) VALUES (%s, %s, %s, %s, %s)"
            val = (data.nombre, data.apellido, data.documento, data.plan, data.observaciones)

            self.conn.execute(sql, val)

            self.mydb.commit()
            
            return True
        except ValueError as err:
            print(err)
            return False

        print(self.conn.rowcount, "was inserted")
    
    def delete_client(self, id:int) -> bool:
        try:
            self.conn.execute(f"DELETE FROM {self.database}.clientes WHERE id = {id}")
            
            self.mydb.commit()

            return True
        
        except ValueError as err:
            print(err)
            return False