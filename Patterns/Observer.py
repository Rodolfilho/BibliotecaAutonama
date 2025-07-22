# Classe Observer - quem recebe as notificações
class Observer:
    # def update(self, evento, **dados):
    #     raise NotImplementedError("Subclasses devem implementar este método")

    def update(self, evento, **dados):
        usuario = dados['Usuario']
        livro = dados['livro']
        print(f"[EMAIL] Enviando notificação para {usuario.Nome}:")
        print(f"      O livro '{livro.Titulo}' foi {evento}.\n")