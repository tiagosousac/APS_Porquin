# application/gasto_api/routes.py
from . import gasto_api_blueprint
from .. import db
from ..models import Gasto
from flask import jsonify, request
from .implementations import ServicoGasto


@gasto_api_blueprint.route('/api/gastos', methods=['GET'])
def listarGastos():
    gastos = ServicoGasto.listarGastos()

    response = jsonify({'results': gastos})
    return response


@gasto_api_blueprint.route('/api/gastos/filter', methods=['GET'])
def filtrarGastos():
    orcamento_id = request.args.get('orcamento_id', None)
    categoria_id = request.args.get('categoria_id', None)
    data_inicio = request.args.get('data_inicio', None)
    data_fim = request.args.get('data_fim', None)

    gastos = ServicoGasto.filtrarGastos(
        orcamento_id, categoria_id, data_inicio, data_fim)

    response = jsonify({'results': gastos})
    return response


@gasto_api_blueprint.route('/api/gasto/create', methods=['POST'])
def cadastrarGasto():
    gasto = Gasto()
    gasto.orcamento_id = request.form['orcamento_id']
    # gasto.categoria_id = request.form['categoria_id']
    gasto.categoria_id = 1
    gasto.nome = request.form['nome']
    gasto.valor = request.form['valor']
    gasto.descricao = request.form['descricao']
    gasto.data_ocorrida = request.form['data_ocorrida']

    gasto = ServicoGasto.cadastrarGasto(gasto)

    if (gasto is None):
        abort(404)

    response = jsonify({'message': 'Gasto added', 'gasto': gasto.to_json()})
    return response


@gasto_api_blueprint.route('/api/gasto/sincronizar', methods=['POST'])
def sincronizarGastos():
    usuario_cpf = request.form['usuario_cpf']
    data_inicio = request.form['data_inicio']
    data_fim = request.form['data_fim']

    response = ServicoGasto.sincronizarGastos(
        usuario_cpf, data_inicio, data_fim)

    if response is None:
        abort(404)

    response = jsonify({'message': 'Gastos sincronizados'})
    return response


@gasto_api_blueprint.route('/api/gasto/<int:id>', methods=['DELETE'])
def removerGasto(id):
    gasto = ServicoGasto.removerGasto(id)

    if gasto is None:
        abort(404)

    return jsonify({'result': True})


@gasto_api_blueprint.route('/api/gasto/<int:id>', methods=['PUT'])
def editarGasto(id):
    if not request.json:
        abort(400)

    categoria_id = request.form['categoria_id']
    orcamento_id = request.form['orcamento_id']
    nome = request.form['nome']
    valor = request.form['valor']
    descricao = request.form['descricao']
    data_ocorrida = request.form['data_ocorrida']

    gasto = ServicoGasto.editarGasto(
        id, categoria_id, orcamento_id, nome, valor, descricao, data_ocorrida)

    if gasto is None:
        abort(404)

    return jsonify(gasto.to_json())
