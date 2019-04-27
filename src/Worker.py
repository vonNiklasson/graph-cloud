from extended_networkx_tools import Creator
from simulated_annealing import Annealing2
import networkx


class Worker:

    graph: networkx.Graph
    annealing: Annealing2

    def __init__(self, node_count: int, optimizer: str = 'combined'):
        # Create graph
        self.graph = Creator.from_random(node_count)
        # Create annealing function
        self.annealing = Annealing2(self.graph)
        self.annealing.set_optimization_parameter(optimizer)

    def solve(self):
        self.graph = self.annealing.solve(False)
        return self.graph
