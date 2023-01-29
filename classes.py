
class Board():
    def __init__(self):
        self.board = [
            [ 0,  1,  0,  1,  0,  1,  0,  1],
            [ 1,  0,  1,  0,  1,  0,  1,  0],
            [ 0,  1,  0,  1,  0,  1,  0,  1],
            [ 0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0],
            [-1,  0, -1,  0, -1,  0, -1,  0],
            [ 0, -1,  0, -1,  0, -1,  0, -1],
            [-1,  0, -1,  0, -1,  0, -1,  0],
        ]
        
    def __str__(self):
        print_board = ''
        for row in self.board:
            print_board = print_board + '+---+---+---+---+---+---+---+---+\n'
            for square in row:
                print_board = print_board + '| '
                if square == 1:
                    print_board = print_board + '○'
                elif square == 0:
                    print_board = print_board + ' '
                elif square == -1:
                    print_board = print_board + '●'
                print_board = print_board + ' '
            print_board = print_board + '|\n'
        print_board = print_board + '+---+---+---+---+---+---+---+---+'
        return print_board