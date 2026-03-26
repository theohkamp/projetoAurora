from app.model.model import SistemaDecolagemModel
from app.view.view import TerminalView


class DecolagemController:
    def __init__(self):
        self.model = SistemaDecolagemModel()
        self.view = TerminalView()

    def iniciar(self):
        dados = self.view.coletar_dados()

        if dados is None:
            self.view.exibir_resultado(False, ["Dados de entrada inválidos (insira números onde solicitado)."])
            return

        lista_erros = self.model.validar_decolagem(dados)

        decolagem_autorizada = len(lista_erros) == 0

        self.view.exibir_resultado(decolagem_autorizada, lista_erros)