from converter import *

def onAppStart(app):
    app.font = 'monopspace'
    app.fontSize = 14
    app.fontColor = 'white'
    app.width = 1920
    app.height = 1080
    app.background = 'black'

    app.trialImage = 'CleanShot 2026-04-20 at 15.48.40@2x.png'

    app.images = []
    app.uiElments = []

    convertButton = UI_Button('convert', 150, 50, app.width / 2, app.height / 2 + 400, backgroundColor='black')

def onMousePress(app, mouseX, mouseY):
    for element in app.uiElements:
        if isClicked(element, mouseX, mouseY):
            element.onClick()

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