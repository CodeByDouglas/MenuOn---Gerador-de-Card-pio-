from flask import Blueprint, render_template, request, jsonify, abort
import requests

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/login')
def login():
    return render_template('login.html')

@main_bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@main_bp.route('/login/registrar-cardapio')
def registrar_cardapio():
    return render_template('registrar.cardapio.html')

@main_bp.route('/login/cardapio')
def cardapio():
    return render_template('cardapio.html')

@main_bp.route('/cardapio/<int:restaurante_id>')
def cardapio_view(restaurante_id):
    # Constrói a URL do endpoint /consultar-itens-cardapio
    endpoint_url = f"{request.host_url.rstrip('/')}/consultar-itens-cardapio"
    params = {'restaurante_id': restaurante_id}
    
    # Faz a requisição GET ao endpoint
    response = requests.get(endpoint_url, params=params)
    
    # Se o status não for OK, aborta com 404.
    if response.status_code != 200:
        abort(404, description="Cardápio não encontrado")
    
    # Decodifica a resposta JSON
    result = response.json()
    
    # Renderiza o template com os dados retornados
    return render_template(
        'cardapio_restaurante.html',
        restaurante_id=restaurante_id,
        pratos=result.get('pratos', []),
        bebidas=result.get('bebidas', []),
        sobremesas=result.get('sobremesas', [])
    )
