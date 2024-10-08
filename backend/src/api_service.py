from flask import Flask, jsonify
from flask_cors import CORS
import src.database_queries as database_query

class App:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.setup_routes()
        self.dbquery = database_query.DatabaseQuery()

    def setup_routes(self):
        @self.app.route('/', methods=['GET'])
        def get_all_users():
            # resultado = self.dbquery.select_all_from_usuario()
            return jsonify(self.dbquery.select_all_cars())
        
        @self.app.route('/cores', methods=['GET'])
        def get_all_colors():
            resultado = self.dbquery.buscarTodasCores()
            return jsonify(resultado)

    def run(self):
        self.app.run(port=5000, host='localhost', debug=True)

if __name__ == '__main__':
    app = App()
    app.run()
