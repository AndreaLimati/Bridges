class Commissione:
    def __init__(self, idCommissione, cliente, num_pacchi, lista_pacchi):
        self.idCommissione = idCommissione
        self.cliente = cliente
        self.num_pacchi = num_pacchi
        self.lista_pacchi = lista_pacchi

    def getIdCliente(self):
        return self.cliente

    def getIdCommissione(self):
        return self.idCommissione