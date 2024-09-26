import mysql.connector
from dotenv import load_dotenv
import os

class DatabaseQuery:
    def __init__(self):
        # Carrega as variáveis do arquivo .env
        load_dotenv()

        # Acessa as variáveis de ambiente
        self.db_user = os.getenv('BD_USER')
        self.db_password = os.getenv('BD_PASSWORD')
        self.db_port = os.getenv('BD_PORT')
        self.db_host = os.getenv('BD_HOST')
        self.db_database = os.getenv('BD_DATABASE')

        # Configurações do banco de dados
        self.config = {
            'host': self.db_host,
            'port': self.db_port,
            'user': self.db_user,
            'password': self.db_password,
            'database': self.db_database
        }

    def select_all_from_usuario(self):
        self.conexao = mysql.connector.connect(**self.config)
        self.cursor = self.conexao.cursor()
        self.cursor.execute('select * from usuario;')  

        registros = self.cursor.fetchall()
        newDict = []
        for registro in registros:
            newDict.append({"id": registro[0],"nome":registro[1]})

        self.cursor.close()
        self.conexao.close()
        return newDict

if __name__ == "__main__":
    db_query = DatabaseQuery()
    db_query.select_all_from_usuario()

