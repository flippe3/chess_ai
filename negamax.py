import chess
import random

class NegaMax:
  '''
  Takes in a board position and returns the negamax move.
  '''
  def __init__(self, depth) -> None:
    self.depth = depth

  def evaluate(self, fen) -> int:
    board = chess.Board(fen)
    
    white = board.occupied_co[chess.WHITE]
    black = board.occupied_co[chess.BLACK]
    score = 0 
    
    score += chess.popcount(white & board.pawns) - chess.popcount(black & board.pawns)
    score += 3 * (chess.popcount(white & board.knights) - chess.popcount(black & board.knights))
    score += 3 * (chess.popcount(white & board.bishops) - chess.popcount(black & board.bishops))
    score += 5 * (chess.popcount(white & board.rooks) - chess.popcount(black & board.rooks))
    score += 9 * (chess.popcount(white & board.queens) - chess.popcount(black & board.queens)) 
    
    if board.turn == chess.BLACK:
      return score * -1
    return score 

  def negamax(self, fen, depth):
    if depth == 0 or chess.Board(fen).is_game_over():
      return self.evaluate(fen), fen
    else:
      board = chess.Board(fen)
      best_score = -999999
      mv = str(list(board.legal_moves)[0])
      for move in list(board.legal_moves):
        board.push_uci(str(move))
        score,last_move  = self.negamax(board.fen(), depth-1)
        score = score * -1
        if score > best_score:
          best_score = score
          mv = move
        board.set_fen(fen)
      print(board.fen())
      return best_score, board.fen()

  def make_move(self, fen) -> str:
    board = chess.Board(fen)
    #print(f'To move {board.turn} current {self.evaluate(board.fen())}')
    if board.is_game_over() == False:
      score, fen = self.negamax(fen, self.depth)
      #board.push_uci(mv)
      board.set_fen(fen)
    return board.fen()


# int negaMax( int depth ) {
#     if ( depth == 0 )
#       return evaluate();

#     int max = -999999;
#     for ( all moves)  {
#         score = -negaMax( depth - 1 );
#         if( score > max )
#             max = score;
#     }
#     return max;
# }
