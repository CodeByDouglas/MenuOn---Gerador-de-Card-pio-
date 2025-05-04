import base64
from app.db import get_connection

def consultar_itens_cardapio(restaurante_id: int):
    if not isinstance(restaurante_id, int):
        print(f"[Erro] ID inválido: {restaurante_id!r}")
        return False

    result = {"pratos": [], "sobremesas": [], "bebidas": []}
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                for key, qry in {
                    "pratos":    "SELECT id, nome, descricao, valor, imagem FROM pratos WHERE restaurante_id = %s;",
                    "sobremesas":"SELECT id, nome, descricao, valor, imagem FROM sobremesas WHERE restaurante_id = %s;",
                    "bebidas":   "SELECT id, nome, descricao, valor, imagem FROM bebidas WHERE restaurante_id = %s;",
                }.items():
                    cur.execute(qry, (restaurante_id,))
                    rows = cur.fetchall()
                    items = []
                    for id_, nome, desc, val, img in rows:
                        # Convert image bytes (memoryview) to base64 string if available
                        if img is not None:
                            img = base64.b64encode(bytes(img)).decode('utf-8')
                        items.append({
                            "id": id_,
                            "nome": nome,
                            "descricao": desc,
                            "valor": float(val) if val is not None else None,
                            "imagem": img
                        })
                    result[key] = items

        return result

    except Exception as e:
        print("Erro ao consultar itens do cardápio:", e)
        return False