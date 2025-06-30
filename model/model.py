import networkx as nx
from database.DAO import DAO
from model.country import Country


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
        self.addEdges(anno)

    def addEdges(self, anno):
        archi = DAO.getAllEdges(anno)
        for arco in archi:
            oggettoArco_01 = self._idMap[arco[0]]
            oggettoArco_02 = self._idMap[arco[1]]
            self._graph.add_edge(oggettoArco_01, oggettoArco_02)

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def getNodesDegree(self):
        result = []
        for nodo in self._graph.nodes:
            if self._graph.degree(nodo) != 0:
                tuplaInfoNodo = (nodo, self._graph.degree(nodo))
                result.append(tuplaInfoNodo)
        return result

    def getCompConnesse(self):
        numCompConnesse = nx.number_connected_components(self._graph)
        return numCompConnesse

    def getNodesRaggiungibili(self, source: Country):
        bfsTree = nx.bfs_tree(self._graph, source)
        nodi = list(bfsTree.nodes)
        return nodi

    def controlNode(self, source: Country):
        if source in self._graph.nodes:
            return True
        else:
            return False