class IServicoGasto:
    @staticmethod
    def listarGastos():
        pass

    @staticmethod
    def filtrarGastos(orcamento_id, categoria_id, data_inicio, data_fim):
        pass

    @staticmethod
    def cadastrarGasto(gasto):
        pass

    @staticmethod
    def sincronizarGastos(usuario_cpf, data_inicio, data_fim):
        pass

    @staticmethod
    def removerGasto(gasto_id):
        pass

    @staticmethod
    def editarGasto(gasto_id, orcamento_id, categoria_id, nome, valor, descricao, data_ocorrida):
        pass
