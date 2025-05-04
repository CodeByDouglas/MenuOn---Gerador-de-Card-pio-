from flask import Blueprint, request, jsonify
from app.services.def_cadastrar_cardapio import cadastrar_cardapio as cadastrar_cardapio_service
import psycopg2

cadastrar_cardapio = Blueprint('cadastrar_cardapio', __name__)

@cadastrar_cardapio.route('/cadastrar-cardapio', methods=['POST'])
def cadastrar_cardapio_endpoint():
    """
    Endpoint para cadastro de um item do cardápio.
    
    Espera um formulário (form-data) com os campos:
      - restaurante_id: ID do restaurante (obrigatório)
      - nome: Nome do item
      - valor: Valor do item
      - tipo: Tipo do item (prato, sobremesa ou bebida)
      - descricao: Descrição do item
      - imagem: Arquivo de imagem (obrigatório)

    Retorna um JSON com o 'id' do item cadastrado em caso de sucesso (status 200) ou
    uma mensagem de erro em caso de falha (status 400).
    """
    # 1) Extrai dados do form-data
    restaurante_id = request.form.get('restaurante_id')
    nome = request.form.get('nome')
    valor = request.form.get('valor')
    tipo = request.form.get('tipo')
    descricao = request.form.get('descricao')
    
    # Validação de campos obrigatórios
    if not restaurante_id or not nome or not valor or not tipo:
        return jsonify({'error': 'Campos obrigatórios não informados'}), 400

    # 2) Pega o arquivo de imagem
    arquivo = request.files.get('imagem')
    if not arquivo:
        return jsonify({'error': 'Nenhuma imagem enviada'}), 400
    img_bytes = arquivo.read()

    try:
        restaurante_id_int = int(restaurante_id)
        valor_float = float(valor)
    except ValueError:
        return jsonify({'error': 'restaurante_id e valor devem ser numéricos'}), 400

    # 3) Chama o service passando os dados
    new_id = cadastrar_cardapio_service(
        restaurante_id=restaurante_id_int,
        nome=nome,
        valor=valor_float,
        descricao=descricao,
        imagem=psycopg2.Binary(img_bytes),  # converte para BYTEA
        tipo=tipo
    )

    if new_id:
        return jsonify({'id': new_id}), 200
    else:
        return jsonify({'error': 'não foi possível cadastrar o item'}), 400