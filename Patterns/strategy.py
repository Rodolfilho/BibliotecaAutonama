from abc import ABC, abstractmethod

class AutenticacaoStrategy(ABC):
    @abstractmethod
    def autenticar(self, username, senha):
        pass

class AutenticacaoTXT(AutenticacaoStrategy):
    def __init__(self, user_gateway):  # ADICIONAR ESTE CONSTRUTOR
        self.user_gateway = user_gateway
        
    def autenticar(self, username, senha):
        usuario = self.user_gateway.buscar_por_username(username)
        if usuario and usuario['senha'] == senha:
            return True
        return False