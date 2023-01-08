from typing import Optional

from ..game import Bot, Move, PartialTrick, PlayerGameState


class AlphaBetaBot(Bot):
    __max_depth = -1
    __randomize = True

    def __init__(self, randomize: bool = True, depth: int = 8) -> None:
        self.__randomize = randomize
        self.__max_depth = depth

    def get_move(
        self, state: PlayerGameState, leader_move: Optional[PartialTrick]
    ) -> Move:
        raise NotImplementedError()
