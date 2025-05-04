from app.db import get_connection

def autenticar_user(email: str, senha: str):
    """
    Busca no banco de dados um restaurante com o e-mail informado e compara a senha.
    Caso a senha seja igual, retorna (True, id do restaurante), caso contrário retorna False.
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT id, senha FROM restaurantes WHERE email = %s;"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()

        if result is None:
            return False

        restaurant_id, senha_salva = result
        if senha == senha_salva:
            return True, restaurant_id
        else:
            return False
    except Exception as e:
        print("Erro ao autenticar usuário:", e)
        return False
    finally:
        if conn:
            conn.close()