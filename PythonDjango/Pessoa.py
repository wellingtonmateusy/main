class Pessoa:
    
    def __init__ (self, nome: str, altura: float, idade: int, etnia: str):
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.etnia = etnia
    
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}')

    def andar(self, distancia: float):
        print(f'Eu sai para caminhar. Voltarei quando completar {distancia} metros.')

    def cozinhar(self, receita: str):
        print(f'Estou cozinhando um(a) {receita}')