import os, sys #main os driver
from PIL import Image #this is the pillow module for image recognition
import math
import tkinter as tk
from tkinter import filedialog

from PIL import Image

image = Image.open("CleanShot 2026-04-20 at 15.48.40@2x.png")
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

    charsKey = 'STANDARD' #place holder for dropdown menu
    chars = list(CHAR_SETS[charsKey])

    charIndex = math.floor((pixel / 255) * (len(chars) - 1)) #get it's position in the ascii art in accordance to grayscale value
    inverseCharIndex = abs(len(chars) - charIndex)
    if inverse:
        currChar = chars[inverseCharIndex]
    else:
        currChar = chars[charIndex]
    return currChar


def getNewImage(image):
    image = image.convert('L')
    width, height = image.size
    app.asciiArray = [ [ '' for _ in range(width)] for _ in range(height)]
    for row in range(height):
        for col in range(width):
            currPixel = image.getpixel((col, row))
            app.asciiArray[row][col] = convertToAscii(currPixel)

    img = Image.fromarray(res)
    img.show()
    img.save('output.png')
    print("done!")