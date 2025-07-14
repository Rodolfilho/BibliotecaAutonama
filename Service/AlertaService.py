from Models.Alerta import Alerta
import random

class AlertaService:
    def __init__(self):
        self.alertas = []

    def GerarProtocolo(self):
        Existente = True

        while Existente:
            protocolo = random.randint(10000, 999999) # Gera um valor aleatório e depois verifica se já existe
            Existente = False

            for alerta in self.alertas:
                if alerta.Protocolo == protocolo:
                    Existente = True
                    break
        return protocolo

    def RegistrarAlerta(self, usuario, descricao, data):
        protocolo = self.GerarProtocolo()
        alerta = Alerta(protocolo, usuario, descricao, data)
        self.alertas.append(alerta)
        return alerta
    
    def AlertasUsuario(self, usuario):
        AlertasUsuario = []
        for alerta in self.alertas:
            if alerta.Usuario == usuario:
                AlertasUsuario.append(alerta)
        return AlertasUsuario