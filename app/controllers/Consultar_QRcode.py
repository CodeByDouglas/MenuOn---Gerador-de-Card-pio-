from flask import Blueprint, request, jsonify
from app.services.def_consultar_QRcode import consultar_qrcode

consultar_qrcode_bp = Blueprint('consultar_qrcode', __name__)

@consultar_qrcode_bp.route('/consultar-qrcode', methods=['POST'])
def consultar_qrcode_endpoint():
    data = request.get_json() or {}
    restaurante_id = data.get('restaurante_id')
    if restaurante_id is None:
        return jsonify({"error": "O campo restaurante_id é obrigatório."}), 400
    try:
        restaurante_id = int(restaurante_id)
    except ValueError:
        return jsonify({"error": "restaurante_id inválido."}), 400
    
    qr_code = consultar_qrcode(restaurante_id)
    
    if qr_code is None:
        return jsonify({"error": "QR Code não encontrado."}), 404
    
    return jsonify({"qr_code": qr_code}), 200