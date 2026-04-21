from cmu_graphics import *
from cmu_cpcs_utils import *
from controller import *
import math

def redrawAll(app):
    newWindow = Window(1920, 1080, 'black')
    convertButton = UI_Button()
    imageWidth, imageHeight = setImageSize(app, app.trialImage)
    convertButton.draw()
    drawImage(app.trialImage, app.width / 2, app.height / 2, width = imageWidth, height = imageHeight, align='center')


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


# class UI_Button:
#     def __init__(self, name, width, height, x, y, backgroundColor = 'black', 
#                  border = None, textAlign = 'Center', font = None, fontSize = 16) -> None:
#         self.name = name
#         self.width = width
#         self.height = height
#         self.x = x
#         self.y = y

#         #styling

#         self.backgroundColor = backgroundColor
#         self.border = border
#         self.textAlign = textAlign
#         self.font = font if font else 'monospace'
#         self.fontSize = fontSize