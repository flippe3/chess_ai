from random import Random
from re import I
import chess

class SelfPlay:
    '''
    Initiates two agents and lets them play against eachother and returns the outcome. Also possible to play n amount of games and get the result.
    '''
    def __init__(self, Agent1, Agent2, state=chess.STARTING_FEN) -> None:
        self.board = chess.Board(state)
        self.agent1 = Agent1
        self.agent2 = Agent2
        self.start_state = state

    def play(self, games=1) -> str:
        played = 0
        black_wins, white_wins, draws = 0, 0, 0
        while played < games:
            move = 0
            while self.board.is_game_over() == False:
                if move % 2 == 0:
                    self.board.set_fen(self.agent1.make_move(self.board.fen()))
                else:
                    self.board.set_fen(self.agent2.make_move(self.board.fen()))
                move += 1
            if self.board.outcome().winner == False:
                black_wins += 1
            elif self.board.outcome().winner == True:
                white_wins += 1
            else:
                draws += 1
            # Reset the board
            self.board = chess.Board(self.start_state)
            played += 1 

        print(f"White Wins:{white_wins}, Black Wins: {black_wins}, Draws: {draws}")
            