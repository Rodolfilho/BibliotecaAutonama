class Livro:
    def __init__(self,Id, Titulo, Autor, Genero, IdAluno, Status="Disponível", Armario=None):
        self.Id = Id
        self.Titulo = Titulo
        self.Autor = Autor
        self.Genero = Genero
        self.IdAluno = IdAluno
        self.Status = Status
        self.Armario = Armario

        self.Observers = []  # Lista de observadores

    def AddObserver(self, obervers):  #Adiciona um observador ao livro
        self.Observers.append(obervers)

    def Notify(self, evento, **dados):  #Notifica os observadores com os dados do evento
        for observer in self.Observers:
            observer.update(evento, **dados)


