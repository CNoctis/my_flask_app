from flask_restful import Api
from flask import Flask
from flask_cors import CORS
from app.routes import create_routers


app = Flask(__name__)

CORS(app)

api = Api(app)

create_routers(api)