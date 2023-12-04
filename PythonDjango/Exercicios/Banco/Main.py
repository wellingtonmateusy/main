from ContaCorrente import ContaCorrente

def main():
    pessoa1 = ContaCorrente(123456,'Ana',125)
    
    print(f'Conta: {pessoa1.numeroConta}, Nome correntista: {pessoa1.nomeCorrentista}, Saldo: {pessoa1.saldo}')
    
    valorDepositado = int(input("Digite o valor de deposito: "))
    valorSacado = int(input("Digite o valor para sacar: "))
    novoNome = (input("Digite o novo nome: "))

    pessoa1.nomeCorrentista = novoNome
    print(f'Conta: {pessoa1.numeroConta}, Nome correntista: {pessoa1.nomeCorrentista}, Saldo: {pessoa1.saldo}')
    
    pessoa1.depositar(valorDepositado)
    print(f'Conta: {pessoa1.numeroConta}, Nome correntista: {pessoa1.nomeCorrentista}, Saldo: {pessoa1.saldo}, Valor depositado: {valorDepositado}')
    
    pessoa1.sacar(valorSacado)
    print(f'Conta: {pessoa1.numeroConta}, Nome correntista: {pessoa1.nomeCorrentista}, Saldo: {pessoa1.saldo}, Valor sacado: {valorSacado}')

if __name__ == '__main__':
    main()