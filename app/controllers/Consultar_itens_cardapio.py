from flask import Blueprint, request, jsonify
from app.sevices.consultar_itens_cardapio import consultar_itens_cardapio as consultar_service

consultar_itens_cardapio_bp = Blueprint('consultar_itens_cardapio', __name__)

@consultar_itens_cardapio_bp.route('/consultar-itens-cardapio', methods=['GET'])
def consultar_itens_cardapio_endpoint():
    restaurante_id_txt = request.args.get('restaurante_id')
    if not restaurante_id_txt:
        return jsonify({'error': 'restaurante_id não fornecido'}), 400
        
    try:
        restaurante_id = int(restaurante_id_txt)
    except ValueError:
        return jsonify({'error': 'restaurante_id deve ser um inteiro válido'}), 400

    result = consultar_service(restaurante_id)
    if result is not False:
        return jsonify(result), 200
    else:
        return jsonify({'error': 'não foi possível localizar os itens do cardápio'}), 404