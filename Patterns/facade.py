from patterns.observer import Subject, LivroObserver
from patterns.command import AlugarLivroCommand

class BibliotecaFacade:
    def __init__(self, auth_strategy, user_service, book_service, book_factory, caretaker):
        self.auth_strategy = auth_strategy
        self.user_service = user_service
        self.book_service = book_service
        self.book_factory = book_factory
        self.caretaker = caretaker
        self.notificador = Subject()

    def cadastrar_usuario(self, username, senha):
        return self.user_service.cadastrar(username, senha)

    def login(self, username, senha):
        return self.auth_strategy.autenticar(username, senha)

    def adicionar_livro(self, titulo, autor, ano, dono):
        livro = self.book_factory.criar_livro(titulo, autor, ano, dono)
        livro_id = self.book_service.adicionar_livro(livro)
        self.caretaker.adicionar_memento(livro_id, f"Livro adicionado por {dono}")

        #ADD adicionar oberservador(proprietario)
        self.notificador.adicionar_observer(LivroObserver(livro['dono']))
        return livro_id

    def ver_catalogo(self):
        return self.book_service.listar_todos()

    def meus_livros(self, dono):
        return self.book_service.listar_por_dono(dono)

    def alugar_livro(self, livro_id, locatario):
        livro = self.book_service.buscar_por_id(livro_id)
        
        if livro and livro['dono'] == locatario:
            return "proprio_livro"
            
        command = AlugarLivroCommand(self.book_service, livro_id, locatario)
        if command.executar():
            if livro:
                self.caretaker.adicionar_memento(
                    livro_id, 
                    f"Alugado por {locatario} (de: {livro['dono']})"
                )
                ##print("Observers registrados:", self.notificador._observers)
                self.notificador.notificar(livro, locatario) #ADD notificar o dono apenas o observador
            return "sucesso"
        return "erro"
    
    def devolver_livro(self, livro_id, locatario):
        livro = self.book_service.buscar_por_id(livro_id)
        if livro and livro.get('alugado_por') == locatario:

            livro['disponivel'] = True   # Corrigido para boolean
            livro['alugado_por'] = ''

            if self.book_service.atualizar_livro(livro_id, **livro):
                self.caretaker.adicionar_memento(
                    livro_id, 
                    f"Devolvido por {locatario} para {livro.get('dono', 'desconhecido')}"
                )
                self.notificador.notificar(livro, locatario)
                return True
        return False
    
    def ver_historico_livro(self, livro_id):
        return self.caretaker.obter_historico(livro_id)
    
    def excluir_livro(self, livro_id, dono):
        livro = self.book_service.buscar_por_id(livro_id)
        if livro and livro['dono'] == dono:
            if self.book_service.excluir_livro(livro_id):
                self.caretaker.adicionar_memento(livro_id, f"Livro excluído por {dono}")
                return True
        return False
    
    def atualizar_livro(self, livro_id, dono, **dados):
        livro = self.book_service.buscar_por_id(livro_id)
        if livro and livro['dono'] == dono:
            if self.book_service.atualizar_livro(livro_id, **dados):
                # Registrar alterações no histórico
                alteracoes = []
                for campo, valor in dados.items():
                        alteracoes.append(f"{campo} alterado para {valor}")
                
                if alteracoes:
                    self.caretaker.adicionar_memento(
                        livro_id, 
                        f"Atualizado por {dono}: {', '.join(alteracoes)}"
                    )
                return True
        return False