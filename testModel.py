from model.country import Country
from model.model import Model

country = Country("CAN", 20, "Canada")
model = Model()
model.buildGraph(1980)
print(model.getRaggiungibili(country))


