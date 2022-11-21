from model import RoombaModel, Roomba, ObstacleAgent, Floor
from mesa.visualization.modules import CanvasGrid, ChartModule, PieChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

COLORS = {'Clean': "blue", 'Dirty': "black"}


def roombaPortrayal(agent):
    if agent is None:
        return

    if (isinstance(agent, Floor)):
        portrayal = {
            "Shape": "rect",
            "w": 0.7,
            "h": 0.7,
            "Color": COLORS[agent.condition],
            "Layer": 0,
            "Filled": "true"
        }

    if (isinstance(agent, Roomba)):
        portrayal = {
            "Shape": "circle",
            "Color": "red",
            "Layer": 1,
            "Filled": "true",
            "r": 0.7
        }

    if (isinstance(agent, ObstacleAgent)):
        portrayal = {
            "Shape": "circle",
            "Color": "grey",
            "Layer": 2,
            "Filled": "true",
            "r": 0.1
        }
    return portrayal


grid = CanvasGrid(roombaPortrayal, 10, 10, 500, 500)

floor_chart = ChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)

floor_pie_chart = PieChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)

server = ModularServer(RoombaModel,
                       [grid, floor_pie_chart, floor_chart],
                       "Roomba Cleaning",
                       {"N": UserSettableParameter("number", "Roomba Number: ", value=5), "ancho": 10, "alto": 10,
                        "percentage": UserSettableParameter("slider", "Floor Percentage", 0.5, 0.01, 1.0, 0.1),
                        "maxTime": UserSettableParameter("number", "Maximum number of steps", value=200)
                        })

server.port = 8521
server.launch()