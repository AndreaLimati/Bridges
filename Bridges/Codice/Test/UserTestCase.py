from unittest import TestCase


class User:
    objects = None


class UserTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        User.objects.create(
            nome="nomeUtente",
            cognome="cognomeUtente",
            telefono="3333333333",
            email="prova@gmail.com",
            password="123321"
        )

    def testNome(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.nome, "nomeUtente")

    def testCognome(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.cognome, "cognomeUtente")

    def testTelefono(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.telefono, "3333333333")

    def testEmail(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.email, "prova")

    def testPassword(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.password, "123321")


class Mezzo:
    objects = None


class MezzoTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        Mezzo.objects.create(
            marca="marcaMezzo",
            modello = "modelloMezzo",
            num_targa = "numTargaMezzo",
            num_telaio = "numTelaioMezzo",
            cap_carico = "capCaricoMezzo"
        )

    def testMarca(self):
        mezzo = Mezzo.objects.get(id=1)
        self.assertEqual(mezzo.marca, "marcaMezzo")

    def testModello(self):
        mezzo = Mezzo.objects.get(id=1)
        self.assertEqual(mezzo.modello, "modelloMezzo")

    def testNumTarga(self):
        mezzo = Mezzo.objects.get(id=1)
        self.assertEqual(mezzo.num_targa, "numTargaMezzo")

    def testNumTelaio(self):
        mezzo = Mezzo.objects.get(id=1)
        self.assertEqual(mezzo.num_telaio, "numTelaioMezzo")

    def testCapCarico(self):
        mezzo = Mezzo.objects.get(id=1)
        self.assertEqual(mezzo.cap_carico, "capCaricoMezzo")


class Spedizione:
    objects = None


class Pacco:
    objects = None


class SpedizioneTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        Spedizione.object.create(
            mezzo = Mezzo.objects.create(
                marca="marcaMezzo",
                modello="modelloMezzo",
                num_targa="numTargaMezzo",
                num_telaio="numTelaioMezzo",
                cap_carico="capCaricoMezzo"
            ),
            listaPacchi = Pacco.objects.create(
                larghezza = "larghezzaPacco",
                lunghezza = "lunghezzaPacco",
                altezza = "altezzaPacco",
                peso = "pesoPacco",
                valore = "valorePacco",
                etichetta_pericolo = "etichettaPericolo",
                azienda_dest = "aziendaDestPacco"
            ),
        )

    def testMezzo(self):
        spedizione = Spedizione.objects.get(id=1)
        self.assertEqual(spedizione.mezzo.num_targa, "marcaMezzo")

    def testPacco(self):
        spedizione = Spedizione.objects.get(id=1)
        self.assertEqual(spedizione.listaPacchi.peso, "pesoPacco")