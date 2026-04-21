from cmu_graphics import *
from cmu_cpcs_utils import *
from controller import *
from converter import *
import math


#these properties are referenced from w3 school's css classes
class UI_Slider:
    def __init__(self, name, lowest, highest) -> None:
        self.name = name
        self.lowest = lowest
        self.highest = highest

class UI_Button:
    def __init__(self, 
                 action, 
                 width, height, 
                 x, y, 
                 opacity = 100,
                 backgroundColor = 'black', 
                 border = None, 
                 textAlign = 'Center', 
                 font = None, 
                 fontColor = 'white',
                 fontSize = 16) -> None:
        
        self.action = action.upper()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.opacity = opacity
        #styling

        self.backgroundColor = backgroundColor
        self.border = border
        self.textAlign = textAlign
        self.font = font if font else 'monospace'
        self.fontColor = fontColor
        self.fontSize = fontSize

        app.uiElments.append(self)

    def onClick(self, app):
        if self.action == 'CONVERT':
            getNewImage(app.trialImage)
            

    def draw(self):
        drawRect(self.x, self.y, self.width, self.height, fill=self.backgroundColor, border = self.border, opacity = self.opacity, align = 'center')
        drawLabel(self.action, self.x, self.y, fill=self.fontColor, font = self.font, size = self.fontSize)

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