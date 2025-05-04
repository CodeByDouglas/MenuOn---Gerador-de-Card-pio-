from flask import Blueprint, render_template, request, jsonify

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