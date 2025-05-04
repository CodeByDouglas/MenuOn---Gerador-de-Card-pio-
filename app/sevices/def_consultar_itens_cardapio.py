import base64
from app.db import get_connection

# Dicionário com as queries, para facilitar a manutenção
QUERIES = {
    "pratos":    "SELECT id, nome, descricao, valor, imagem FROM pratos WHERE restaurante_id = %s;",
    "sobremesas": "SELECT id, nome, descricao, valor, imagem FROM sobremesas WHERE restaurante_id = %s;",
    "bebidas":   "SELECT id, nome, descricao, valor, imagem FROM bebidas WHERE restaurante_id = %s;",
}

def convert_imagem_to_base64(imagem):
    """Converte a imagem para string codificada em base64, se disponível."""
    if imagem is not None:
        return base64.b64encode(bytes(imagem)).decode('utf-8')
    return None

def consultar_itens_cardapio(restaurante_id: int):
    try:
        restaurante_id_int = int(restaurante_id)
    except (ValueError, TypeError):
        print(f"[Erro] ID inválido: {restaurante_id!r}")
        return False

    resultado = {"pratos": [], "sobremesas": [], "bebidas": []}
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                for categoria, consulta in QUERIES.items():
                    cur.execute(consulta, (restaurante_id_int,))
                    rows = cur.fetchall()
                    itens = []
                    for id_item, nome, descricao, valor, imagem in rows:
                        itens.append({
                            "id": id_item,
                            "nome": nome,
                            "descricao": descricao,
                            "valor": float(valor) if valor is not None else None,
                            "imagem": convert_imagem_to_base64(imagem)
                        })
                    resultado[categoria] = itens
        return resultado

    except Exception as e:
        print("Erro ao consultar itens do cardápio:", e)
        return False