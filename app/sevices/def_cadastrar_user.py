from app.db import get_connection

def cadastrar_user(nome: str, email: str, senha: str):
    """
    Insere um novo restaurante no banco de dados com os dados fornecidos.
    Retorna o id do restaurante cadastrado em caso de sucesso ou False em caso de falha.
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO restaurantes (nome, email, senha)
            VALUES (%s, %s, %s)
            RETURNING id;
        """
        cursor.execute(query, (nome, email, senha))
        new_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        return new_id
    except Exception as e:
        print("Erro ao cadastrar usuário:", e)
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            conn.close()