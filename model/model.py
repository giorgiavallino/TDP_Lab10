import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._stati = DAO.getAllCountry()
        self._idMap = {}
        for stato in self._stati:
            self._idMap[stato.CCode] = stato

    def buildGraph(self, anno):
        nodi = DAO.getAllNodes(anno)
        for nodo in nodi:
            oggettoNodo = self._idMap[nodo.state1no]
            if not self._graph.has_node(oggettoNodo):
                self._graph.add_node(oggettoNodo)
                print(self._graph.nodes)

    def addEdges(self, anno):
        archi = DAO.getAllEdges(anno)
        self._graph.add_edges_from(archi)

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)