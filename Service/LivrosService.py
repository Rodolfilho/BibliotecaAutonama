from Models.Livro import Livro
from Service.ArmarioService import AdicionarLivro, RemoverLivro
import random
from Patterns.Observer import Observer
from AlunoService import AlunoService

class LivrosService:
    def __init__(self):
        self.Livros = [] #Lista com os livros armazenados

    def CadastrarLivro(self, livro):
        id = self.GerarId()
        livro.Id = id
        AdicionarLivro(id)
        self.Livros.append(livro)

    def RemoverLivro(self, Titulo):
        for livro in self.Livros:
            if livro.Titulo == Titulo:
                self.Livros.remove(livro)
                RemoverLivro(livro.Armario, livro.Id)
                print(f"Livro {Titulo} removido com sucesso!")
                return True
            else:
                print(f"Livro {Titulo} não encontrado.")

    def ListarLivros(self):
        return self.Livros
    
    def BuscarLivro(self, titulo):
        resultados = []

        for livro in self.Livros:
            if titulo.lower() in livro.Titulo.lower():
                resultados.append(livro)
        return resultados
    
    def LivroEmprestado (self, codigo, Usuarios): #Passsar a lista de usuarios presente no ServiceUSuario
        for livro in self.Livros:
            if livro.Id == codigo:
                if livro and livro.Status == "Disponível":
                    livro.Status = "Emprestado" 

                    for aluno in Usuarios:
                        if aluno.Matricula == livro.IdAluno:
                            livro.AddOberserver(aluno)
                            livro.notify("emprestado", livro=livro, usuario=aluno)
                    return True
        return False
        
    def LivroDevolvido (self, codigo,Usuarios):
        for livro in self.Livros:
            if livro.Id == codigo:
                if livro.Status == "Emprestado":
                    livro.Status = "Disponível"
                    
                    for aluno in Usuarios:
                        if aluno.Matricula == livro.IdAluno:
                            livro.AddOberserver(aluno)
                            livro.notify("emprestado", livro=livro, usuario=aluno)                    
                    return True
        return False
    

    def GerarId(self):
        Existente = True

        while Existente:
            ID = random.randint(10000, 999999) # Gera um valor aleatório e depois verifica se já existe
            Existente = False

            for livro in self.Livros:
                if livro.Id == ID:
                    Existente = True
                    break
        return ID
        