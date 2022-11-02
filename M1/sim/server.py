from mesa.visualization.modules import  CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from model import GameOfLife

colors = {"Alive": "#000000", "Dead": "#FFFFFF"}

def lifeGrid_portrayal(cell):
    if cell is None:
        return

    portrayal = {"Shape": "rect", "w": 0.7, "h": 0.7, "Filled": "true", "Layer": 0}

    (x, y) = cell.pos

    portrayal["x"] = x
    portrayal["y"] = y
    portrayal["Color"] = colors[cell.condition]

    return portrayal

canvas_element = CanvasGrid(lifeGrid_portrayal, 100, 100, 500, 500)

model_param = {"height": 100, "width": 100, "density":UserSettableParameter("slider", "Cell density", 0.04, 0.01, 1.0, 0.1)}

server = ModularServer(GameOfLife, [canvas_element], "Conway's Game of Life", model_param)

server.launch()