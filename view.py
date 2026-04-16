# from cmu_graphics import *
# from cmu_cpcs_utils import *
# import math

class Window:
    def __init__(self, width, height, backgroundColor) -> None:
        self. width = width
        self.height = height
        self.backgroundColor = backgroundColor

    def __repr__(self):
        return f'window size {self.width} x {self.height}, window color {self.backgroundColor}'
    

class UI_Slider:
    def __init__(self, name, lowest, highest) -> None:
        self.name = name
        self.lowest = lowest
        self.highest = highest


def redrawAll(app):
    newWindow = Window(400, 400, 'black')
    app.setFill(newWindow.backgroundColor)