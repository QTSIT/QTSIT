"""
Code for random walk algorithms.
"""

import random


# abstract class walk - will be used in classical walk and quantum walk
class walk:
    """Abstract class for random walk algorithms.
    """

    def __init__(self, graph):
        self.graph = graph
        self.current_node = random.choice(graph.nodes())
        self.visited = [self.current_node]
        self.steps = 0

    def walk(self, steps):
        for i in range(steps):
            self.step()

    def step(self):
        self.steps += 1
        self.current_node = self.next_node()
        self.visited.append(self.current_node)

    def next_node(self):
        pass

    def get_visited(self):
        return


class classical_walk(walk):
    """Classical random walk algorithm.
    """

    def __init__(self, graph):
        super().__init__(graph)

    def next_node(self):
        return random.choice(list(self.graph.neighbors(self.current_node)))


class quantum_walk(walk):
    """Quantum random walk algorithm.
    """

    def __init__(self, graph):
        super().__init__(graph)

    def next_node(self):
        return random.choice(list(self.graph.neighbors(self.current_node)))


class groundtruth:
    """Groundtruth class for the random walk algorithms.
    """

    def __init__(self) -> None:
        pass
