from tokenize import String
import chess
import random

class RandomAgent:
  '''
  Takes in a board position and returns a random legal move.
  '''

  def make_move(self, state) -> str:
    board = chess.Board(state)
    print(board)
    if board.is_checkmate() == False and board.is_insufficient_material() == False:
      legal_moves = board.legal_moves.count() 
      if legal_moves > 0:
        val = random.randrange(0,legal_moves)
        move = list(board.legal_moves)[val]
        print(move)
        board.push_uci(str(move))
    return board.fen()


  