class Command:
    def executar(self):
        pass

#Funcionalidades mais utilizadas no sistema
class AlugarLivroCommand(Command):
    def __init__(self, book_service, livro_id, locatario):
        self.book_service = book_service
        self.livro_id = livro_id
        self.locatario = locatario

    def executar(self):
        return self.book_service.alugar_livro(self.livro_id, self.locatario)
    
class DevolverLivroCommand(Command):
    def __init__(self, book_service, livro_id, locatario):
        self.book_service = book_service
        self.livro_id = livro_id
        self.locatario = locatario

    def executar(self):
        return self.book_service.devolver_livro(self.livro_id, self.locatario)
