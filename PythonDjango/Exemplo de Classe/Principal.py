from Pessoa import Pessoa

class Principal:

    pessoa1 = Pessoa(nome = 'Jose', altura = 1.87, idade = 78, etnia = 'caucasiano')
    
    pessoa1.apresentar()
    pessoa1.cozinhar('Feijão')
    pessoa1.andar(250.0)