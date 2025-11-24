from entita.dipendente import Dipendente

class Amministratore:
    def __init__(self, nome: str, cognome: str, tel: str, email: str, passw: str, patenti, ruolo: str, scadenza, tipo_contratto, stipendio, inizio_incarico, fine_incarico):
        Dipendente.__init__(self, nome, cognome, tel, email, passw, patenti, ruolo, scadenza, tipo_contratto, stipendio)
        self.inizio_incarico = inizio_incarico
        self.fine_incarico = fine_incarico