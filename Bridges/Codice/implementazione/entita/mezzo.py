class Mezzo:
    def __init__(self, idMezzo, marca: str, modello: str, num_targa: str, num_telaio: str, cap_carico: int) -> None:
        self.idMezzo = idMezzo
        self.marca = marca
        self.modello = modello
        self.num_targa = num_targa
        self.num_telaio = num_telaio
        self.cap_carico = cap_carico
        self.autisti = []

    def assegnaAutista(self, Dipendente):
        self.autisti.append(Dipendente)