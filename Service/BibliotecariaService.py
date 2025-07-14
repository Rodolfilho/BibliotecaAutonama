from Models.Bibliotecaria import Bibliotecaria

class BibliotecariaService:
    def __init__(self):
        self.bibliotecarias = [] 

    def BuscarBibliotecaria(self, CPF):
        for Bibliotecaria in self.bibliotecarias:
            if Bibliotecaria.CPF == CPF:
                return Bibliotecaria
        return None

    def AutenticarBibliotecaria(self, CPF, senha):
        Bibliotecaria = self.BuscarBibliotecaria(CPF)
        if Bibliotecaria and Bibliotecaria.Senha == senha:
            return True
        return False
