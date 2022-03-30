from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Pong"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "../Pong/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "../Pong/assets/sounds/boing.wav"
WELCOME_SOUND = "../Pong/assets/sounds/start.wav"
OVER_SOUND = "../Pong/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
# IN_PLAY = 2
# GAME_OVER = 3
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
# LEVEL_FILE = "../Pong/assets/data/level-{:03}.txt"
# BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
SCORE2_MARGIN = 150
# LIVES_GROUP = "lives"
# LIVES_FORMAT = "LIVES: {}"
SCORE1_GROUP = "score1"
SCORE2_GROUP = "score2"
SCORE1_FORMAT = "SCORE1: {}"
SCORE2_FORMAT = "SCORE2: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "../Pong/assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# RACKET1
RACKET1_GROUP = "racket1"
RACKET1_IMAGES = [f"../Pong/assets/images/{n:03}.png" for n in range(103, 106)]
RACKET1_WIDTH = 28 # 106
RACKET1_HEIGHT = 106 # 28
RACKET1_RATE = 6
RACKET1_VELOCITY = 7

# RACKET2
RACKET2_GROUP = "racket2"
RACKET2_IMAGES = [f"../Pong/assets/images/{n:03}.png" for n in range(106, 109)]
RACKET2_WIDTH = 28 # 106
RACKET2_HEIGHT = 106 # 28
RACKET2_RATE = 6
RACKET2_VELOCITY = 7

# BRICK
BRICK_GROUP = "bricks"
BRICK_IMAGES = {
    "b": [f"../Pong/assets/images/{i:03}.png" for i in range(10,19)],
    "g": [f"../Pong/assets/images/{i:03}.png" for i in range(20,29)],
    "p": [f"../Pong/assets/images/{i:03}.png" for i in range(30,39)],
    "y": [f"../Pong/assets/images/{i:03}.png" for i in range(40,49)]
}
BRICK_WIDTH = 80
BRICK_HEIGHT = 28
BRICK_DELAY = 0.5
BRICK_RATE = 4
BRICK_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"