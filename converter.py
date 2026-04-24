import os, sys #main os driver
from PIL import Image, ImageDraw, ImageFont #this is the pillow module for image recognition
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


def getNewImage(app, image, imageWidth, imageHeight, inverse = False):
    app.asciiArray = []
    image, DisplayImageWidth, DisplayImageHeight = modifyImage(app, image, imageWidth, imageHeight)
    for row in range(DisplayImageHeight):
        rowList = []
        for col in range(DisplayImageWidth):
            currPixel = image.getpixel((col, row))
            rowList.append(convertToAscii(currPixel, inverse = inverse) * 2) 
            #double it up, cuz character width is smaller than the height
        app.asciiArray.append(rowList)
        
    # img = Image.fromarray(app.asciiArray)
    # img.show()
    # img.save('output.png')
    print("done!")


def modifyImage(app, image, imageWidth, imageHeight):
    targetCols = int(imageWidth // (app.charWidth* 2))
    targetRows = int(imageHeight // app.charHeight)
    print(f'display: {imageWidth}x{imageHeight}, target: {targetCols}x{targetRows}, charWidth: {app.charWidth}, fontSize: {app.fontSize}')
    ...
    image = image.resize((targetCols, targetRows)).convert('L')
    imageWidth, imageHeight = image.size
    return image, imageWidth, imageHeight

#This function is written by Claude
# def exportToPNG(app, outputPath='output.png'):
#     rows, cols = len(app.asciiArray), len(app.asciiArray[0])
    
#     charWidth = app.fontSize
#     charHeight = app.fontSize * 2
    
#     imgWidth = cols * charWidth
#     imgHeight = rows * charHeight
    
#     canvas = Image.new('RGB', (imgWidth, imgHeight), color='white')
#     draw = ImageDraw.Draw(canvas)
    
#     for row in range(rows):
#         rowString = ''.join(app.asciiArray[row])
#         draw.text((0, row * charHeight), rowString, fill='black')
    
#     canvas.save(outputPath)
#     print(f'saved to {outputPath}')