import psycopg2
from flask import current_app

def get_connection():
    cfg = current_app.config
    return psycopg2.connect(
        host=cfg.get('DB_HOST', 'localhost'),
        port=cfg.get('DB_PORT', '5432'),
        dbname=cfg['POSTGRES_DB'],
        user=cfg['POSTGRES_USER'],
        password=cfg['POSTGRES_PASSWORD']
    )