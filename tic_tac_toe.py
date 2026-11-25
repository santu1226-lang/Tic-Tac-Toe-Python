class TicTacToe:
    WIN_LINES = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

    def __init__(self):
        self.board = [' '] * 9
        self.player = 'X'

    def display(self):
        cells = [v if v != ' ' else str(i+1) for i,v in enumerate(self.board)]
        for i in range(0,9,3):
            print(' | '.join(cells[i:i+3]))
            if i < 6:
                print('--+---+--')

    def move(self, position):
        if not 1 <= position <= 9 or self.board[position-1] != ' ':
            return False
        self.board[position-1] = self.player
        return True

    def winner(self):
        return any(all(self.board[i] == self.player for i in line) for line in self.WIN_LINES)

    def draw(self):
        return ' ' not in self.board and not self.winner()

    def play(self):
        print('Welcome to Tic-Tac-Toe!')
        while True:
            self.display()
            try:
                position = int(input(f'Player {self.player}, choose 1-9: '))
            except ValueError:
                print('Enter a number from 1 to 9.')
                continue
            if not self.move(position):
                print('Invalid or occupied position. Try again.')
                continue
            if self.winner():
                self.display()
                print(f'Player {self.player} wins!')
                break
            if self.draw():
                self.display()
                print('Game drawn!')
                break
            self.player = 'O' if self.player == 'X' else 'X'

if __name__ == '__main__':
    TicTacToe().play()
