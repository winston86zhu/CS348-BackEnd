from flask import Flask
from flask_restful import Api

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)

    from modules import init_api
    init_api(api)

    app.run(host='0.0.0.0', port=5000)
