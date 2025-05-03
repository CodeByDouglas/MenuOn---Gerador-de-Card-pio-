from flask import Blueprint, request, jsonify
import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv
import os

load_dotenv()
# Renomeie a blueprint para "criar_tabelas"
criar_tabelas = Blueprint('criar_tabelas', __name__)

# Configuração do pool de conexões utilizando variáveis de ambiente
try:
    db_pool = psycopg2.pool.SimpleConnectionPool(
        minconn=1,
        maxconn=10,
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432'),
        database=os.getenv('POSTGRES_DB')
    )
except Exception as e:
    print("Erro ao criar o pool de conexões:", e)

@criar_tabelas.route('/criar-tabelas', methods=['POST'])
def create_tables():
    comandos = [
        """CREATE TABLE IF NOT EXISTS restaurantes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(150) UNIQUE NOT NULL,
            senha VARCHAR(255) NOT NULL,
            qr_code TEXT,
            link TEXT
        );""",
        """CREATE TABLE IF NOT EXISTS pratos (
            id SERIAL PRIMARY KEY,
            restaurante_id INTEGER NOT NULL
                REFERENCES restaurantes(id)
                ON DELETE CASCADE,
            nome VARCHAR(100) NOT NULL,
            valor NUMERIC(10,2) NOT NULL,
            descricao TEXT,
            imagem BYTEA
        );""",
        """CREATE TABLE IF NOT EXISTS bebidas (
            id SERIAL PRIMARY KEY,
            restaurante_id INTEGER NOT NULL
                REFERENCES restaurantes(id)
                ON DELETE CASCADE,
            nome VARCHAR(100) NOT NULL,
            valor NUMERIC(10,2) NOT NULL,
            descricao TEXT,
            imagem BYTEA
        );""",
        """CREATE TABLE IF NOT EXISTS sobremesas (
            id SERIAL PRIMARY KEY,
            restaurante_id INTEGER NOT NULL
                REFERENCES restaurantes(id)
                ON DELETE CASCADE,
            nome VARCHAR(100) NOT NULL,
            valor NUMERIC(10,2) NOT NULL,
            descricao TEXT,
            imagem BYTEA
        );"""
    ]

    conn = None
    try:
        conn = db_pool.getconn()
        cursor = conn.cursor()
        for comando in comandos:
            cursor.execute(comando)
        conn.commit()
        cursor.close()
        return jsonify({"message": "Tabelas criadas com sucesso."}), 201
    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            db_pool.putconn(conn)