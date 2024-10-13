import numpy as np
import qiskit

from qiskit import QuantumCircuit



class Walk:
    """
    A base class to represent a general walk (classical or quantum).
    
    Attributes:
    -----------
    size : int
        The number of positions in the walking space.
    j : int
        Number of runs where a slot machine is tested.
    k : int
        Number of iterations for averaging.
    steps : int
        Number of steps the walker takes in each iteration.
    initial_theta : float
        Initial theta value for updating the walking space.
    pos_index : int
        Current position of the walker.
    ground_truth : list
        Ground truth probabilities for the slot machine at each position.
    emp_truth : list
        Empirical probabilities based on walker's experience.
    happiness : list
        Cumulative count of successful slot machine pulls.
    hits : list
        Cumulative count of slot machine pulls at each position.
    walking_space : list
        Array representing theta values for each position.
    init_state : str
        Initial state of the walker in binary form.
    kwargs : dict
        Additional arguments passed from subclasses.
    """
    def __init__(self, size, initial_pos, initial_theta, steps, j, k, gt, **kwargs):
        """
        Initialize the Walk with common attributes.

        Parameters:
        -----------
        size : int
            Number of positions in the walking space.
        initial_pos : int
            Initial position of the walker.
        initial_theta : float
            Initial theta for the walk space modification.
        steps : int
            Number of steps to take in each walk.
        j : int
            Number of slot machine trials per walk.
        k : int
            Number of iterations for averaging.
        gt : list
            Ground truth probabilities for each position.
        kwargs : dict
            Additional parameters for specific subclasses (e.g., quantum circuits).
        """
        self.size = size
        self.j = j
        self.k = k
        self.steps = steps
        self.initial_theta = initial_theta
        self.pos_index = initial_pos
        self.ground_truth = gt
        self.emp_truth = [0.0 for _ in range(size)]
        self.happiness = [0 for _ in range(self.size)]
        self.hits = [0 for _ in range(self.size)]
        self.walking_space = [initial_theta for _ in range(size)]
        self.init_state = str(bin(initial_pos)[2:].zfill(5))
        self.kwargs = kwargs  # Store additional arguments for subclass logic

    def slotMachine(self):
        """
        Simulate pulling a slot machine at the current position.
        The result is based on the ground truth probability for that position.

        Returns:
        --------
        int
            1 if successful, 0 otherwise.
        """
        x = np.random.binomial(n=1, p=self.ground_truth[self.pos_index])
        return x

    def explore(self):
        """
        Explore the walking space by running multiple slot machine trials,
        updating empirical truths, and adjusting walking space.
        """
        a = 5
        b = 6
        for i in range(self.j):
            self.walk()  # walking logic differs for classical and quantum
            x = self.slotMachine()
            if x:
                self.happiness[self.pos_index] += 1
            self.hits[self.pos_index] += 1
            self.emp_truth[self.pos_index] = self.happiness[self.pos_index] / self.hits[self.pos_index]

            # Update walking space based on empirical truth
            for j in range(self.size):
                self.walking_space[j] = self.initial_theta * np.exp(-a * np.power(self.emp_truth[j], b))
            self.pos_index = np.array(self.emp_truth).argmax()
            self.init_state = str(bin(self.pos_index)[2:].zfill(5))

    def walk(self):
        """
        Placeholder method to define walking logic.
        This will be implemented by subclasses.
        """
        pass

    def main(self):
        """
        Main function to execute the explore method and return total happiness.

        Returns:
        --------
        int
            Total happiness (sum of successful slot machine pulls).
        """
        self.explore()
        return sum(self.happiness)
class ClassicalWalk(Walk):
    """
    A subclass of Walk representing a classical random walk.
    
    Methods:
    --------
    walk():
        Implements classical random walk logic using simple coin tosses.
    """

    def walk(self):
        """
        Implements classical random walk logic based on coin toss.
        If the coin toss result is greater than 0.5, move right, else move left.
        """
        for _ in range(self.steps):
            if np.random.rand() > 0.5:
                self.pos_index = (self.pos_index + 1) % self.size  # Move right
            else:
                self.pos_index = (self.pos_index - 1) % self.size  # Move left
        # No quantum circuit involved here

class QuantumWalk(Walk):
    """
    A subclass of Walk representing a quantum walk using Qiskit.
    
    Methods:
    --------
    incremment_gate():
        Creates a quantum increment gate for the walk.
    decrement_two_coins():
        Creates a quantum decrement gate for the walk.
    walk():
        Implements the quantum walk logic using Qiskit circuits.
    """
    def __init__(self, size, initial_pos, initial_theta, steps, j, k, gt, **kwargs):
        """
        Initialize the QuantumWalk.

        Parameters:
        -----------
        size : int
            Number of positions in the walking space.
        initial_pos : int
            Initial position of the walker.
        initial_theta : float
            Initial theta for the walk space modification.
        steps : int
            Number of steps to take in each walk.
        j : int
            Number of slot machine trials per walk.
        k : int
            Number of iterations for averaging.
        gt : list
            Ground truth probabilities for each position.
        kwargs : dict
            Additional arguments specific to the quantum walk, such as circuit and registers.
        """
        super().__init__(size, initial_pos, initial_theta, steps, j, k, gt, **kwargs)
        self.n = int(np.ceil(np.log2(size)))
        self.q_walk = QuantumCircuit(self.n + 2, self.n)

    def incremment_gate(self):
        """
        Create and return a quantum increment gate.

        Returns:
        --------
        qiskit.circuit.Gate
            A custom quantum increment gate for the walk circuit.
        """
        qc = QuantumCircuit(self.n + 1, name="Inc")
        qc.cx(0, 1)
        qc.ccx(0, 1, 2)
        for i in range(2, self.n + 1):
            qc.mcx([j for j in range(i)], i)
        return qc.to_gate()

    def decrement_two_coins(self):
        """
        Create and return a quantum decrement gate.

        Returns:
        --------
        qiskit.circuit.Gate
            A custom quantum decrement gate for the walk circuit.
        """
        qc = QuantumCircuit(self.n + 2, name="dec")
        for i in range(self.n, 0, -1):
            if i > 1:
                qc.x([j for j in range(2, i + 1)])
                qc.mcx([j for j in range(i + 1)], i + 1)
                qc.x([j for j in range(2, i + 1)])
        qc.ccx(0, 1, 2)
        return qc.to_gate()

    def walk(self):
        """
        Implements the quantum walk logic using Qiskit circuits.

        The walker takes a series of quantum steps, and the position is updated
        based on the quantum measurements.
        """
        self.q_walk.clear()
        self.q_walk.prepare_state(self.init_state,[i+2 for i in range(self.n)])
        for i in range(self.steps): # makes the circuit for steps number of steps
            self.q_walk.u(self.walking_space[self.pos_index],0,0,0)
            self.q_walk.u(self.walking_space[self.pos_index],0,0,1)
            self.q_walk.append(self.incremment_gate(), [i+1 for i in range(self.n+1)])
            self.q_walk.x(1)
            self.q_walk.append(self.decrement_two_coins(), [i for i in range(self.n+2)])
            self.q_walk.x(1)
        for i in range(self.n):
            self.q_walk.measure(i+2,i)
        
    #   ## Simulation of the circuit happens here:
    #   backend = Aer.backends(name = 'qasm_simulator')[0]
    #   result = execute(self.q_walk, backend, shots=1).result().get_counts(self.q_walk)
    #   self.pos_index = int(max(result).replace(" ", ""),2)

