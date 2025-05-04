from flask import Flask
from dotenv import load_dotenv
import os
from .controllers.Criar_Tabelas import criar_tabelas
from .controllers.Logar_user import logar_user
from .controllers.Cadastrar_user import cadastrar_user
from .controllers.Cadastrar_cardapio import cadastrar_cardapio
from .controllers.Consultar_itens_cardapio import consultar_itens_cardapio
from .controllers.Consultar_QRcode import consultar_qrcode_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    # Carrega configurações via .flaskenv/.env
    app.config.from_prefixed_env()  # auto-processa FLASK_*, SECRET_KEY etc.
    
    # Registra blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(criar_tabelas)
    app.register_blueprint(logar_user)
    app.register_blueprint(cadastrar_user)
    app.register_blueprint(cadastrar_cardapio)
    app.register_blueprint(consultar_itens_cardapio)
    app.register_blueprint(consultar_qrcode_bp)

    # Utiliza as variáveis corretas definidas em .env para a conexão com o banco
    app.config['DB_HOST']            = os.getenv('DB_HOST', 'localhost')
    app.config['DB_PORT']            = os.getenv('DB_PORT', '5432')
    app.config['POSTGRES_DB']        = os.getenv('POSTGRES_DB')
    app.config['POSTGRES_USER']      = os.getenv('POSTGRES_USER')
    app.config['POSTGRES_PASSWORD']  = os.getenv('POSTGRES_PASSWORD')
    
    return app