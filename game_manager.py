from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from scene import Scene

import pygame
import sys

from pygame.locals import DOUBLEBUF, HWSURFACE, QUIT, K_F3, KEYDOWN
from enum import Enum

from constants import SCR_DIM, FPS
from game import Game

class GameManager:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SCR_DIM, DOUBLEBUF | HWSURFACE)
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick_busy_loop(FPS) / 1000
        self.debug = False

        self.scene = Game(self)
        self.scene.setup()

    def run(self):
        while self.scene.running:
            self.update()
            self.scene.draw()
            if self.debug:
                self.scene.debug()
            pygame.display.flip()

        self.kill()

    def update(self):
        self.dt = self.clock.tick_busy_loop(FPS) / 1000 # dt calculated for pixels/second
        pygame.display.set_caption(f"Pygame Window | {self.clock.get_fps():.0f}")
        self.events = {event.type: event for event in pygame.event.get()}

        if QUIT in self.events:
            self.kill()

        self.scene.update()

    def kill(self) -> None:
        pygame.quit()
        sys.exit()

    class Scenes(Enum):
        GAME = Game

    # "self.game.new_scene(self.game.Scenes.GAME)" anywhere in any sprite code to start a new scene
    def new_scene(self, scene_class: Scene, **kwargs) -> None:
        self.scene.kill()
        self.scene = scene_class.value(self)
        self.scene.setup(**kwargs)

    # Switch to an already existing scene object (ex. from pause screen back to main game where game data is saved)
    def switch_scene(self, scene: Scene) -> None:
        self.scene.kill()
        self.scene = scene
        self.scene.start()