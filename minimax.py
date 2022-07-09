import chess
import random

class MiniMax:
  '''
  Takes in a board position and returns the minimax move.
  '''

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


  def make_move(self, fen) -> str:
    board = chess.Board(fen)
    #print(f'To move {board.turn} current {self.evaluate(board.fen())}')
    if board.is_game_over() == False:
      evals = {} 
      best_move = -999
      selected_move = list(board.legal_moves)[0]
      
      # Only looks depth 1
      for move in list(board.legal_moves):
        board.push_uci(str(move))
        score = self.evaluate(board.fen()) * -1
        if score > best_move:
          best_move = score
          selected_move = move
        evals[move] = score
        board.set_fen(fen)

      board.push_uci(str(selected_move))

    return board.fen()
