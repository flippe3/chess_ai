from selfplay import SelfPlay
from randomplay import RandomAgent
from negamax import NegaMax

ag1 = RandomAgent()
ag2 = NegaMax(3)

selfplay = SelfPlay(ag1, ag2)

selfplay.play(games=1, show_moves=False, show_end=True)