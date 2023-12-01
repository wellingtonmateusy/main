from Bola import Bola

class Main:
    
    def main():

        ball = Bola('Verde', 72, 'PVC')

        print(f'Cor da bola: {ball.getCor()}')
        print(f'Material: {ball.getMaterial}')

        ball.setCor('Vermelha')
        print(f'Cor da bola: {ball.getCor()}')

    if __name__ == '__main__':
        main()