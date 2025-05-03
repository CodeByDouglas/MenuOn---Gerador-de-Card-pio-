from flask import Flask

def create_app():
    app = Flask(__name__)
    # Carrega configurações via .flaskenv/.env
    app.config.from_prefixed_env()  # auto-processa FLASK_*, SECRET_KEY etc.
    
    # Registra blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app