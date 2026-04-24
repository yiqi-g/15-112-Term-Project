from cmu_graphics import *
from cmu_cpcs_utils import *
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
                 name,
                 width, height, 
                 x, y, 
                 onClickFn = None,
                 backgroundColor = 'white', 
                 border = None, 
                 textAlign = 'Center', 
                 font = None, 
                 fontColor = 'black',
                 fontSize = 16): 
        self.name = name
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.onClickFn = onClickFn

        #styling

        self.backgroundColor = backgroundColor
        self.border = border
        self.textAlign = textAlign
        self.font = font if font else 'monospace'
        self.fontColor = fontColor
        self.fontSize = fontSize

    def onClick(self, mouseX, mouseY):
        
        if ((self.x - self.width // 2 <= mouseX) and (mouseX <= self.x + self.width // 2)
            and self.y - self.height // 2 <= mouseY) and (mouseY <= self.y + self.height // 2):
            if self.onClickFn != None:
                self.onClickFn()

    def draw(self):
        drawRect(self.x, self.y, self.width, self.height, fill=self.backgroundColor, 
                 border = self.border, align = 'center')
        drawLabel(self.name, self.x, self.y, fill=self.fontColor, font = self.font, size = self.fontSize)

class UI_Importer(UI_Button): 
    pass
    # def __init__(self):
    #     super().__init__(self):

class UI_DropDown(UI_Button):
    pass

class UI_Window:
    def __init__(self, width, height, backgroundColor) -> None:
        self. width = width
        self.height = height
        self.backgroundColor = backgroundColor

    def __repr__(self):
        return f'window size {self.width} x {self.height}, window color {self.backgroundColor}'