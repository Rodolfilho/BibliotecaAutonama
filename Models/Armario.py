import random
from Service.ArmarioService import ArmarioService
from Patterns.Prototype import Prototype 



class Armario(Prototype):
    def __init__(self, id=None, IdLivros=None,disponibilidade="Disponível"):
        self.Id = id
        self.Livros = []
        self.Disponibilidade = disponibilidade
            
