from flask import Blueprint, render_template, request, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return '👋 Olá, Flask está rodando!'

@main_bp.route('/echo', methods=['POST'])
def echo():
    data = request.get_json() or {}
    return jsonify({'você_enviou': data})
