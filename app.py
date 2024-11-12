import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Cargar variables de entorno antes de utilizarlas
load_dotenv()
CORS (app)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
ma = Marshmallow(app)

# Mueve la importación de los modelos aquí para evitar importaciones circulares
from models import Equipo, Modelo, Categoria, User
from views.register import register_bp
from routes import *
from models import Lista_Categoria
from schemas import Lista_CategoriaSchema


register_bp(app)
