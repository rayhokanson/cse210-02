from constants import *
from game.directing.director import Director
from game.directing.scene_manager1 import SceneManager


def main():
    director = Director(SceneManager.VIDEO_SERVICE)
    director.start_game()

if __name__ == "__main__":
    main()