from converter import *
from components import *
from PIL import Image

def onAppStart(app):
    app.setMaxShapeCount(100000000000)
    app.font = 'monopspace'
    app.fontSize = 4
    app.fontColor = 'white'
    app.width = 1920
    app.height = 1080
    app.background = 'black'

    app.charWidth = app.fontSize / 2
    app.charHeight = app.fontSize

    app.trialImage = '5da360c98b9af0ad709fe18606992229.jpg'

    app.images = []
    app.uiElements = []
    app.asciiArray = []

    app.convertButton = UI_Button('convert', 150, 50, app.width / 2, app.height / 2 + 400, backgroundColor='black')

def onMousePress(app, mouseX, mouseY):
    for element in app.uiElements:
        if isClicked(element, mouseX, mouseY):
            element.onClick(app)

def onMouseDrag(app, mouseX, mouseY):
    pass

def isClicked(element, mouseX, mouseY):
    if isinstance(element, UI_Button):
        return ((element.x - element.width // 2 <= mouseX) and (mouseX <= element.x + element.width // 2)
            and element.y - element.height // 2 <= mouseY) and (mouseY <= element.y + element.height // 2)
    elif isinstance(element, UI_Slider):
        pass
    elif isinstance(element, UI_Importer):
        # open os and allow image upload
        pass