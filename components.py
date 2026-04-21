from cmu_graphics import *
from cmu_cpcs_utils import *
from controller import *
import math


#these properties are referenced from w3 school's css classes
class UI_Slider:
    def __init__(self, name, lowest, highest) -> None:
        self.name = name
        self.lowest = lowest
        self.highest = highest

class UI_Button:
    def __init__(self, name, width, height, x, y, backgroundColor = 'black', 
                 border = None, textAlign = 'Center', font = None, fontSize = 16) -> None:
        self.name = name
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        #styling

        self.backgroundColor = backgroundColor
        self.border = border
        self.textAlign = textAlign
        self.font = font if font else 'monospace'
        self.fontSize = fontSize

    def onClick(self):
        pass

    def drawButton(self):
        pass

class UI_Importer: 
    pass

class UI_DropDown(UI_Button):
    pass

class UI_Window:
    def __init__(self, width, height, backgroundColor) -> None:
        self. width = width
        self.height = height
        self.backgroundColor = backgroundColor

    def __repr__(self):
        return f'window size {self.width} x {self.height}, window color {self.backgroundColor}'