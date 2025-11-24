import pickle

class AppData:
    def __init__(self):
        self.dipendenti = []
        self.amministratori = []
        self.clienti = []
        self.pacchi = []
        self.spedizione = []
        self.commissione = []
        self.azienda_dest = []
        self.mezzi = []

        self.pacchi_temp = []

    @staticmethod
    def carica(path: str) -> "AppData":
        try:
            with open(path, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return AppData()

    def salvaDati(self, path: str):
        with open(path, "wb") as f:
            pickle.dump(self, f)