from cmu_graphics import *
from components import *
from PIL import Image, ImageDraw, ImageFont
import math
import os


def onAppStart(app):
    
    app.setMaxShapeCount(100000000000)
    app.font = 'monopspace'
    app.fontSize = 2
    app.fontColor = 'black'
    app.background = 'white'
    app.charsKeys = ["STANDARD", "BLOCKS", "BINARY", "DETAILED", "MINIMAL", "ALPHABETIC", "NUMERIC", "MATH", "SYMBOLS"]
    app.sideBarWidth = 200

    app.charWidth = app.fontSize / 2
    app.charHeight = app.fontSize

    app.imageWidth = 0
    app.imageHeight = 0

    app.uiElements = []
    app.asciiArray = []
    app.sideBar = UI_sidebar('controls', 200, app.height, 
                             app.width - 200, 0, backgroundColor= 'white', border= 'black',)
    initializeButtons(app)
    app.errorMessage = ''
    app.CMUImage = None
    app.PILImage = None

    app.exportMessage = ''
def syncImages(app, filePath: str):
    try:
        app.PILImage = Image.open(filePath)
        app.CMUImage = filePath
    except Exception as e: # this is written by claude
        app.errorMessage = str(e) + ' please try again.'

def initializeButtons(app):
    #This function is written by Claude
    def exportToPNG(outputPath=None):
        if app.asciiArray == []:
            app.exportMessage = 'Convert an image first.'
            return
        
        # Resolve output path relative to this file, not the CWD
        if outputPath is None:
            scriptDir = os.path.dirname(os.path.abspath(__file__))
            outputPath = os.path.join(scriptDir, 'output.png')
        
        rows = len(app.asciiArray)
        
        # Load a real monospace font at a readable size for export
        exportFontSize = 12
        try:
            font = ImageFont.truetype('Courier New.ttf', exportFontSize)
        except OSError:
            try:
                font = ImageFont.truetype('Menlo.ttc', exportFontSize)
            except OSError:
                font = ImageFont.load_default()
        
        # Measure actual rendered width from a full row, not a single char
        sampleRow = ''.join(app.asciiArray[0])
        imgWidth = math.ceil(font.getlength(sampleRow))
        
        # Measure line height from chars with ascenders + descenders, round up
        charBbox = font.getbbox('Mgjpq')
        lineHeight = math.ceil((charBbox[3] - charBbox[1]) * 1.2)
        
        # Extra lineHeight of padding at the bottom as a safety buffer
        imgHeight = rows * lineHeight + lineHeight
        
        canvas = Image.new('RGB', (imgWidth, imgHeight), color='white')
        draw = ImageDraw.Draw(canvas)
        
        for row in range(rows):
            rowString = ''.join(app.asciiArray[row])
            draw.text((0, row * lineHeight), rowString, fill='black', font=font)
        
        canvas.save(outputPath)
        app.exportMessage = f'Saved to {outputPath}'

    def convertButtonClick():
        imageWidth, imageHeight = setImageSize(app, app.CMUImage)
        print(f'setImageSize returned: {imageWidth}x{imageHeight}')
        # getNewImage(app, app.PILImage, imageWidth, imageHeight, inverse=False)
        app.imageArray = getNewImage(app, app.PILImage, imageWidth, imageHeight)

    # importButton = UI_Button('import', 150, 50, 
    #                         app.width / 2 - 200, app.height / 2 + 400, None,
    #                         backgroundColor='white')

    convertButton = UI_Button('CONVERT', app.sideBarWidth - 50, 40, 
                          app.width - app.sideBarWidth // 2, app.height - 130, 
                          convertButtonClick, backgroundColor='white', align = 'Left', fontColor='black', border='black', opacity= 50)

    exportButton = UI_Button('EXPORT', app.sideBarWidth - 50, 40,
                         app.width - (app.sideBarWidth// 2), app.height - 80,
                         exportToPNG, backgroundColor='white', align = 'Left', fontColor='black', border='black', opacity = 50)
    
    app.uiElements.append(convertButton)
    app.uiElements.append(exportButton)
    # def updateButtons():
    #     app.uiElements.append(convertButton)

    #     if app.asciiArray != []:
    #         app.uiElements.append(exportButton)
    #     elif (app.asciiArray != []) and (exportButton in app.asciiArray):
    #         app.uiElements.remove(exportButton)

    # updateButtons()

def image_onMousePress(app, mouseX, mouseY):
    for element in app.uiElements:
        element.onClick(mouseX, mouseY)



def start_onKeyPress(app, key):
    if key == 'i':
        filepath = app.getTextInput('Enter Box.png, Cat.jpg, or Landscape.jpeg' )
        if isinstance(filepath, str):
            app.errorMessage = ''
            syncImages(app, filepath)
            if app.errorMessage == '':
                app.asciiArray = []
                setActiveScreen('image')
        elif not isinstance(filepath, str):
            app.errorMessage = 'There was an error importing your image. Please Try Again.'

def image_onKeyPress(app, key):
    pass
            
# def onMouseDrag(app, mouseX, mouseY):
#     pass

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
    else:
        return imageWidth, imageHeight

# This function is written with the assistance of Claude, parts including charWidth and drawLabel parameters. Everything else is written by hand.
def drawAsciiImage(app, asciiArray, imageWidth, imageHeight):
    rows, cols = len(asciiArray), len(asciiArray[0])
    startingX = app.width // 2 - imageWidth // 2
    startingY = app.height // 2 - imageHeight // 2
    charWidth = (app.fontSize / 2) * cols
    charHeight = app.fontSize
    print(f'startingX: {startingX}, imageWidth: {imageWidth}')
    for row in range(rows):
        rowString = ''.join(asciiArray[row])
        drawLabel(rowString, startingX, 
                    startingY + row * charHeight, 
                    font = app.font, fill = 'black',
                    size = app.fontSize, align = 'left')
        
def start_redrawAll(app):
    if  app.errorMessage == '':
        drawLabel('press i to enter an image file path: ', app.width/2, app.height/2, size = 18, font = app.font, fill = 'black')
    else:
         drawLabel(app.errorMessage, app.width/2, app.height/2, font = app.font, fill = 'black',  size = 18)

def image_redrawAll(app):
    if app.CMUImage is None:
        drawLabel('Loading...', app.width/2, app.height/2, size=18)
        return
    app.sideBar.draw(app)
    imageWidth, imageHeight = setImageSize(app, app.CMUImage)
    if app.asciiArray == []:
        drawImage(app.CMUImage, app.width // 2, app.height // 2, width = imageWidth, 
            height = imageHeight, align='center')
    else:
        drawAsciiImage(app, app.asciiArray, imageWidth, imageHeight)
    
    if app.exportMessage != '':
        drawLabel(app.exportMessage, app.width/2, app.height - 30, fill='black', size=16, font = app.font)
def main():
    runAppWithScreens(initialScreen='start', width=1600, height=1080)

main()