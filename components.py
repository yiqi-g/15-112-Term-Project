from cmu_graphics import *
from cmu_cpcs_utils import *
from converter import *
import math


#these properties are referenced from w3 school's css classes
class UI_Button:
    def __init__(self, 
                 name,
                 width, height, 
                 x, y, 
                 onClickFn = None,
                 backgroundColor = 'white', 
                 border = None, 
                 borderWidth = 1,
                 opacity = 100,
                 align = 'center', 
                 font = None, 
                 fontColor = 'black',
                 fontSize = 16): 
        self.name = name
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.onClickFn = onClickFn
        self.opacity = opacity

        #styling

        self.backgroundColor = backgroundColor
        self.border = border
        self.borderWidth = borderWidth
        self.align = align
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
                 border = self.border, borderWidth = self.borderWidth, align = 'center', opacity = self.opacity)
        drawLabel(self.name, self.x, self.y, fill=self.fontColor, font = self.font, size = self.fontSize)

class UI_sidebar (UI_Button):
    def __init__(self, name, width, height, x = 0, y = 0, onClickFn=None,
                 backgroundColor='white', border=None, borderWidth = 1, opacity = 50, align='center',
                 fontColor='black', fontSize=16):
        super().__init__(name, width, height, x, y, onClickFn,
                         backgroundColor, border, borderWidth, opacity, align, None,
                         fontColor, fontSize)
        
    def draw(self, app):
        drawRect(self.x, self.y, self.width, self.height, fill=self.backgroundColor, border = self.border,      borderWidth = self.borderWidth, opacity = self.opacity)
        for button in app.uiElements:
            if isinstance(button, UI_Button):
                button.draw()

    
class UI_Importer(UI_Button): 
    pass
    # def __init__(self):
    #     super().__init__(self):
