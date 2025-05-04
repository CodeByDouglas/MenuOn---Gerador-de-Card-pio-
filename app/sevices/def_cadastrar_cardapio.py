from app.db import get_connection
import psycopg2

def cadastrar_cardapio(restaurante_id: int, nome: str, valor: float, descricao: str, imagem: bytes, tipo: str):
    """
    Insere um item de cardápio no banco de dados.
    
    Dependendo de 'tipo', insere o registro na tabela correspondente:
      - 'prato'     → pratos
      - 'sobremesa' → sobremesas
      - 'bebida'    → bebidas

    Retorna o id do item inserido em caso de sucesso; caso contrário, retorna False.
    """
    # Mapeia o tipo para a tabela correta
    tabelas = {
        'prato': 'pratos',
        'sobremesa': 'sobremesas',
        'bebida': 'bebidas',
    }
    tabela = tabelas.get(tipo.lower())
    if not tabela:
        print(f"[Erro] Tipo inválido: {tipo!r}")
        return False

    sql = f"""
        INSERT INTO {tabela} (restaurante_id, nome, valor, descricao, imagem)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                # Converte imagem para Binary se necessário
                img_param = psycopg2.Binary(imagem) if isinstance(imagem, (bytes, bytearray)) else imagem
                cursor.execute(sql, (restaurante_id, nome, valor, descricao, img_param))
                new_id = cursor.fetchone()[0]
        return new_id

    except Exception as e:
        print("Erro ao cadastrar item de cardápio:", e)
        return False