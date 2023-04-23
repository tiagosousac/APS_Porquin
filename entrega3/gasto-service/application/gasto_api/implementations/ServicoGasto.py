from ..interfaces.IServicoGasto import IServicoGasto
from ...models import Gasto
from ... import db
import requests
from dateutil import parser


class ServicoGasto(IServicoGasto):
    @staticmethod
    def listarGastos():
        gastos = []

        for gasto in Gasto.query.all():
            gastos.append(gasto.to_json())

        return gastos

    @staticmethod
    def filtrarGastos(orcamento_id, categoria_id, data_inicio, data_fim):

        gastos = []
        gasto_query = Gasto.query

        if orcamento_id is not None:
            gasto_query = gasto_query.filter(
                Gasto.orcamento_id == orcamento_id)

        if categoria_id is not None:
            gasto_query = gasto_query.filter(
                Gasto.categoria_id == categoria_id)

        if data_inicio is not None:
            gasto_query = gasto_query.filter(
                Gasto.data_ocorrida >= data_inicio)

        if data_fim is not None:
            gasto_query = gasto_query.filter(Gasto.data_ocorrida <= data_fim)

        for row in gasto_query.all():
            gastos.append(row.to_json())

        return gastos

    @staticmethod
    def cadastrarGasto(gasto):
        gasto_db = Gasto.query.get(gasto.id)

        if gasto_db is not None:
            return None

        db.session.add(gasto)
        db.session.commit()

        return gasto

    @staticmethod
    def sincronizarGastos(usuario_cpf, data_inicio, data_fim):
        url = 'https://6434029c582420e231716b14.mockapi.io/api/gastos'
        response = requests.get(url)

        if response is None:
            return None

        gastos_inserir = []

        gastos = response.json()
        for gasto in gastos:
            novo_gasto = Gasto()
            novo_gasto.orcamento_id = 1
            novo_gasto.categoria_id = 1
            novo_gasto.nome = gasto['nome']
            novo_gasto.valor = gasto['valor']
            novo_gasto.descricao = gasto['descricao']
            novo_gasto.data_ocorrida = parser.parse(gasto['data'])

            gastos_inserir.append(novo_gasto)

        db.session.add_all(gastos_inserir)
        db.session.commit()

        return gastos

    @staticmethod
    def removerGasto(gasto_id):
        gasto_db = Gasto.query.get(gasto_id)

        if gasto_db is None:
            return None

        db.session.delete(gasto_db)
        db.session.commit()

        return gasto_db

    @staticmethod
    def editarGasto(gasto_id, orcamento_id, categoria_id, nome, valor, descricao, data_ocorrida):
        gasto = Gasto.query.get(id)
        if gasto is None:
            return None

        gasto.orcamento_id = orcamento_id
        gasto.categoria_id = categoria_id
        gasto.nome = nome
        gasto.valor = valor
        gasto.descricao = descricao
        gasto.data_ocorrida = data_ocorrida

        db.session.commit()

        return gasto
