class Subject:
    def __init__(self):
        self._observers = []

    def adicionar_observer(self, observer):
        self._observers.append(observer)

    def notificar(self, livro, locatario):
        for observer in self._observers:
            observer.atualizar(livro, locatario)

class LivroObserver:
    def atualizar(self, livro, locatario):
        print(f"\n[NOTIFICAÇÃO] Livro '{livro['titulo']}' alugado por {locatario}")