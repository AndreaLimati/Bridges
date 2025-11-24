from entita.utente import Utente
from controllori.controllori import Controllore

class Dipendente(Utente):
    def __init__(self, idDipendente, nome: str, cognome: str, tel: str, email: str, passw: str, patenti, ruolo: str, scadenza, tipo_contratto, stipendio):
        Utente.__init__(self, nome, cognome, tel, email, passw)
        self.idDipendente = idDipendente
        self.patenti = patenti
        self.ruolo = ruolo
        self.scadenza = scadenza
        self.tipo_contratto = tipo_contratto
        self.stipendio = stipendio
    
