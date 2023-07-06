class Pessoa:
    def __init__(self):
        self.nome = None
        self.gmail = None

    def login(self):
        self.nome = input("Digite o nome: ")
        self.gmail = input("Digite o gmail: ")
        self.logado = print("------------------\nLogin bem sucedido!\n nome: {}\ngmail: {}".format(self.nome, self.gmail))

class Locomacao(Pessoa):
    def __init__(self):
        self.sair_de_casa = None
        self.volta_pra_casa = None

    def sair(self):
        self.sair_de_casa = True
        self.volta_pra_casa = False
        if self.sair_de_casa == True:
            print("Vc saiu de casa!")
        else:
            print("em casa ainda")    

    def voltar(self):
        self.sair_de_casa = False
        self.volta_pra_casa = True    
        if self.volta_pra_casa == True:
            print("Vc esta voltando pra casa!")
        else:
            print("na rua ainda")
    def onde_estar(self):
        if self.sair_de_casa == True:
            print("na rua")
        else:
            print("estar em casa")
class Comer(Locomacao):
    def __init__(self, sair_de_casa):
        super().__init__(sair_de_casa)
        self.alimento = None
        self.bebida = None
    def Beber(self):
        self.sair_de_casa = False
        if self.sair_de_casa == False:
            self.bebida = True
    def Comer(self):
        self.sair_de_casa = False
        if self.sair_de_casa == False:
            self.alimento = True        
    def __str__(self) -> str:
        return f"vc se alimentou? {self.alimento} e bebeu agua? {self.bebida}"


jorge = Pessoa()
jorge.login()
jorge = Locomacao()
jorge.sair()
jorge.voltar()
jorge.sair()
jorge.onde_estar()
jorge = Comer()
jorge.Comer()
jorge.Beber()