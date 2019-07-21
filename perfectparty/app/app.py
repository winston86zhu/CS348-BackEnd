from flask import Flask
from flask_restful import Api
from flask_cors import CORS

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)

    CORS(app)

    from extensions import DatabaseConnection
    DatabaseConnection('host=db port=5432 dbname=postgres user=postgres password=')

    from modules import init_api
    init_api(api)

    app.run(host='0.0.0.0', port=5000, debug=True)

