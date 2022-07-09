from random import Random
import chess
from random_play import RandomAgent

class SelfPlay:
    '''
    Initiates two agents and lets them play against eachother and returns the outcome. Also possible to play n amount of games and get the result.
    '''
    def __init__(self, Agent1, Agent2, state=None) -> None:
        self.board = chess.Board(state)
        self.agent1 = Agent1
        self.agent2 = Agent2

    def play(self, games=1) -> str:
        played = 0
        while played < games:
            move = 0
            while self.board.is_game_over() == False:
                if move % 2 == 0:
                    self.board = self.agent1.make_move(self.board)
                else:
                    self.board = self.agent2.make_move(self.board) 
                move += 1
            print(self.board.outcome())
            played += 1
