import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._graph = nx.Graph()

    def buildGraph(self, anno):
        nodi = DAO.getAllNodes(anno)
        self._graph.add_nodes_from(nodi)
        self.addEdges(anno)

    def addEdges(self, anno):
        archi = DAO.getAllEdges(anno)
        self._graph.add_edges_from(archi)

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)