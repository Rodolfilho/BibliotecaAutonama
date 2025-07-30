class LivroFactory:
    @staticmethod
    def criar_livro(titulo, autor, ano, dono):
        return {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "dono": dono,
            "disponivel": "True",
            "alugado_por": ""
        }