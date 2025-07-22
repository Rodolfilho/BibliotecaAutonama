from Models.QrCode import QrCode
from Models.Alerta import Alerta
from Models.Bibliotecaria import Bibliotecaria
from datetime import datetime
import random

class QrCodeService:
    def __init__(self,bibliotecarias, alerta_service):
        self.alerta_service = alerta_service    # Armazena o serviço de alerta para registrar alertas
        self.bibliotecarias = bibliotecarias    #Puxa a lista de bibliotecárias do serviço
        self.qrcodes = [] 

    def GerarID(self):
        Existente = True

        while Existente:
            ID = random.randint(10000, 999999) # Gera um valor aleatório e depois verifica se já existe
            Existente = False

            for QrCode in self.qrcodes:
                if QrCode.Id == ID:
                    Existente = True
                    break
        return ID

    def RegistrarQrCode(self, Aluno, Livro): #Gera o QR Code para o empréstimo e gera o id
        Id = self.GerarID()
        QrCode = QrCode(Id, Aluno, Livro, "Emprestado")
        self.qrcodes.append(QrCode)
        return QrCode
    
    def RegistrarDevolucao(self, Id): #Registra a devolução do Livro e verifica se o prazo foi excedido
        for qr in self.qrcodes:
            if qr.Id == Id and qr.Status == "Emprestado":
                qr.Status = "Disponível"

                dias = (datetime.now() - qr.Data).days
                if dias > qr.Prazo:             # Casao seja devolvido com atraso, gera um alerta
                    for biblio in self.bibliotecarias:
                        self.alerta_service.RegistrarAlerta(biblio.nome, descricao= f"{qr.Aluno.nome} excedeu o prazo de devolução do livro {qr.Livro.Titulo}", data=datetime.now())
                return True
        return False
    
    def BuscarQrCode(self, Id):
        for qr in self.qrcodes:
            if qr.Id == Id:
                return qr
        return None