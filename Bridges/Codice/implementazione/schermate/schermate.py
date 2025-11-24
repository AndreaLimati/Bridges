from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QLineEdit, QGridLayout, QMessageBox
from controllori.controllori import Controllore
from modello.modello import AppData

class View(QWidget):
    def __init__(self):
        super().__init__()
        self.idUtente = 0
        self.setWindowTitle("BRIDGES")
        self.model = AppData.carica("data.pkl")
        self.controllore = Controllore(self.model)
        self.finestraIniziale()


    def finestraIniziale(self):
        self.clearLayout()
        layout = QVBoxLayout()

        id_utente = QLineEdit()
        id_utente.setPlaceholderText("ID Utente")
        password = QLineEdit()
        password.setPlaceholderText("Password")

        button_log = QPushButton("Login")
        button_reg = QPushButton("Registrati")
        button_dip = QPushButton("Dipendente")

        button_dip.pressed.connect(self.finestraDipendente)
        button_log.pressed.connect(lambda: self.chiamaControlloLogin(id_utente.text(), password.text()))
        button_reg.pressed.connect(self.finestraRegistrazione)

        layout.addWidget(id_utente)
        layout.addWidget(password)
        layout.addWidget(button_reg)
        layout.addWidget(button_log)
        layout.addWidget(button_dip)
        self.setLayout(layout)

    def chiamaControlloLogin(self, id_utente: str, passw: str):
        if not id_utente.isdigit():
            QMessageBox.warning(self, "Error", "ID Utente non valido")
        elif self.controllore.controllaLoginDipendenti(id_utente, passw):
            self.idUtente = id_utente
            self.finestraDipendente()
        elif self.controllore.controllaLoginClienti(id_utente, passw):
            self.idUtente = id_utente
            self.finestraPrincipale()
        else:
            QMessageBox.warning(self, "Error", "Credenziali non valide")

    def finestraPrincipale(self):
        self.clearLayout()
        layout = QVBoxLayout()

        self.controllore.salva()

        button_richiesta = QPushButton("Richiesta commissione")
        button_resoconto = QPushButton("Resoconto spedizioni")
        button_annulla = QPushButton("Annulla commissione")
        button_indietro = QPushButton("Indietro")

        button_indietro.pressed.connect(self.finestraIniziale)
        button_resoconto.pressed.connect(self.resocontoCommissioni)
        button_annulla.pressed.connect(self.annullaCommissione)
        button_richiesta.pressed.connect(self.richiestaCommissione)

        layout.addWidget(button_richiesta)
        layout.addWidget(button_resoconto)
        layout.addWidget(button_annulla)
        layout.addWidget(button_indietro)
        self.setLayout(layout)

    def finestraDipendente(self):
        self.clearLayout()
        layout = QVBoxLayout()

        button_visualizza_com = QPushButton("Visualizza Commissione")
        button_visualizza_inv = QPushButton("Visualizza Inventario")
        button_conferma = QPushButton("Conferma Arrivo")
        button_rimuovi = QPushButton("Rimuovi Pacco")
        button_segnala = QPushButton("Segnala Danneggiamento")
        button_prepara = QPushButton("Prepara Spedizione")
        button_aggiorna_spedizione = QPushButton("Aggiorna Stato Spedizione")
        button_aggiorna_mezzo = QPushButton("Aggiorna Stato Mezzo")
        button_indietro = QPushButton("Indietro")

        button_indietro.pressed.connect(self.finestraIniziale)

        layout.addWidget(button_visualizza_com)
        layout.addWidget(button_visualizza_inv)
        layout.addWidget(button_conferma)
        layout.addWidget(button_rimuovi)
        layout.addWidget(button_segnala)
        layout.addWidget(button_prepara)
        layout.addWidget(button_aggiorna_spedizione)
        layout.addWidget(button_aggiorna_mezzo)
        layout.addWidget(button_indietro)

        self.setLayout(layout)

    def richiestaCommissione(self):
        self.clearLayout()
        layout = QVBoxLayout()

        peso = QLineEdit()
        altezza = QLineEdit()
        lunghezza = QLineEdit()
        spessore = QLineEdit()
        costo = QLineEdit()
        sicurezza = QLineEdit()
        nazione_dest = QLineEdit()
        citta_dest = QLineEdit()
        via_dest = QLineEdit()
        nomeazienda_dest = QLineEdit()
        nomeref_dest = QLineEdit()

        peso.setPlaceholderText("Peso")
        altezza.setPlaceholderText("Altezza")
        lunghezza.setPlaceholderText("Lunghezza")
        spessore.setPlaceholderText("Spessore")
        costo.setPlaceholderText("Costo")
        sicurezza.setPlaceholderText("Sicurezza")
        nazione_dest.setPlaceholderText("Nazione di destinazione")
        citta_dest.setPlaceholderText("Città di destinazione")
        via_dest.setPlaceholderText("Via di destinazione")
        nomeazienda_dest.setPlaceholderText("Nome azienda di destinazione")
        nomeref_dest.setPlaceholderText("Nome referente di destinazione")

        button_aggiungipacco = QPushButton("Aggiungi")
        button_conferma = QPushButton("Conferma")
        button_indietro = QPushButton("Indietro")

        button_aggiungipacco.pressed.connect(lambda: self.controllore.aggiungiPaccoTemp(spessore.text(), lunghezza.text(), altezza.text(), peso.text(), costo.text(), sicurezza.text(), nomeazienda_dest.text(), nazione_dest.text(), citta_dest.text(), via_dest.text(), nomeref_dest.text()))
        button_conferma.pressed.connect(lambda: self.controllore.finalizzaPacchi(self.idUtente))
        button_indietro.pressed.connect(self.finestraPrincipale)

        layout.addWidget(peso)
        layout.addWidget(altezza)
        layout.addWidget(lunghezza)
        layout.addWidget(spessore)
        layout.addWidget(costo)
        layout.addWidget(sicurezza)
        layout.addWidget(nazione_dest)
        layout.addWidget(citta_dest)
        layout.addWidget(via_dest)
        layout.addWidget(nomeazienda_dest)
        layout.addWidget(nomeref_dest)
        layout.addWidget(button_aggiungipacco)
        layout.addWidget(button_conferma)
        layout.addWidget(button_indietro)
        self.setLayout(layout)

    def finestraRegistrazione(self):
        self.clearLayout()
        layout = QVBoxLayout()

        nome = QLineEdit()
        cognome = QLineEdit()
        tel = QLineEdit()
        nome_azienda = QLineEdit()
        p_iva = QLineEdit()
        indirizzo_sede = QLineEdit()
        email = QLineEdit()
        password = QLineEdit()

        conferma = QPushButton("Conferma")
        button_indietro = QPushButton("Indietro")

        conferma.pressed.connect(lambda: self.controllore.registraAzienda(nome.text(), cognome.text(), tel.text(), nome_azienda.text(), p_iva.text(), indirizzo_sede.text(), email.text(), password.text()))
        button_indietro.pressed.connect(self.finestraIniziale)

        nome.setPlaceholderText("Nome Referente")
        cognome.setPlaceholderText("Cognome Referente")
        tel.setPlaceholderText("Telefono Referente")
        nome_azienda.setPlaceholderText("Nome Azienda")
        p_iva.setPlaceholderText("P.IVA")
        indirizzo_sede.setPlaceholderText("Indirizzo Sede")
        email.setPlaceholderText("Email")
        password.setPlaceholderText("Password")

        layout.addWidget(nome)
        layout.addWidget(cognome)
        layout.addWidget(tel)
        layout.addWidget(nome_azienda)
        layout.addWidget(p_iva)
        layout.addWidget(indirizzo_sede)
        layout.addWidget(email)
        layout.addWidget(password)
        layout.addWidget(conferma)
        layout.addWidget(button_indietro)
        self.setLayout(layout)

    def resocontoCommissioni(self):
        self.clearLayout()
        layout = QGridLayout()

        #ricerca per idCliente, poi stampa le commisioni
        vet = self.controllore.visualizzaCommissioni(self.idUtente)

        intestazione1 = QLabel("ID COMMISSIONE")
        intestazione2 = QLabel("ID CLIENTE")
        intestazione3 = QLabel("NUMERO PACCHI")
        intestazione4 = QLabel("ID PACCHI")

        layout.addWidget(intestazione1, 0, 0)
        layout.addWidget(intestazione2, 0, 1)
        layout.addWidget(intestazione3, 0, 2)
        layout.addWidget(intestazione4, 0, 3)

        i = 1

        for v in vet:
            idComm = QLabel(v["idCommissione"])
            idCliente = QLabel(v["idCliente"])
            numeroPacchi = QLabel(v["numeroPacchi"])
            text = "["
            for j in range(len(v["listaPacchi"])):
                if j==len(v["listaPacchi"])-1:
                    text+=str(v["listaPacchi"][j])
                else:
                    text += str(v["listaPacchi"][j]) + ", "
            text+= "]"
            idPacchi = QLabel(text)

            layout.addWidget(idComm, i, 0)
            layout.addWidget(idCliente, i, 1)
            layout.addWidget(numeroPacchi, i, 2)
            layout.addWidget(idPacchi, i, 3)

            i+=1

        button_indietro = QPushButton("Indietro")

        button_indietro.pressed.connect(self.finestraPrincipale)

        layout.addWidget(button_indietro, i, 0)
        self.setLayout(layout)

    def annullaCommissione(self):
            self.clearLayout()
            layout = QVBoxLayout()

            idCancellare = QLineEdit()

            conferma = QPushButton("Conferma")
            button_indietro = QPushButton("Indietro")

            conferma.pressed.connect(lambda: self.controllore.clienteAnnullaCommissione(idCancellare.text(), self.idUtente))
            button_indietro.pressed.connect(self.finestraPrincipale)

            layout.addWidget(idCancellare)
            layout.addWidget(conferma)
            layout.addWidget(button_indietro)

            self.setLayout(layout)

    def clearLayout(self):
        if self.layout():
            QWidget().setLayout(self.layout())




