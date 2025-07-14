from Models.Livro import Livro

class LivrosService:
    def __init__(self):
        self.Livros = [] #Lista com os livros armazenados

    def CadastrarLivro(self, livro):
        self.Livros.append(livro)

    def ListarLivros(self):
        return self.Livros
    
    def BuscarLivro(self, titulo):
        resultados = []

        for livro in self.Livros:
            if titulo.lower() in livro.Titulo.lower():
                resultados.append(livro)
        return resultados
    
    def LivroEmprestado (self, codigo):
        for Livro in self.Livros:
            if Livro.Id == codigo:
                if Livro and Livro.Status == "Disponível":
                    Livro.Status = "Emprestado"
                    return True
        return False
        
    def LivroDevolvido (self, codigo):
        for Livro in self.Livros:
            if Livro.Id == codigo:
                if Livro and Livro.Status == "Emprestado":
                    Livro.Status = "Disponível"
                    return True
        return False
        
    