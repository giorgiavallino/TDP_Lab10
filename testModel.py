from model.model import Model

model = Model()
model.buildGraph(1816)
print(model._graph.nodes)
print(model._graph.edges)