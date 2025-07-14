from datetime import datetime

class QrCode:
    def __init__(self, Id, Aluno, Livro, Status, Prazo=14):
        self.Id = Id
        self.Aluno = Aluno
        self.Livro = Livro
        self.Data = datetime.now()
        self.Status = Status
        self.Prazo = Prazo

        