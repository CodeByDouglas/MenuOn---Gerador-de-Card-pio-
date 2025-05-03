from flask import Flask
from dotenv import load_dotenv
import os
from .controllers.Criar_Tabelas import criar_tabelas

load_dotenv()

def create_app():
    app = Flask(__name__)
    # Carrega configurações via .flaskenv/.env
    app.config.from_prefixed_env()  # auto-processa FLASK_*, SECRET_KEY etc.
    
    # Registra blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(criar_tabelas)

    
    app.config['DB_HOST']     = os.getenv('DB_HOST')
    app.config['DB_NAME']     = os.getenv('DB_NAME')
    app.config['DB_PORT']     = os.getenv('DB_PORT')
    app.config['DB_USER']     = os.getenv('DB_USER')
    app.config['DB_PASSWORD'] = os.getenv('DB_PASSWORD')
    return app