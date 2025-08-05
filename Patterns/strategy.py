from abc import ABC, abstractmethod

class AutenticacaoStrategy(ABC): #Define a estrutura das classes de autenticação
    @abstractmethod
    def autenticar(self, identificador, senha):
        pass

#Herda os parametros para buscar o usuario e vefificar a senha 
class AutenticacaoUsuario(AutenticacaoStrategy): 
    def __init__(self, user_gateway):  
        self.user_gateway = user_gateway
        
    def autenticar(self, username, senha):
        usuario = self.user_gateway.buscar_por_username(username)
        if usuario and usuario['senha'] == senha:
            return True
        return False
    
class AutenticacaoEmail(AutenticacaoStrategy):
    def __init__(self, user_gateway):
        self.user_gateway = user_gateway

    def autenticar(self, email, senha):
        usuario = self.user_gateway.buscar_por_email(email)
        return usuario and usuario['senha'] == senha