import os, sys #main os driver
from PIL import Image #this is the pillow module for image recognition
import math
import tkinter as tk
from tkinter import filedialog

from PIL import Image

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

image = Image.open("hopper.ppm")
#open and turn grayscale


def convert(charSets, pixel, inverse = False):
    charsKey = 'STANDARD' #place holder for dropdown menu
    chars = list(CHAR_SETS[charsKey])

    charIndex = math.floor((pixel / 255) * (len(chars) - 1)) #get it's position in the ascii art in accordance to grayscale value
    inverseCharIndex = abs(len(chars) - charIndex)
    if inverse:
        currChar = chars[inverseCharIndex]
    else:
        currChar = chars[charIndex]
    return currChar


def getNewImage(charSets, image):
    image = image.convert('L')
    width, height = image.size
    res = [ [ '' for _ in range(width)] for _ in range(height)]
    for row in range(height):
        for col in range(width):
            currPixel = image.getpixel((col, row))
            res[row][col] = convert(charSets, currPixel)
    return res

    