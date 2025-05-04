from flask import Blueprint, request, jsonify
from app.services.def_autenticar_user import autenticar_user

logar_user = Blueprint('logar_user', __name__)

@logar_user.route('/autencar-user', methods=['POST'])
def login_user():
    """
    Endpoint para autenticação de usuário.
    Recebe um JSON com 'email' e 'senha' e retorna o ID do usuário autenticado
    ou uma mensagem de erro.
    """
    data = request.get_json() or {}
    email = data.get('email')
    senha = data.get('senha')
    
    if not email or not senha:
        return jsonify({"error": "Email e senha são obrigatórios"}), 400

    result = autenticar_user(email, senha)
    if result is False:
        return jsonify({"error": "informações de login inválidas"}), 401
    else:
        _, user_id = result
        return jsonify({"user_id": user_id}), 200