from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_manager import GameManager

from scene import Scene

class Game(Scene):
    def setup(self) -> None:
        # Main game initialization goes here
        super().setup()

    def update(self) -> None:
        # Main game update logic goes here
        super().update()
        # or here if the logic should run after all sprites update

    def draw(self) -> None:
        # Main game drawing goes here
        super().draw()
        # or here if drawn on top of all sprites