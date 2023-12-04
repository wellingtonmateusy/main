class ContaCorrente:

    def __init__(self, numeroConta, nomeCorrentista, saldo):
        self.__numeroConta = numeroConta
        self.__nomeCorrentista = nomeCorrentista
        self.__saldo = saldo

    @property
    def numeroConta(self):
        return self.__numeroConta

    @numeroConta.setter
    def numeroConta(self, numeroConta):
        self.__numeroConta = numeroConta
        
    @property
    def nomeCorrentista(self):
        return self.__nomeCorrentista

    @nomeCorrentista.setter
    def nomeCorrentista(self, novoNome):
        self.__nomeCorrentista = novoNome
    
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
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