from mesa import Agent

class LifeCell(Agent):
    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.pos = pos
        self.condition = "Dead"

    def step(self):

        neighborCount = 0

        for neighbor in self.model.grid.neighbor_iter(self.pos):
            if neighbor.condition == "Alive":
                neighborCount += 1

        #For a space that is populated:
        if self.condition == "Alive":
            #Each cell with one or no neighbors dies, as if by solitude.
            #Each cell with four or more neighbors dies, as if by overpopulation.
            if neighborCount < 2  or neighborCount > 3:
                self.condition = "Dead"
            #Each cell with two or three neighbors survives.
            elif neighborCount == 2 or neighborCount == 3:
                self.condition = "Alive"
        
        #For a space that is empty or unpopulated
        if self.condition == "Dead":
            #Each cell with three neighbors becomes populated.
            if neighborCount == 3:
                self.condition = "Alive"
    
    def advance(self):
        return super().advance()