from entita.utente import Utente

class Cliente(Utente):
    def __init__(self, id_cliente, nome, cognome, tel, email, passw, nome_azienda, pIva, indirizzo):
        Utente.__init__(self, nome, cognome, tel,email, passw)
        self.idCliente = id_cliente
        self.nome_azienda = nome_azienda
        self.pIva = pIva
        self.indirizzo = indirizzo
        self.ordini_effettuali = []