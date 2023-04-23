# application/orcamento_api/routes.py
from . import orcamento_api_blueprint
from .. import db
from ..models import Orcamento
from .implementations import ServicoOrcamento
from flask import make_response, request, jsonify


@orcamento_api_blueprint.route('/api/orcamentos', methods=['GET'])
def listarOrcamentos():
    orcamentos = ServicoOrcamento.listarOrcamentos()

    response = jsonify({'results': orcamentos})
    return response


@orcamento_api_blueprint.route('/api/orcamento/create', methods=['POST'])
def CriarOrcamento():
    orcamento = Orcamento()
    orcamento.nome = request.form['nome']
    orcamento.mes = request.form['mes']
    orcamento.valor_maximo = request.form['valor_maximo']

    orcamento = ServicoOrcamento.criarOrcamento(orcamento)

    response = jsonify({'message': 'Orcamento added',
                       'result': orcamento.to_json()})
    return response
