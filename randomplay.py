import chess
import random

class RandomAgent:
  '''
  Takes in a board position and returns a random legal move.
  '''

  def make_move(self, state) -> str:
    board = chess.Board(state)
    if board.is_game_over() == False:
      legal_moves = board.legal_moves.count()
      if legal_moves > 0:
        val = random.randrange(0, legal_moves)
        move = list(board.legal_moves)[val]
        board.push_uci(str(move))
    return board.fen()
