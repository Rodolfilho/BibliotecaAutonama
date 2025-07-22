from Models.Armario import Armario, CadastrarArmario
from Models.Livro import Livro
import random


class ArmarioService:
    ListaArmarios = [] 

    def __init__(self):
        pass 

    def GerarID(self):
        Existente = True

        while Existente:
            ID = random.randint(10000, 999999) # Gera um valor aleatório e depois verifica se já existe
            Existente = False

            for armario in ArmarioService.ListaArmarios:
                if armario.Id == ID:
                    Existente = True
                    break
        return ID
    
    def CadastrarArmario(self):
        id = self.GerarID()
        armario = Armario(id)
        ArmarioService.ListaArmarios.append(armario)
        return armario

    def AddArmarioList(self):
        armario = CadastrarArmario(self)
        self.ListaArmarios.append(armario)

    def BuscarArmario(self, id):
        for armario in self.ListaArmarios:
            if armario.Id == id:
                return armario
        return None
    
    def AdicionarLivro(self, IdLivro):
        for armario in self.ListaArmarios:
            if armario.Disponibilidade == "Disponível":
                armario.Livros.append(IdLivro)
                if len(armario.Livros) >= 5:
                    armario.Disponibilidade = "Indisponível"
                return armario.Id
        
        # for armario in self.ListaArmarios:
        #     if armario.dispoinibilidade == "Disponível":
        #         return armario
        #     if armario:
        #         armario.Livros.append(IdLivro)
        #         if len(armario.Livros) >= 5:
        #             armario.Disponibilidade = "Indisponível"
                    
    
    def RemoverLivro(self, id, IdLivro):
        armario = self.BuscarArmario(id)
        if armario:
            if IdLivro in armario.Livros:
                armario.Livros.remove(IdLivro)
                if len(armario.Livros) < 5:
                    armario.Disponibilidade = "Disponível"
            return True
        
        
    