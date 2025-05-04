from app.db import get_connection

def autenticar_user(email: str, senha: str):
    """
    Busca no banco de dados um restaurante com o e-mail informado e compara a senha.
    
    Retorna:
      - (True, id) se a senha for igual à armazenada;
      - False caso o restaurante não seja encontrado ou a senha não corresponda.
    """
    try:
        # Usa o context manager para obter a conexão e o cursor,
        # garantindo o fechamento automático dos recursos
        with get_connection() as conn:
            with conn.cursor() as cursor:
                query = "SELECT id, senha FROM restaurantes WHERE email = %s;"
                cursor.execute(query, (email,))
                result = cursor.fetchone()
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