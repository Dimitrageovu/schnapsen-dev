from src.schnapsen.game import Bot, PlayerPerspective, PartialTrick, Move
from typing import Optional
import random


class RandBot(Bot):
    def __init__(self, seed: int) -> None:
        self.seed = seed
        self.rng = random.Random(self.seed)

    def get_move(self, player_perspective: PlayerPerspective, leader_move: Optional[PartialTrick]) -> Move:
        moves = player_perspective.valid_moves()
        move = self.rng.choice(list(moves))
        return move

    def __repr__(self) -> str:
        return f"RandBot(seed={self.seed})"
