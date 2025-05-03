import psycopg2
from flask import current_app

def get_connection():
    cfg = current_app.config
    return psycopg2.connect(
        host=cfg['DB_HOST'],
        port=cfg['DB_PORT'],
        dbname=cfg['DB_NAME'],
        user=cfg['DB_USER'],
        password=cfg['DB_PASSWORD']
    )
