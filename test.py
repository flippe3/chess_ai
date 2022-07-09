from selfplay import SelfPlay
from randomplay import RandomAgent
from minimax import MiniMax

ag1 = RandomAgent()
ag2 = MiniMax()

selfplay = SelfPlay(ag1, ag2)

selfplay.play(games=1, show_moves=False, show_end=True)