from model.model import Model

model = Model()
model.buildGraph(1980)
print(model.getNumNodes())
print(model.getNumEdges())
for nodo in model._graph.nodes:
    if model._graph.degree(nodo) != 0:
        print(nodo)
        print(model._graph.degree(nodo))
model.getCompConnesse()


