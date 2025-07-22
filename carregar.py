from Models.Usuario import Aluno

def carregar_alunos_arquivo(caminho_arquivo):
    alunos = []
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                id, nome, matricula, senha = linha.strip().split(";")
                aluno = Aluno(id, nome, matricula, senha)
                alunos.append(aluno)
    except FileNotFoundError:
        print("Arquivo de alunos não encontrado.")
    return alunos
