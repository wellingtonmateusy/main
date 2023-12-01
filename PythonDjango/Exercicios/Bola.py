class Bola:
    def __init__ (self, cor: str, circunferencia: int, material:  str):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        
    def setCor(self, novaCor):
        self.cor = novaCor
    
    def getCor(self):
        return self.cor
    
    def exibir(self):
        print(f'A cor da bola é: {bola.getCor()} \nSua circunferência é de: {bola.circunferencia}cm \nSeu material é de: {bola.material}\n')

bola = Bola('azul', 50, 'plástico')
bola.exibir()
bola.setCor(novaCor = input('Digite a cor para alterar a cor da bola: '))
bola.exibir()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         


# Professor

class Bola:

    def __init__(self, cor: str, circunf: int, material: str):
        self.cor = cor
        self.circuf = circunf
        self.material = material
        
    
    def setCor(self, cor: str) -> None:
        self.cor = cor

    def getCor(self) -> str:
        return self.cor
    
    def setCircunf(self, circunf: int) -> None:
        self.circunf = circunf

    def getCircunf(self) -> int:
        return self.circunf

    def setMaterial(self, material: str) -> None:
        self.material = material

    def getMaterial(self) -> str:
        return self.material
