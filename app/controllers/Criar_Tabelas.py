from flask import Blueprint, jsonify
from dotenv import load_dotenv
from app.db import get_connection

load_dotenv()
criar_tabelas = Blueprint('criar_tabelas', __name__)

@criar_tabelas.route('/criar-tabelas', methods=['POST'])
def create_tables():
    """
    Endpoint para criação das tabelas necessárias no banco de dados.
    
    Executa comandos SQL para criar as tabelas:
      - restaurantes
      - pratos
      - bebidas
      - sobremesas
      
    Cada tabela é criada apenas se não existir.
    
    Retorna:
      - HTTP 201 com mensagem de sucesso se todas as tabelas forem criadas;
      - HTTP 500 com mensagem de erro caso ocorra alguma exceção.
    """
    comandos = [
        """CREATE TABLE IF NOT EXISTS restaurantes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(150) UNIQUE NOT NULL,
            senha VARCHAR(255) NOT NULL,
            qr_code BYTEA,
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

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                # Executa cada comando SQL da lista
                for comando in comandos:
                    cursor.execute(comando)
            conn.commit()
        return jsonify({"message": "Tabelas criadas com sucesso."}), 201

    except Exception as e:
        # Em caso de erro, a exceção é capturada e enviada no retorno
        return jsonify({"error": str(e)}), 500