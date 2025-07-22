import copy 

class Prototype:
    def clone(self):
        return copy.deepcopy(self) #Copia o ojbeto inteiro, incluindo atributos internos