import base64
from app.db import get_connection

def consultar_qrcode(restaurante_id: int):
    """
    Consulta o campo 'qr_code' da tabela 'restaurantes' para o restaurante com o ID fornecido
    e retorna o QR Code em formato base64.
    
    Retorna:
      - Uma string com o QR Code codificado em base64 se encontrado.
      - None, caso o QR Code não seja encontrado ou ocorra algum erro.
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT qr_code FROM restaurantes WHERE id = %s;", (restaurante_id,))
                result = cursor.fetchone()
        
        if result is None or result[0] is None:
            return None
        
        qr_code_binary = result[0]
        qr_code_base64 = base64.b64encode(qr_code_binary).decode('utf-8')
        return qr_code_base64
    except Exception as e:
        print("Erro ao consultar QR Code:", e)
        return None