class Aluno:
    
    def __init__ (self, nome: str, matricula: complex, nota:  list):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota
    
    def apresentar(self):
        print(f'\nOlá, Aluno {self.nome}\nSua Matrícula é {self.matricula}')

    def calcularNotas(self):
        if not self.nota:
            return 0
        return sum(self.nota) / 5

    def media(self):
        print(f'Sua Média {self.calcularNotas()}')
        
aluno1 = Aluno(nome = 'Jose', matricula = 123, nota = [2.0, 5.0, 6.0, 8.0, 9.0])
aluno2 = Aluno(nome = 'Andresa', matricula = 456, nota = [6.0, 4.5, 6.5, 8.0, 9.0])
    
aluno1.apresentar()
aluno1.media()
aluno2.apresentar()
aluno2.media()


# Professor

class Aluno:
    
    def __init__(self, nome:str, matricula: int, notas: []):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas

    def media(self):
        return sum(self.notas) / len(self.notas)
    
    def exibirInfos(self):
        print(f'Nome: {self.nome}\nMatricula: {self.matricula}\nNotas: {self.notas} - Médias: {self.media()}')