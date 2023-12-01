class Pessoa:
    
    def __init__ (self, nome: str, idade: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhercer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.altura += 0.5
        else:
            print('Você não cresce mais')

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        if self.peso - peso > 0:
            self.peso -= peso
        else:
            print("Não é possível emagrecer essa quantidade de peso!")

    def crescer(self, altura):
        self.altura = altura

pessoa1 = Pessoa('Antonia', 18, 80.5, 1.84)

pessoa1.envelhercer(1)
pessoa1.engordar(5)
pessoa1.emagrecer(3)
print(f'Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nPeso: {pessoa1.peso}\nAltura: {pessoa1.altura}')
pessoa1.crescer(1)


