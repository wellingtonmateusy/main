# 2. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 

#- Atributos: número da conta, nome do correntista e saldo. 

#- Métodos: alterarNome, depósito e saque; 

#No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrete:
    
    def __init__(self, numeroConta:complex, nomeCorrentista: str, saldo: float):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo
        
    def alterarNome(self, novoNome):
        self.nomeCorrentista = novoNome
    
    def depositar(self, valorDepositado):
        if (valorDepositado > 0):
            self.saldo += valorDepositado

    def sacar(self, valorSacado):
        if (valorSacado <= self.saldo):
            self.saldo -= valorSacado
            return True
        else:
            print("Saldo insuficiente!")
            return False

conta1 = ContaCorrete(54321,"Joao",500)
print(f"Numero da conta: {conta1.numeroConta}")
print(f"Nome do correntista: {conta1.nomeCorrentista}")
print(f"Saldo:{conta1.saldo}\n")
conta1.alterarNome('Maria')
print(f"Novo Nome:{ conta1.nomeCorrentista}")
conta1.depositar(700)
print(f"Novo Saldo: {conta1.saldo}")
conta1.sacar(800)