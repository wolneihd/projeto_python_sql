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
            return jsonify(self.dbquery.select_all_from_usuario())

    def run(self):
        self.app.run(port=5000, host='localhost', debug=True)

if __name__ == '__main__':
    app = App()
    app.run()
