from Models.Usuario import Aluno

class AlunoService:
    Alunos = [] 

    def __init__(self):
        pass 

    def cadastrar_aluno(self, aluno):
        self.Alunos.append(aluno)

    def listar_alunos(self):
        return self.Alunos
    
    def buscar_aluno_por_matricula(self, matricula):
        for aluno in self.Alunos:
            if aluno.Matricula == matricula:
                return aluno
        return None

    def autenticar_aluno(self, matricula, senha):
        aluno = self.buscar_aluno_por_matricula(matricula)
        if aluno and aluno.Senha == senha:
            return True
        return False

    