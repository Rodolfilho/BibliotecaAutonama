from patterns.facade import BibliotecaFacade
from patterns.strategy import AutenticacaoStrategy, AutenticacaoUsuario, AutenticacaoEmail
from patterns.factory import LivroFactory
from patterns.memento import LivroCaretaker
from services import UsuarioService, LivroService
from gateways import UsuarioGateway, LivroGateway


class SistemaBiblioteca:
    def __init__(self):
        user_gateway = UsuarioGateway()
        book_gateway = LivroGateway()
        
        self.facade = BibliotecaFacade(
            auth_strategy=AutenticacaoUsuario(user_gateway),
            user_service=UsuarioService(user_gateway),
            book_service=LivroService(book_gateway),
            book_factory=LivroFactory(),
            caretaker=LivroCaretaker()
        )
        self.usuario_logado = None

    def run(self):
        while True:
            if not self.usuario_logado:
                self.menu_principal()
            else:
                self.menu_usuario()

    def menu_principal(self):
        print("\n--- Sistema de Compartilhamento de Livros ---")
        print("1. Cadastrar")
        print("2. Login")
        print("3. Ver Catálogo")
        print("4. Sair")
        opcao = input("Escolha: ")
        
        if opcao == "1":
            self.cadastrar_usuario()
        elif opcao == "2":
            self.login()
        elif opcao == "3":
            self.ver_catalogo()
        elif opcao == "4":
            exit()

    def menu_usuario(self):
        print(f"\n--- Bem-vindo, {self.usuario_logado} ---")
        print("1. Adicionar Livro")
        print("2. Ver Catálogo")
        print("3. Alugar Livro")
        print("4. Devolver Livro") 
        print("5. Meus Livros")
        print("6. Histórico de Livro")
        print("7. Logout")
        opcao = input("Escolha: ")
        
        if opcao == "1":
            self.adicionar_livro()
        elif opcao == "2":
            self.ver_catalogo()
        elif opcao == "3":
            self.alugar_livro()
        elif opcao == "4": 
            self.devolver_livro()
        elif opcao == "5":
            self.meus_livros()
        elif opcao == "6":
            self.historico_livro()
        elif opcao == "7":
            self.usuario_logado = None


    def run(self):
        while True:
            if not self.usuario_logado:
                self.menu_principal()
            else:
                self.menu_usuario()

    def menu_principal(self):
        print("\n--- Sistema de Compartilhamento de Livros ---")
        print("1. Cadastrar")
        print("2. Login")
        print("3. Ver Catálogo")
        print("4. Sair")
        opcao = input("Escolha: ")
        
        if opcao == "1":
            self.cadastrar_usuario()
        elif opcao == "2":
            self.login()
        elif opcao == "3":
            self.ver_catalogo()
        elif opcao == "4":
            exit()

    def cadastrar_usuario(self):
        username = input("Usuário: ")
        senha = input("Senha: ")
        if self.facade.cadastrar_usuario(username, senha):
            print("Cadastro realizado!")
        else:
            print("Usuário já existe!")

    def login(self):
        username = input("Usuário: ")
        senha = input("Senha: ")
        if self.facade.login(username, senha):
            self.usuario_logado = username
            print("Login realizado!")
        else:
            print("Credenciais inválidas!")

    def adicionar_livro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = input("Ano: ")
        self.facade.adicionar_livro(titulo, autor, ano, self.usuario_logado)
        print("Livro adicionado!")

    def ver_catalogo(self):
        print("\n--- Catálogo Completo ---")
        for livro in self.facade.ver_catalogo():
            meu_livro = "[MEU LIVRO]" if livro['dono'] == self.usuario_logado else ""
            
            status = "Disponível" if livro['disponivel'] == 'True' else f"Alugado por {livro['alugado_por']}"
            print(f"ID: {livro['id']} {meu_livro}")
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Dono: {livro['dono']}")
            print(f"Status: {status}")
            print("-" * 30)

    def alugar_livro(self):
        livro_id = input("ID do livro para alugar: ")
        resultado = self.facade.alugar_livro(livro_id, self.usuario_logado)
        
        if resultado == "sucesso":
            print("Livro alugado com sucesso!")
        elif resultado == "proprio_livro":
            print("Você não pode alugar seu próprio livro!")
        else:
            print("Livro indisponível ou ID inválido!")

    def devolver_livro(self):
        livro_id = input("ID do livro para devolver: ")
        if self.facade.devolver_livro(livro_id, self.usuario_logado):
            print("Livro devolvido com sucesso!")
        else:
            print("Você não alugou este livro ou ID inválido!")

    def meus_livros(self):
        while True:
            print(f"\n--- Meus Livros ({self.usuario_logado}) ---")
            livros = self.facade.meus_livros(self.usuario_logado)
            
            if not livros:
                print("Você ainda não tem livros cadastrados.")
                return
                
            for livro in livros:
                status = "Disponível" if livro['disponivel'] == 'True' else f"Alugado por {livro['alugado_por']}"
                print(f"ID: {livro['id']} | Título: {livro['titulo']} | Status: {status}")
            
            print("\n1. Adicionar mais livros")
            print("2. Excluir livro")
            print("3. Atualizar livro")
            print("4. Voltar")
            opcao = input("Escolha: ")
            
            if opcao == "1":
                self.adicionar_livro()
            elif opcao == "2":
                livro_id = input("ID do livro para excluir: ")
                if self.facade.excluir_livro(livro_id, self.usuario_logado):
                    print("Livro excluído com sucesso!")
                else:
                    print("Erro ao excluir livro. Verifique o ID.")
            elif opcao == "3":
                livro_id = input("ID do livro para atualizar: ")
                novo_titulo = input("Novo título (deixe em branco para manter): ")
                novo_autor = input("Novo autor (deixe em branco para manter): ")
                novo_ano = input("Novo ano (deixe em branco para manter): ")
                
                if self.facade.atualizar_livro(
                    livro_id, 
                    self.usuario_logado,
                    titulo=novo_titulo if novo_titulo else None,
                    autor=novo_autor if novo_autor else None,
                    ano=novo_ano if novo_ano else None
                ):
                    print("Livro atualizado com sucesso!")
                else:
                    print("Erro ao atualizar livro. Verifique o ID.")
            elif opcao == "4":
                return

    def historico_livro(self):
        livro_id = input("ID do livro para ver histórico: ")
        historico = self.facade.ver_historico_livro(livro_id)
        
        if historico:
            print(f"\n--- Histórico do Livro ID: {livro_id} ---")
            for i, estado in enumerate(historico, 1):
                print(f"{i}. {estado}")
        else:
            print("Livro não encontrado ou sem histórico")

    def gerar_qr_code(self):
        num = [random.randint(0, 9) for _ in range(5)]
        return "".join(str(random.randint(0, 9)) for _ in range(5))
