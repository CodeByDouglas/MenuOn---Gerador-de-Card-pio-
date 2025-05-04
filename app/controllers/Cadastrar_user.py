from flask import Blueprint, request, jsonify
from app.services.def_cadastrar_user import cadastrar_user as cadastrar_service
from app.services.def_gerar_QRcode import gerar_qrcode

cadastrar_user = Blueprint('cadastrar_user', __name__)

@cadastrar_user.route('/cadastrar-user', methods=['POST'])
def cadastrar_user_endpoint():
    """
    Endpoint para cadastro de um novo restaurante.
    
    Espera um JSON com os campos:
      - nome: Nome do restaurante
      - email: Email do restaurante
      - senha: Senha de acesso

    Retorna um JSON com o 'user_id' em caso de sucesso (status 200) ou com uma mensagem
    de erro (status 400 ou 404) se não for possível efetuar o cadastro.
    """
    # Extrai os dados do corpo da requisição
    data = request.get_json() or {}
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')
    
    # Validação dos parâmetros obrigatórios
    if not all([nome, email, senha]):
        return jsonify({"error": "Os campos nome, email e senha são obrigatórios"}), 400
    
    # Chama a função de cadastro no serviço
    result = cadastrar_service(nome, email, senha)
    
    if result is not False:
        # Gera o QR Code usando a URL construída com o ID do restaurante/cadastrado
        url = f"https://zany-space-computing-machine-7vrr9w7rv59whp6qv-5000.app.github.dev/cardapio/{result}"
        gerar_qrcode(url, result)
        return jsonify({"user_id": result}), 200
    else:
        return jsonify({"error": "não foi possível cadastrar esse usuário"}), 404