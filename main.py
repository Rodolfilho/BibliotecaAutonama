from Service.LivrosService import *
from Service.ArmarioService import *
from Service.AlunoService import *
from Models.Livro import Livro
from Models.Usuario import Aluno
aluno_service = AlunoService()
livro_service = LivrosService()

def TelaInicial():

    lista_alunos = carregar_alunos_arquivo("alunos.txt")

    for aluno in lista_alunos:
        print(f"ID: {aluno.CPF}, Nome: {aluno.Nome}, Matrícula: {aluno.Matricula}, senha: {aluno.Senha}")



    while True:
        print("\n===== Sistema da Biblioteca =====")
        print("1 - Sou Aluno")
        print("2 - Sou Bibliotecário")
        print("0 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            matricula = LoginAluno()
        # elif opc == "2":
        #     LoginBibliotecario()
        elif opc == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def LoginAluno():
    while True:
        print("\n===== Login Aluno =====")
        matricula = input("Digite sua matrícula: ")
        senha = input("Digite sua senha: ")


        if aluno_service.autenticar_aluno(matricula, senha):
            print("Login realizado com sucesso!")
            MenuAluno(aluno_service.buscar_aluno_por_matricula(matricula))
            return matricula
        else:
            print("Matrícula ou senha inválidos. Tente novamente.")
            MenuAluno(aluno_service.buscar_aluno_por_matricula(matricula))

def MenuAluno(aluno):
    while True:
        print("\n===== Munu Aluno =====")
        print("1 - Gerenciar Livros")
        print("2 - Registrar Alerta")
        print("3 - Ver Catalogo")
        print("0 - Sair") 

        opc = input("Escolha uma opção: ")
        if opc == "1":
            GerenciarLivrosAluno(aluno)
        # elif opc == "2":
        #     RegistrarAlerta(aluno)
        # elif opc == "3":
        #     VerCatalogo()
        elif opc == "0":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")   

        def GerenciarLivrosAluno(aluno):
            print("\n===== Gerenciar Livros =====")
            print("1 - Cadastrar Livro")
            print("2 - Remover Livro")
            print("0 - Sair") 

            opc = input("Escolha uma opção: ")
            if opc == "1":
                titulo = input("Digite o titulo do livro: ")
                autor = input("Digite o autor do livro: ")
                Genero = input("Digite o gênero do livro: ")
                IdAluno = aluno.matricula
                livro = Livro(None, titulo, autor, Genero, IdAluno)
                livro_service.CadastrarLivro(livro)
                print("Livro cadastrado com sucesso!")
            elif opc == "2":
                print("Lista de livros:")
                for livro in livro_service.ListarLivros():
                    print(f"{livro.Id} - {livro.Titulo} por {livro.Autor}")

                titulo = input("Digite o título do livro que deseja remover: ")
                livro_service.RemoverLivro(titulo)


def carregar_alunos_arquivo(caminho):
    alunos = []
    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(";")
            if len(partes) == 4:
                id = int(partes[0])
                nome = partes[1]
                matricula = partes[2]
                senha = (partes[3])
                aluno = Aluno(id, nome, matricula, senha)
                alunos.append(aluno)
    return alunos       

if __name__ == "__main__":
    TelaInicial()

