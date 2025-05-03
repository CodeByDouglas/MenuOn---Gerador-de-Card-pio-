from flask import Blueprint, request, jsonify
from app.sevices.cadastrar_user import cadastrar_user as cadastrar_service

cadastrar_user = Blueprint('cadastrar_user', __name__)

@cadastrar_user.route('/cadastrar-user', methods=['POST'])
def cadastrar_user_endpoint():
    data = request.get_json() or {}
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')

    result = cadastrar_service(nome, email, senha)
    if result is not False:
        return jsonify({"user_id": result}), 200
    else:
        return jsonify({"error": "não foi possível cadastrar esse usuário"}), 404