import numpy as np

from board import board
from agent import agent
from zombie import zombie


class PacManZ(board, agent, zombie):
    def __init__(self, height, width, n_zombie, n_obstcale, n_shot) -> None:
        self.initial_n_zombie = n_zombie
        self.n_zombie = n_zombie
        self.n_played_game = 0
        self.board = board(self, height, width, n_obstcale, n_shot)
        self.agent = agent(self)
        self.zombie = [zombie(self) for i in range(n_zombie)]

        self.board.generate_board()
        self.agent.generate_agent()
        for i in range(n_zombie):
            self.zombie[i].generate_zombie()

    def play(self):
        while True:
            print(self.agent.move_agent())
            self.board.print_board()
            # wait for key
            input()

    def reset(self):
        self.board.generate_board()
        self.agent.generate_agent()
        self.n_zombie = self.initial_n_zombie
        self.zombie = [zombie(self) for i in range(self.n_zombie)]
        for i in range(self.n_zombie):
            self.zombie[i].generate_zombie()
        self.board.has_vaccine = False
        self.agent.iteration = 0