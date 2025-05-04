from app.db import get_connection
import psycopg2

def cadastrar_cardapio(restaurante_id: int, nome: str, valor: float, descricao: str, imagem: bytes, tipo: str):
    """
    Insere um item de cardápio no banco de dados usando SQL puro.
    Dependendo de 'tipo', aponta para a tabela correta:
      - 'prato'     → pratos
      - 'sobremesa' → sobremesas
      - 'bebida'    → bebidas

    Retorna o id inserido em caso de sucesso, ou False em caso de erro.
    """
    # Mapeamento tipo → nome da tabela
    tabelas = {
        'prato': 'pratos',
        'sobremesa': 'sobremesas',
        'bebida': 'bebidas',
    }
    tabela = tabelas.get(tipo.lower())
    if not tabela:
        print(f"[Erro] tipo inválido: {tipo!r}")
        return False

    sql = f"""
        INSERT INTO {tabela} (restaurante_id, nome, valor, descricao, imagem)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id;
    """

    try:
        # O contexto do connection cuidará de commit/rollback automaticamente
        with get_connection() as conn:
            with conn.cursor() as cur:
                # Se 'imagem' for bytes, converte para Binary
                img_param = psycopg2.Binary(imagem) if isinstance(imagem, (bytes, bytearray)) else imagem
                cur.execute(sql, (restaurante_id, nome, valor, descricao, img_param))
                new_id = cur.fetchone()[0]
        return new_id

    except Exception as e:
        print("Erro ao cadastrar item de cardápio:", e)
        return False