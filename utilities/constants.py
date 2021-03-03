WIDTH = 480
HEIGHT = 480
FPS = 120
RANDOM_AI = True
NNET_PLAYER = 2
VISUAL = False

# Neural Network parameters
INPUTS = 9
HIDDEN_LAYERS = [36, 36]
OUTPUTS = 9
ACTIVATION = 'ReLU'
OUTPUT_ACTIVATION = 'Linear'

# Reward Policy
REWARD_BAD_CHOICE = -100
REWARD_LOST_GAME = -500
REWARD_WON_GAME = 500
REWARD_TIE_GAME = 100

MEMORY_CAPACITY = 100000
BATCH_SIZE = 64
GAMMA = 0.99
TARGET_UPDATE = 10
LEARNING_RATE = 0.001
NUM_EPISODES = 1000

# epsilon greedy strategy
eSTART = 1
eEND = 0.01
eDECAY = 0.0001
# eSTART = 0
# eEND = 0
# eDECAY = 0

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (185, 185, 185)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
