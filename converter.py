import os, sys #main os driver
from PIL import Image #this is the pillow module for image recognition
import math
# import tkinter as tk
# from tkinter import filedialog

image = Image.open("5da360c98b9af0ad709fe18606992229.jpg")
#open and turn grayscale


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

    charsKey = 'DETAILED' #place holder for dropdown menu
    chars = list(CHAR_SETS[charsKey])

    charIndex = math.floor((pixel / 255) * (len(chars) - 1)) #get it's position in the ascii art in accordance to grayscale value
    inverseCharIndex = len(chars) - 1 - charIndex #get the opposite
    if inverse:
        currChar = chars[inverseCharIndex]
    else:
        currChar = chars[charIndex]
    return currChar


def getNewImage(app, image, inverse = False):
    image = Image.open(image)
    width, height = image.size
    image = image.resize((width // 4, height // 4))
    width, height = image.size
    image = image.convert('L')
    app.asciiArray = []
    for row in range(height):
        rowList = []
        for col in range(width):
            currPixel = image.getpixel((col, row))
            rowList.append(convertToAscii(currPixel, inverse = inverse) * 2) 
            #double it up, cuz character width is smaller than the height
        app.asciiArray.append(rowList)


    # img = Image.fromarray(app.asciiArray)
    # img.show()
    # img.save('output.png')
    print("done!")