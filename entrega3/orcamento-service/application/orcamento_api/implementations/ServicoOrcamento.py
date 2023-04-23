from ..interfaces.IServicoOrcamento import IServicoOrcamento
from ...models import Orcamento
from ... import db


class ServicoOrcamento(IServicoOrcamento):
    @staticmethod
    def listarOrcamentos():
        orcamentos = []
        for row in Orcamento.query.all():
            orcamentos.append(row.to_json())

        return orcamentos

    @staticmethod
    def criarOrcamento(orcamento):
        orcamento_db = Orcamento.query.get(orcamento.id)

        if orcamento_db is not None:
            return None

        db.session.add(orcamento)
        db.session.commit()

        return orcamento
