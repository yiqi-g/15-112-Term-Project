from cmu_graphics import *
from components import *
from PIL import Image
import math


def onAppStart(app):
    
    app.setMaxShapeCount(100000000000)
    app.font = 'monopspace'
    app.fontSize = 4
    app.fontColor = 'black'
    app.background = 'white'

    app.charWidth = app.fontSize / 2
    app.charHeight = app.fontSize

    app.imageWidth = 0
    app.imageHeight = 0

    app.uiElements = []
    app.asciiArray = []

    initializeButtons(app)
    syncImages(app, '5da360c98b9af0ad709fe18606992229.jpg')

def syncImages(app, filePath: str):
    app.PILImage = Image.open(filePath)
    app.CMUImage = filePath

def initializeButtons(app):
    
    def convertButtonClick():
        app.imageArray = getNewImage(app, app.PILImage, inverse = False)

    # importButton = UI_Button('import', 150, 50, 
    #                         app.width / 2 - 200, app.height / 2 + 400, None,
    #                         backgroundColor='white')

    convertButton = UI_Button('convert', 
                              150, 50, app.width / 2, app.height / 2 + 400, convertButtonClick,backgroundColor='white')
    
    app.uiElements.extend([convertButton])

def onMousePress(app, mouseX, mouseY):
    for element in app.uiElements:
        element.onClick(mouseX, mouseY)

def onKeyPress(app, key):
    if key == 'i':
        filepath = app.getTextInput('enter an image file path:' )
        if isinstance(filepath, str):
            syncImages(app, filepath)
            app.asciiArray = []
            
def onMouseDrag(app, mouseX, mouseY):
    pass

def redrawAll(app):
    imageWidth, imageHeight = setImageSize(app, app.CMUImage)
    if app.asciiArray == []:
        drawImage(app.CMUImage, app.width // 2, app.height // 2, width = imageWidth, 
            height = imageHeight, align='center')
    else:
        drawAsciiImage(app, app.asciiArray, imageWidth, imageHeight)
    
    for UI in app.uiElements:
        UI.draw()

def setImageSize(app, image):
    imageWidth, imageHeight = getImageSize(image)
    isPortrait = imageHeight > imageWidth
    if (imageHeight >= (app.height * 0.75)) or (imageWidth >= (app.width * 0.75)):
        if isPortrait:
            maxHeight = app.height * 0.75
            maxWidth = (app.imageWidth / app.imageHeight) * maxHeight
        else:
            maxWidth = app.width * 0.75
            maxHeight = (app.imageHeight / app.imageWidth) * maxWidth
        return maxWidth, maxHeight
    else:
        return imageWidth, imageHeight

# This function is written with the assistance of Claude, parts including charWidth and drawLabel parameters. Everything else is written by hand.
def drawAsciiImage(app, asciiArray, imageWidth, imageHeight):
    rows, cols = len(asciiArray), len(asciiArray[0])
    startingX = app.width // 2 - imageWidth // 2
    startingY = app.height // 2 - imageHeight // 2
    charWidth = (app.fontSize / 2) * cols
    charHeight = app.fontSize
    for row in range(rows):
        rowString = ''.join(asciiArray[row])
        drawLabel(rowString, startingX, 
                    startingY + row * charHeight, 
                    font = app.font, fill = 'black',
                    size = app.fontSize, align = 'left')

def main():
    runApp(width=1280, height=720)

main()