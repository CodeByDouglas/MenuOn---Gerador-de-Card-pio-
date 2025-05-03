from flask import Blueprint, request, jsonify
from app.sevices.autenticar_user import autenticar_user as autenticar_service

logar_user = Blueprint('logar_user', __name__)

@logar_user.route('/autencar-user', methods=['POST'])
def autenticar_user():
    data = request.get_json() or {}
    email = data.get('email')
    senha = data.get('senha')
    
    result = autenticar_service(email, senha)
    if result is False:
        return jsonify({"error": "informações de login invalidas"}), 401
    else:
        _, user_id = result
        return jsonify({"user_id": user_id}), 200