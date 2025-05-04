from flask import Blueprint, request, jsonify
from app.services.def_consultar_itens_cardapio import consultar_itens_cardapio as consultar_service

# Renomeando o blueprint para deixar explícito que é a rota de consulta de itens do cardápio
consultar_itens_cardapio = Blueprint('consultar_itens_cardapio', __name__)

@consultar_itens_cardapio.route('/consultar-itens-cardapio', methods=['GET'])
def consultar_itens_cardapio_endpoint():
    """
    Endpoint para consulta dos itens do cardápio de um restaurante.
    
    Parâmetros (via query string):
        - restaurante_id: ID do restaurante (esperado em formato numérico)

    Retorna:
        - JSON com os itens (pratos, sobremesas e bebidas) em caso de sucesso (status 200)
        - JSON com mensagem de erro em caso de falha ou parâmetros inválidos (status 400 ou 404)
    """
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