
class PersonAccount:
    def __init__(self):
        self.nome = None
        self.sb_nome = None
        self.receitas = None
        self.despesas = None
    
    def total_income(self):
        self.receitas = 300

    def total_expense(self):
        self.despesas = 164  

    def account_info(self):
        self.nome = 'pollyana'
        self.sb_nome = 's. Rocha'
        #rendimento
       
    def account_balance(self):
        self.total_income()
        self.total_expense()
        self.account_info()
        total_livre = self.receitas - self.despesas
        return f'A {self.nome} {self.sb_nome} tem o total de {total_livre} no final do mes'
#Rendimentos é um conjunto de rendimentos e sua descrição. 
# O mesmo vale para as despesas.
polly = PersonAccount()
print(polly.account_balance())