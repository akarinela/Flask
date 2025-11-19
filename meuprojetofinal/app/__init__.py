from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Configura os caminhos
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DB_PATH = os.path.join(PROJECT_ROOT, 'meubanco.db')

# 1. Cria a aplicação Flask
app = Flask(__name__, template_folder='templates')

# 2. Configura o Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Inicializa o Banco
db = SQLAlchemy(app)