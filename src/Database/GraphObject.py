from typing import Dict


class GraphObject:

    # Basic attributes
    node_count: int
    edge_count: int

    # Graph attributes
    convergence_rate: float
    energy_cost: float
    total_edge_cost: float

    diameter: int
    eccentricity_average: float

    # Graph structure
    graph_nodes: Dict
    graph_edges: Dict
    eccentricity_distribution: Dict
