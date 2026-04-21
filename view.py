from cmu_graphics import *
from cmu_cpcs_utils import *
from controller import *
from components import *
import math

def redrawAll(app):
    convertButton = UI_Button('convert', 150, 50, app.width / 2, app.height / 2 + 400, backgroundColor='black')
    imageWidth, imageHeight = setImageSize(app, app.trialImage)
    drawImage(app.trialImage, app.width / 2, app.height / 2, width = imageWidth, height = imageHeight, align='center')
    convertButton.draw()

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