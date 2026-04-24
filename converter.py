import os, sys #main os driver
from PIL import Image #this is the pillow module for image recognition
import math


def convertToAscii(pixel, inverse = False):
    # this dictionary is written by claude
    CHAR_SETS = {
        'STANDARD':   '@#S%?*+;:,. ',
        'BLOCKS':     '█▓▒░ ',
        'BINARY':     '10 ',
        'DETAILED':   '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\'"^`\'. ',
        'MINIMAL':    '@: ',
        'ALPHABETIC': 'WMBASTHINKCO ',
        'NUMERIC':    '8642013 ',
        'MATH':       '∑∫≈±×÷=+- ',
        'SYMBOLS':    '#@&$%!?;:,. ',
    }

    charsKey = 'NUMERIC' #place holder for dropdown menu
    chars = list(CHAR_SETS[charsKey])

    charIndex = math.floor((pixel / 255) * (len(chars) - 1)) #get it's position in the ascii art in accordance to grayscale value
    inverseCharIndex = len(chars) - 1 - charIndex #get the opposite
    if inverse:
        currChar = chars[inverseCharIndex]
    else:
        currChar = chars[charIndex]
    return currChar


def getNewImage(app, image, inverse = False):
    app.asciiArray = []
    image, imageWidth, imageHeight = modifyImage(app, image)
    for row in range(imageHeight):
        rowList = []
        for col in range(imageWidth):
            currPixel = image.getpixel((col, row))
            rowList.append(convertToAscii(currPixel, inverse = inverse) * 2) 
            #double it up, cuz character width is smaller than the height
        app.asciiArray.append(rowList)
        
    # img = Image.fromarray(app.asciiArray)
    # img.show()
    # img.save('output.png')
    print("done!")


def modifyImage(app, image):
    shunkenSize = 4
    imageWidth, imageHeight = app.PILImage.size
    image = image.resize((imageWidth // shunkenSize, imageHeight // shunkenSize)).convert('L')
    # image = image.convert('L')
    imageWidth, imageHeight = image.size
    return image, imageWidth, imageHeight