class Subject:
    def __init__(self):
        self._observers = []

    def adicionar_observer(self, observer):
        self._observers.append(observer)

    def remover_observer(self, observer):
        self._observers.remove(observer)

    def notificar(self, livro, locatario):
        for observer in self._observers:
            observer.atualizar(livro, locatario)

class LivroObserver:
    def __init__(self,dono): ##ADD guarda o dono do livro como observer
        self.dono = dono

    def atualizar(self, livro, locatario):
        if livro['dono'] == self.dono:
            print(f"\n[NOTIFICAÇÃO para {self.dono}] Livro '{livro['titulo']}' alugado por {locatario}")    #simula a notificao que o proprietario (observador) receberia por email