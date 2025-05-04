from app.db import get_connection

def cadastrar_user(nome: str, email: str, senha: str):
    """
    Insere um novo restaurante no banco de dados com os dados fornecidos.
    
    Retorna:
      - id do restaurante cadastrado em caso de sucesso;
      - False em caso de falha.
    """
    query = """
        INSERT INTO restaurantes (nome, email, senha)
        VALUES (%s, %s, %s)
        RETURNING id;
    """
    
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (nome, email, senha))
                new_id = cursor.fetchone()[0]
            conn.commit()
        return new_id

    except Exception as e:
        print("Erro ao cadastrar usuário:", e)
        return False