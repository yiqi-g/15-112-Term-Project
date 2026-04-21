from cmu_graphics import *
from cmu_cpcs_utils import *
from controller import *
from components import *
import math

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
        
            