import chess
import random

def random_play():
  board = chess.Board()
  while board.is_checkmate() == False and board.is_insufficient_material() == False: 
      count = board.legal_moves.count()
      if count > 0:
        val = random.randrange(0,count)
        move = list(board.legal_moves)[val]
        board.push_uci(str(move))
      else:
        break
  return board.outcome().result(), board.outcome().termination, len(board.move_stack), board.board_fen()


results = []
endgames = []
move_counts = []
fens = []

for i in range(1000):
  result, endgame, moves, fen = random_play()
  results.append(result)
  endgames.append(endgame)
  move_counts.append(moves)
  fens.append(fen)

print(results)