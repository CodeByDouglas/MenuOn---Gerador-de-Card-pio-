import qrcode
from io import BytesIO
from app.db import get_connection

def gerar_qrcode(url: str, restaurante_id: int):
    """
    Gera um QR Code a partir da URL fornecida e atualiza o campo 'qr_code'
    na tabela 'restaurantes' para o restaurante com o ID especificado.
    
    Retorna True se a operação for bem sucedida; caso contrário, retorna False.
    """
    try:
        # Gera o QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Salva a imagem em um buffer de memória
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        qr_code_binary = buffer.read()
        
        # Atualiza o banco de dados com o QR Code gerado
        with get_connection() as conn:
            with conn.cursor() as cursor:
                update_query = """
                    UPDATE restaurantes
                    SET qr_code = %s
                    WHERE id = %s;
                """
                cursor.execute(update_query, (qr_code_binary, restaurante_id))
            conn.commit()
        return True
    except Exception as e:
        print("Erro ao gerar QR Code:", e)
        return False

