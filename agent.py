import numpy as np
import random
import Neural_Network as nn
from collections import namedtuple
import math
import constants as c


class Agent:
    def __init__(self, inputs, hidden_layers, outputs):
        self.PolicyNetwork = nn.NeuralNetwork(inputs, hidden_layers, outputs)
        self.TargetNetwork = nn.NeuralNetwork(inputs, hidden_layers, outputs)
        self.state = []
        self.action = 0
        self.reward = 0
        self.next_state = []
        self.adversary = 2
        self.NNet_player = 1
        self.current_step = 0

    def play(self, previous_turn, game):
        inputs = game.state
        inputs = inputs.reshape(9)
        results = self.PolicyNetwork.forward_propagation(inputs)
        results = results[0]
        self.state = game.state
        action, row, col = self.eGreedyStrategy(results, game)
        self.action = action
        termination_state, sprite_params = game.new_play(row, col)
        self.reward = self.calculate_reward(previous_turn, game.turn, game.winner)
        self.next_state = game.state
        return termination_state, sprite_params

    def eGreedyStrategy(self, results, game):
        exploration_rate = self.get_exploration_rate()
        self.current_step += 1
        # Exploration V.S Exploitation
        if np.random.rand() < exploration_rate:
            action = np.random.choice(c.OUTPUTS)
            row, col = self.split_rowcol(action)
        else:
            if np.max(results) > 0:
                action = np.argmax(results)
                row, col = self.split_rowcol(action)
                results[action] = 0
            else:
                empty_cells = np.where(game.state == 0)
                choice = random.choice(range(len(empty_cells[0])))
                col = empty_cells[1][choice]
                row = empty_cells[0][choice]
                action = self.combine_rowcol(row, col)
        return action, row, col

    def get_exploration_rate(self):
        return c.eEND + (c.eSTART - c.eEND) * \
            math.exp(-1. * self.current_step * c.eDECAY)

    @staticmethod
    def split_rowcol(action):
        row = math.floor(action / 3)
        col = action % 3
        return row, col

    @staticmethod
    def combine_rowcol(row, col):
        action = row * 3 + col
        return action

    def calculate_reward(self, previous_turn, turn, winner):
        if winner == 0:
            if previous_turn == turn:
                return c.REWARD_BAD_CHOICE
            return 0
        elif winner == self.adversary:
            return c.REWARD_LOST_GAME
        elif winner == self.NNet_player:
            return c.REWARD_WON_GAME
        return 0

    def train_NNet(self, replay_memory):
        self.PolicyNetwork.RL_train(replay_memory)
        self.current_step = 0
