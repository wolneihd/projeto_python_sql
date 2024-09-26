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

    def select_all_cars(self):
        self.conexao = mysql.connector.connect(**self.config)
        self.cursor = self.conexao.cursor()
        self.cursor.execute("""
        select  
        	carros.id,
            fabricantes.fabricante,
            cores.cor,
            carros.placa,
            date_format(carros.data_cadastro, '%d/%m/%y') as 'data_cadastro'    
        	    from carros
            INNER JOIN fabricantes ON carros.id_fabricante = fabricantes.id
            INNER JOIN cores ON carros.id_cor = cores.id;
        """)  

        carros = self.cursor.fetchall()
        all_cars = []
        for carro in carros:
            all_cars.append({"id": carro[0], "fabricante": carro[1], "cor": carro[2], "placa": carro[3], "data_cadastro": carro[4]})
            print(all_cars)

        self.cursor.close()
        self.conexao.close()
        return all_cars

if __name__ == "__main__":
    db_query = DatabaseQuery()
    db_query.select_all_cars()

