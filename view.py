from cmu_graphics import *
from components import *
from PIL import Image
import math

def onAppStart(app):
    app.setMaxShapeCount(100000000000)
    app.font = 'monopspace'
    app.fontSize = 6
    app.fontColor = 'white'
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

def redrawAll(app):
    imageWidth, imageHeight = setImageSize(app, app.trialImage)
    if app.asciiArray == []:
        drawImage(app.trialImage, app.width / 2, app.height / 2, width = imageWidth, 
                height = imageHeight, align='center')
    else:
        drawAsciiImage(app.asciiArray, imageWidth, imageHeight)
        print(app.asciiArray[0])
    app.convertButton.draw()

    print(len(app.asciiArray))

def setImageSize(app, image):
    imageWidth, imageHeight = getImageSize(image)
    isPortrait = imageHeight > imageWidth
    if (imageHeight >= (app.height * 0.75)) or (imageWidth >= (app.width * 0.75)):
        if isPortrait:
            maxHeight = app.height * 0.75
            maxWidth = (imageWidth / imageHeight) * maxHeight
        else:
            maxWidth = app.width * 0.75
            maxHeight = (imageHeight / imageWidth) * maxWidth
        return maxWidth, maxHeight
    return imageWidth, imageHeight


# This function is written with the assistance of Claude, parts including charWidth and drawLabel parameters. Everything else is written by hand.
def drawAsciiImage(asciiArray, imageWidth, imageHeight):
    rows, cols = len(asciiArray), len(asciiArray[0])
    startingX = app.width / 2 - imageWidth / 2
    startingY = app.height / 2 - imageHeight / 2
    charWidth = (app.fontSize / 2) * cols
    charHeight = app.fontSize
    for row in range(rows):
        rowString = ''.join(asciiArray[row])
        print(startingX, startingY)
        drawLabel(rowString, startingX, 
                    startingY + row * charHeight, 
                    font = app.font, fill = 'white',
                    size = app.fontSize)
        
            