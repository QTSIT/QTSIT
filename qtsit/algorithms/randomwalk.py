"""
Code for random walk algorithms.
"""
import numpy as np


class classical_walk:
    """Classical random walk algorithm.
    """

    def __init__(self,
                 size,
                 initial_pos,
                 steps,
                 j,
                 k,
                 ground_truth,
                 toss_val: float = 0.1) -> None:
        self.size = size
        self.j = j
        self.k = k
        self.result = ""
        self.steps = steps
        self.toss_val = toss_val
        self.walking_space = []
        for _ in range(size):
            self.walking_space.append([0.5, 0, 0.5])

        self.pos: list[float] = []
        self.pos_index = initial_pos
        self.ground_truth = ground_truth
        self.emp_truth = []
        for _ in range(size):
            self.emp_truth.append(0.0)
        self.happiness = [0 for i in range(self.size)]
        self.hits = [0 for i in range(self.size)]
        self.cumsum = 0

    def goto_pos(self) -> None:
        """Go to the position.
        """
        self.pos = self.walking_space[self.pos_index]

    def coin_toss(self) -> None:
        """Coin toss function.
        """
        self.toss_val = np.random.rand()

        if (0 <= self.toss_val <= self.pos[0]):
            self.result = "BACK"
        if (self.pos[0] < self.toss_val <= self.pos[0] + self.pos[1]):
            self.result = "STAY"
        if (self.pos[0] + self.pos[1] < self.toss_val <= 1):
            self.result = "FORWARD"

    def one_walk(self) -> None:
        """One walk function.
        """
        if (self.pos_index == self.size - 1):
            if (self.result == "BACK"):
                self.pos_index = self.pos_index - 1

            if (self.result == "FORWARD"):
                self.pos_index = 0

        elif (self.pos_index == 0):
            if (self.result == "BACK"):
                self.pos_index = self.size - 1

            if (self.result == "FORWARD"):
                self.pos_index = self.pos_index + 1

        else:
            if (self.result == "BACK"):
                self.pos_index = self.pos_index - 1

            if (self.result == "FORWARD"):
                self.pos_index = self.pos_index + 1

    def walkk(self):
        for _ in range(self.steps):
            self.goto_pos()
            self.coin_toss()
            self.one_walk()

    def slotMachine(self):
        x = np.random.binomial(n=1, p=self.ground_truth[self.pos_index])
        return x

    def explore(self):
        a = 9
        b = 6
        for i in range(self.j):
            self.walkk()
            x = self.slotMachine()
            if (x):
                self.happiness[self.pos_index] += 1
            self.hits[self.pos_index] += 1
            self.emp_truth[self.pos_index] = self.happiness[
                self.pos_index] / self.hits[self.pos_index]
            for j in range(self.size):

                self.walking_space[j][0] = 0.5 * np.exp(
                    -a * np.power(self.emp_truth[j], b))
                self.walking_space[j][1] = 1 - 2 * self.walking_space[j][0]
                self.walking_space[j][2] = self.walking_space[j][0]
            self.pos_index = np.array(self.emp_truth).argmax()

    def main(self):
        """Main function.
        """
        self.explore()

        return sum(self.happiness)


class quantum_walk():
    """Quantum random walk algorithm.
    """

    def __init__(self, graph):
        super().__init__(graph)


class groundtruth:
    """Groundtruth class for the random walk algorithms.
    """

    def __init__(self) -> None:
        pass
