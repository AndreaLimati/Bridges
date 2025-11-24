import hashlib

from modello.modello import AppData

class Controllore:
    def __init__(self, model: AppData):
        self.model = model

    def salva(self):
        self.model.salvaDati("data.pkl")

    def scegliIdMezzo(self):
        x=0
        for i in range(len(self.model.mezzi)):
            if x<self.model.mezzi[i].idMezzo:
                x = self.model.mezzi[i].idMezzo
        return x+1

    def scegliIdUtente(self):
        x=0
        for i in range(len(self.model.dipendenti)):
            if x<self.model.dipendenti[i].idDipendente:
                x = self.model.clienti[i].idCliente
        for i in range(len(self.model.clienti)):
            if x<self.model.clienti[i].idCliente:
                x = self.model.clienti[i].idCliente
        return x+1

    def scegliIdAziendaDest(self):
        x=0
        for i in range(len(self.model.azienda_dest)):
            if x<self.model.azienda_dest[i].idAzienda:
                x = self.model.azienda_dest[i].idAzienda
        return x+1

    def scegliIdPacco(self):
        x=0
        for i in range(len(self.model.pacchi)):
            if x<self.model.pacchi[i].idPacco:
                x = self.model.pacchi[i].idPacco
        return x+1

    def scegliIdCommissione(self):
        x=0
        for i in range(len(self.model.commissione)):
            if x<self.model.commissione[i].idCommissione:
                x = self.model.commissione[i].idCommissione
        return x+1

    def scegliIdSpedizione(self):
        x=0
        for i in range(len(self.model.spedizione)):
            if x<self.model.spedizione[i].idSpedizione:
                x = self.model.spedizione[i].idSpedizione
        return x+1

    def controllaLoginDipendenti(self, idUtente, password):
        password = hashlib.md5(password.encode())
        for i in range(len(self.model.dipendenti)):
            if idUtente==self.model.dipendenti[i].idDipendente & password==self.model.dipendenti[i].passw:
                return True
        return False

    def controllaLoginClienti(self, idUtente, password: str):
        password = self.hashPassword(password)
        for i in range(len(self.model.clienti)):
            if idUtente.__eq__(self.model.clienti[i].idCliente) and password.__eq__(self.model.clienti[i].passw):
                return True
        return False

    def registraAzienda(self, nome_ref: str, cognome_ref: str, tel_ref:str, nome_azienda:str, p_iva:str, indirizzo:str, email:str, password:str):
        from entita.cliente import Cliente
        id_cliente = self.scegliIdUtente()
        password = self.hashPassword(password)
        self.model.clienti.append(Cliente(id_cliente, nome_ref, cognome_ref, tel_ref, email, password, nome_azienda, p_iva, indirizzo))

    @staticmethod
    def hashPassword(x: str):
        return hashlib.md5(x.encode()).hexdigest()

    def aggiungiPaccoTemp(self, larghezza, lunghezza, altezza, peso, valore, etichettaPericolo, nome, nazione, citta, via, ref):
        from entita.pacco import Pacco
        azienda = self.registraAziendaDest(self.scegliIdAziendaDest(), nome, nazione, citta, via, ref)
        self.model.pacchi_temp.append(Pacco(self.scegliIdPacco(), larghezza, lunghezza, altezza, peso, valore, etichettaPericolo, azienda))
        self.model.pacchi.append(Pacco(self.scegliIdPacco(), larghezza, lunghezza, altezza, peso, valore, etichettaPericolo, azienda))

    def finalizzaPacchi(self, idCliente):
        from entita.commissione import Commissione
        self.model.commissione.append(Commissione(self.scegliIdCommissione(), idCliente, len(self.model.pacchi_temp), self.model.pacchi_temp))
        for i in range(len(self.model.pacchi_temp)):
            print(self.model.pacchi_temp[i].peso)
        self.model.pacchi_temp = []

    def registraAziendaDest(self, idAzienda, nome, nazione, citta, via, referente):
        from entita.azienda_destinazione import AziendaDestinazione
        self.model.azienda_dest.append(AziendaDestinazione(idAzienda, nome, nazione, citta, via, referente))
        return self.model.azienda_dest[len(self.model.azienda_dest) - 1]

    def visualizzaCommissioni(self, idCliente):
        vet = []
        for com in self.model.commissione:
            if com.getIdCliente().__eq__(idCliente):
                var = {
                    "idCommissione": str(com.idCommissione),
                    "idCliente": str(com.cliente),
                    "numeroPacchi": str(com.num_pacchi),
                    "listaPacchi": []
                }
                for pacco in com.lista_pacchi:
                    var["listaPacchi"].append(str(pacco.idPacco))
                vet.append(var)
        return vet

    def clienteAnnullaCommissione(self, idCommissione, idCliente):
        for comm in self.model.commissione:
            if comm.getIdCliente().__eq__(idCliente) and comm.getIdCommissione.__eq__(idCommissione):
                for p in comm.lista_pacchi:
                    if self.model.pacchi.__contains__(p):
                        self.model.pacchi.remove(p)
                self.model.commissione.remove(comm)