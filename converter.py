import os, sys #main os driver
from PIL import Image #this is the pillow module for image recognition
import math
import tkinter as tk
from tkinter import filedialog

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

class Pixel:

def convert(charSets, pixel, inverse = False):
    charsKey = 'STANDARD' #place holder for dropdown menu
    chars = list(CHAR_SETS[charSetKey])

    charIndex = math.floor((pixel / 255) * (len(chars) - 1)) #get it's position in the ascii art in accordance to grayscale value
    inverseCharIndex = abs(len(chars) - charIndex)
    if inverse:
        currChar = chars[inverseCharIndex]
    else:
        currChar = chars[charIndex]
    return currChar


def getNewImage(charSets, image):
    rows, cols = #get image rows, #get image cols
    res = [ [ '' for _ in range(cols)] for _ in range(rows)]
    for row in rows:
        for col in cols:
            currPixel = # get image pixel value
            newPixel = convert(charSets, pixel)
            res[row][col] = newPixel
    return res

    