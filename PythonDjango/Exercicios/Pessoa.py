# 1. Classe Pessoa: Crie uma classe que modele uma pessoa:

#- Atributos: nome, idade, peso e altura

#- Métodos: Envelhercer, engordar, emagrecer, crescer. 

#Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
class Pessoa:
    
    def __init__ (self, nome: str, idade: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def interface(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Peso:", self.peso)
        print("Altura:", self.altura)

    def envelhecer(self):
        self.idade += 1

    def engordar(self, quant_kg):
        self.peso += quant_kg

    def emagrecer(self, quant_kg):
        if self.peso - quant_kg < 0:
            return print("Você não pode se emagrecer!")
        else:
            self.peso -= quant_kg

    def crescer(self, cm):
        if self.altura > 21:
            self.altura += cm
        else:
            return print("Você não pode crescer mais por conta da sua idade")

pessoa1 = Pessoa('Luiz Marcos', 32, 78.5, 1.65)
pessoa1.envelhecer()
pessoa1.engordar(quant_kg = 1)
pessoa1.emagrecer(quant_kg = 2)
pessoa1.crescer(cm = 0.50)
pessoa1.interface()



