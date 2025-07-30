class LivroMemento:
    def __init__(self, estado):
        self.estado = estado
        self.data = self._obter_data_hora()
    
    def _obter_data_hora(self):
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y %H:%M")
    
    def __str__(self):
        return f"[{self.data}] {self.estado}"

class LivroCaretaker:
    def __init__(self):
        self.historico = {}
    
    def adicionar_memento(self, livro_id, estado):
        if livro_id not in self.historico:
            self.historico[livro_id] = []
        self.historico[livro_id].append(LivroMemento(estado))
    
    def obter_historico(self, livro_id):
        return self.historico.get(livro_id, [])