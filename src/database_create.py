import mysql.connector
from dotenv import load_dotenv
import os

class DatabaseManager:
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
            'password': self.db_password
        }

        # Obtém o caminho do arquivo SQL
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'script_database.sql'))
        print(f"caminho do arquivo: {self.file_path}")

        # Lê o conteúdo do arquivo SQL
        self.sql_file = self.read_sql_file()

        # Cores para impressão no console
        self.fonte_vermelho = "\033[31m"
        self.fonte_verde = "\033[32m"
        self.fonte_reset = "\033[0m"

    def read_sql_file(self):
        try:
            with open(self.file_path, 'r') as fd:
                return fd.read()
        except FileNotFoundError:
            print(f"{self.fonte_vermelho}Arquivo não encontrado: {self.file_path}{self.fonte_reset}")
            return ""

    def run_sql_script(self):
        if not self.sql_file:
            print(f"{self.fonte_vermelho}Nenhum comando SQL para executar.{self.fonte_reset}")
            return

        try:
            conexao = mysql.connector.connect(**self.config)
            cursor = conexao.cursor()

            # Executa o script SQL
            commands = self.sql_file.split(';')  # Supondo que os comandos estão separados por ponto e vírgula
            for command in commands:
                if command.strip():  # Ignora comandos vazios
                    cursor.execute(command)

            conexao.commit()  # Confirma as mudanças no banco de dados
            print(f"Script SQL executado com sucesso:")
            print(f"{self.fonte_verde}{self.sql_file}{self.fonte_reset}")

        except mysql.connector.Error as err:
            print(f"{self.fonte_vermelho}Erro: {err}{self.fonte_reset}")
        finally:
            cursor.close()
            conexao.close()

if __name__ == "__main__":
    db_manager = DatabaseManager()
    db_manager.run_sql_script()
