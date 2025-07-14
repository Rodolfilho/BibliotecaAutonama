from Models.Usuario import Aluno

class AlunoService:
    def __init__(self):
        self.alunos = [] # Lista para armazenar os alunos

    def cadastrar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        return self.alunos
    
    def buscar_aluno_por_matricula(self, matricula):
        for aluno in self.alunos:
            if aluno.Matricula == matricula:
                return aluno
        return None

    def autenticar_aluno(self, matricula, senha):
        aluno = self.buscar_aluno_por_matricula(matricula)
        if aluno and aluno.Senha == senha:
            return True
        return False

    