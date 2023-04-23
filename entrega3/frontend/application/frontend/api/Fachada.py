import requests
from flask import request

from ..interfaces.IFachada import IFachada

from .ControleGasto import ControleGasto
from .ControleOrcamento import ControleOrcamento


class Fachada(IFachada):
    @staticmethod
    def get_gastos():
        return ControleGasto.listar_gastos()

    @staticmethod
    def post_gasto(gasto):
        return ControleGasto.cadastrar_gasto(gasto)

    @staticmethod
    def sync_gastos(info):
        return ControleGasto.sincronizar_gastos(info)

    @staticmethod
    def create_orcamento(form):
        return ControleOrcamento.criar_orcamento(form)

    @staticmethod
    def get_orcamentos():
        return ControleOrcamento.listar_orcamentos()
