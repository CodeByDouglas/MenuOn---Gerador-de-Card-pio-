from flask import Blueprint, request, jsonify
from app.sevices.def_cadastrar_cardapio import cadastrar_cardapio as cadastrar_cardapio_service
import psycopg2

cadastrar_cardapio = Blueprint('cadastrar_cardapio', __name__)

@cadastrar_cardapio.route('/cadastrar-cardapio', methods=['POST'])
def cadastrar_cardapio_endpoint():
    # 1) Pega campos de texto do form-data
    restaurante_id = request.form.get('restaurante_id')
    nome           = request.form.get('nome')
    valor          = request.form.get('valor')
    tipo           = request.form.get('tipo')
    descricao      = request.form.get('descricao')

    # 2) Pega o arquivo de imagem
    arquivo = request.files.get('imagem')
    if not arquivo:
        return jsonify({'error': 'Nenhuma imagem enviada'}), 400
    img_bytes = arquivo.read()

    # 3) Chama o service passando os dados
    new_id = cadastrar_cardapio_service(
        restaurante_id=int(restaurante_id),
        nome=nome,
        valor=float(valor),
        descricao=descricao,
        imagem=psycopg2.Binary(img_bytes),  # já converte para BYTEA
        tipo=tipo
    )

    if new_id:
        return jsonify({'id': new_id}), 200
    else:
        return jsonify({'error': 'não foi possível cadastrar o item'}), 400