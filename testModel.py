from model.model import Model

model = Model()
model.buildGraph(1816)
print(model._idMap)
print(model.getNumNodes())