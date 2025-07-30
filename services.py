class UsuarioService:
    def __init__(self, gateway):
        self.gateway = gateway
        
    def cadastrar(self, username, senha):
        if self.gateway.buscar_por_username(username):
            return False
        self.gateway.salvar(username, senha)
        return True
        
    #def autenticar(self, username, senha):
        #usuario = self.gateway.buscar_por_username(username)
        #return usuario and usuario['senha'] == senha
    
class LivroService:
    def __init__(self, gateway):
        self.gateway = gateway
        
    def adicionar_livro(self, livro):
        return self.gateway.salvar(livro)
    
    def listar_todos(self):
        return self.gateway.listar_todos()
    
    def listar_por_dono(self, dono):
        return [livro for livro in self.gateway.listar_todos() if livro['dono'] == dono]
    
    def buscar_por_id(self, livro_id):
        return self.gateway.buscar_por_id(livro_id)
    
    def alugar_livro(self, livro_id, locatario):
        livro = self.gateway.buscar_por_id(livro_id)
        if livro and livro['disponivel'] == 'True':
            livro['disponivel'] = 'False'
            livro['alugado_por'] = locatario
            return self.gateway.atualizar(livro)
        return False
    
    # NOVO: Excluir livro
    def excluir_livro(self, livro_id):
        return self.gateway.excluir(livro_id)
    
    # NOVO: Atualizar livro
    def atualizar_livro(self, livro_id, **dados):
        livro = self.gateway.buscar_por_id(livro_id)
        if livro:
            # Atualizar apenas os campos fornecidos
            for campo, valor in dados.items():
                if valor is not None:  # Ignorar campos não fornecidos
                    livro[campo] = valor
            return self.gateway.atualizar(livro)
        return False

    def devolver_livro(self, livro_id, locatario):
        livro = self.gateway.buscar_por_id(livro_id)
        if livro and livro['alugado_por'] == locatario:
            livro['disponivel'] = 'True'
            livro['alugado_por'] = ''
            return self.gateway.atualizar(livro)
        return False