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
    def __init__(self, name, width, height, backgroundColor = 'black', border = None, textAlign = 'Center', font = app.font, fontSize = 16) -> None:
        self.name = name
        self.width = width
        self.height = height
        self.backgroundColor = backgroundColor
        self.border = border
        self.textAlign = textAlign
        self.font = font
        self.fontSize = fontSize

    def onClick(self):
        
class UI_Importer: 


class UI_DropDown(UI_Button):


class UI_Window:
    def __init__(self, width, height, backgroundColor) -> None:
        self. width = width
        self.height = height
        self.backgroundColor = backgroundColor

    def __repr__(self):
        return f'window size {self.width} x {self.height}, window color {self.backgroundColor}'