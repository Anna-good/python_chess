import chess
import chess.pgn

class ChessEngine:
    def __init__(self):
        self.chess_table = chess.Board()
        self.move_log = []
    
    def is_game_over(self):
        '''checkmate, stalemate, insufficient material, the seventyfive-move rule, fivefold repetition or a variant end condition'''
        return self.chess_table.is_game_over(claim_draw=True)

    def which_players_move(self):
        return 'White' if self.chess_table.turn else 'Black'
    
    def upload_game(self, path_to_game):
        pgn = open(path_to_game)
        first_game = chess.pgn.read_game(pgn)
        self.chess_table = first_game.board()
        for move in first_game.mainline_moves():
            self.chess_table.push(move)

    def print_field(self):
        pieces_row_series = self.chess_table.__str__().split('\n')

        print ("\n    A B C D E F G H  \n") 

        for i in range(8):
            print(8 - i, ' ', pieces_row_series[i], ' ', 9 - i)

        print ("\n    A B C D E F G H  \n") 
    
    def can_handle_move(self, uci_move_string):
        try:
            uci_move = chess.Move.from_uci(uci_move_string)
        except chess.InvalidMoveError:
            print('The move does not fit into the framework of the playing field')
            return False

        if self.is_game_over():
            print('The game is no longer going on!')
            return False

        if uci_move not in self.chess_table.legal_moves:
            sans = ", ".join(self.chess_table.san(move) for move in list(self.chess_table.legal_moves))
            print('Is not a possible move. Possible moves: ', sans)
            return False
        
        self.move_log.append(uci_move)
        self.chess_table.push(uci_move)
        
        return True
    
    def roll_back_the_move(self):
        self.chess_table.pop()

def get_what_would_player_like_to_do(player_token):
    player_answer = input(player_token + " - Enter the number of the sub-item\n1. Start new game\n2. Upload game \n3. Make a move\n4. Roll back the move\n5. Stop\n> ")
    try:
        return int(player_answer)
    except:
        return 5

def get_where_would_player_like_to_go(player_token):
    player_answer = input(player_token + " - What piece and where do you want to place it?\n> ")
    return player_answer

def ask_to_continue():
    input("Contunue? Press enter\n> ")

def start_engine():
    engine = ChessEngine()

    command = 1
    while command != 5:
        engine.print_field()
        command = get_what_would_player_like_to_do(engine.which_players_move())

        if command == 1:
            engine = ChessEngine()
        
        if command == 2:
            engine = ChessEngine()
            engine.upload_game("Magnus_Carlsen_-_Vladimir_Kramnik.txt2")

        if command == 3 and not engine.can_handle_move(get_where_would_player_like_to_go(engine.which_players_move())):
            ask_to_continue()

        if command == 4:
            engine.roll_back_the_move()

def preview_game(path_to_file):
    path_to_file

def main():
    start_engine()

if __name__ == '__main__':
    main()
