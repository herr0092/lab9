# Fernando Herrera - 040960796
#   Library

import time
import random
from gfxhat import lcd, backlight, fonts
import math

from PIL import Image, ImageFont, ImageDraw
import subprocess as sp

# Sleep 
def dormir( segs = 0.02 ):
    time.sleep(segs)


# Function to print some label
def printTitle( message ):
    print('=====================')
    print(' ' + message )
    print('=====================')


# Function to calculate area
# @radius: int - radius of the circle
def calculateArea( radius ):
    area = math.pi * ( radius * radius)
    return area

# Function to calculate MPG
# m: float = minimun
# g: float = galons
def calculateMPG(m, g):
    mpg =  round(m / g, 2)
    return mpg

# Function to calculate MPG
# f: float = fahrenheit temperature
def calculateCelsius( f ):
    c = round( ( f - 32 ) * (5/9), 2)
    return c

# Calculate distance between two points
# x1,x2, y1, y2 MOST be integer values
def calculateDistanceBetweenPoints(x1,y1,x2,y2):
    xDistance = x1 - x2
    yDistance = y1 - y2
    a2 = xDistance ** 2
    b2 = yDistance ** 2

    return math.sqrt( a2 + b2 )



def clearConsole():
    sp.call('clear',shell=True)

def showMenu():
    clearConsole()

    print('''
-=-=-=-=- Welcome =-=-=-=-
-     Choose wisely!     -
=                        =
-  1- Horizontal line    -
=  2- Vertical line      =
-  3- Basic Staircase    -
=  4- Custom Staricase   =
-  5- Random pixel       -
=                        =
-  0- Clear and Exit     -
=                        = 
-=-=-=-=-=-=-=-=-=-=-=-=-=
''')


def clearScreen():
    lcd.clear()
    lcd.show()
    backlight.set_all(200, 200, 200)
    backlight.show()

def rainbowFinish():
    for i in range(0,100): 
        setBgColor(255, 17, 0)
        setBgColor(255, 248, 1)
                    
def clearBacklight():
    setBgColor(0,0,0)

# Change the bgcolor
def setBgColor(r,g,b):
    backlight.set_all(r, g, b)
    backlight.setup()
    backlight.show()

def setRedBG():
    setBgColor(205, 36, 0)

def setGreenBG():
    setBgColor(27, 203, 26)

def randomBgColor():
    r = random.randint(100,255)
    g = random.randint(100,255)
    b = random.randint(100,255)
    backlight.set_all(r, g, b)
    backlight.show()


# Creates a vertical line at given x coordinate
def verticalLine( x ):
    setRedBG()
    for i in range(0,63):
        lcd.set_pixel(x, i, 1)
        lcd.show()
        time.sleep(0.02)

    setGreenBG()
    

#Creates a horizontal line at given y coordinate
def horizontalLine( y ):
    setRedBG()
    for i in range(0, 127):
        lcd.set_pixel(i, y, 1)
        lcd.show()
        time.sleep(0.02)

    setGreenBG()

# Default staircase
def defaultStaircase():
    staircase(30, 63, 5, 5)

# Creates a staircase
def staircase(x, y, w, h):
    # x = 30
    # y = 63
    
    setRedBG()
    while x < 127 and y >= 0:

        for i in range(0, w):
            x = x + 1
            if ( x > 127 ): 
                break

            lcd.set_pixel(x, y, 1)
            lcd.show()
        
        for i in range(0,h):
            y = y - 1
            if ( y < 0 ): 
                break
            lcd.set_pixel(x, y, 1)
            lcd.show()
    
    
    # lcd.show()

    setGreenBG()


# Displays a random pixel for X seconds
def randomPixel(t):

    now  = int(round(time.time() * 1000))
    exit = now + (t * 1000)

    while now <= exit:
        x = random.randint(0, 127)
        y = random.randint(0, 63)
        setPixel( x,y, 1 )
        
        now = int(round(time.time() * 1000))

        # setBgColor(40, 56, 142)
        setRedBG()
        setGreenBG()
        setRedBG()
        setBgColor(200,200,200)
    

def setPixel( x, y, on ):
    lcd.set_pixel(x, y, on)
    lcd.show()




# From ============ Lab 6 ---- task 1

# This function displays a given text to the screen
def displayText(text,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 


# Lab 6 ===== Task 2

def displayObject(obj, coorX, coorY):

    x = coorX # -1
    y = coorY # -1

    # Validations
    if ( (coorX + len(obj[0])) > 127 ):
        print('Not enough space to draw in X:{} coordinate'.format(coorX))
        print('Changing X value to 0');
        # coorX = -1
        coorX = 127 - len(obj[0])
    
    if ( coorY + len(obj) > 62 ):
        print('Not enough space to draw in Y:{} coordinate'.format(coorY))
        print('Changing X value to 0');
        y = 63 - len(obj)


    setRedBG()
    

    for line in obj:
        y = y + 1
        x = coorX

        for val in line:
            x = x + 1
            # print('x: {} y: {} val: {} \n'.format(x,y, val))
            setPixel( x, y, val )
    
    setGreenBG()


# Display an object as fast as possible
def displayObjectNoAnimation(obj, coorX, coorY, off = False):
    
    x = coorX # -1
    y = coorY # -1

    # Validations
    if ( (coorX + len(obj[0])) > 127 ):
        # coorX = -1
        coorX = 127 - len(obj[0])
    
    if ( coorY + len(obj) > 62 ):
        y = 63 - len(obj)


    for line in obj:
        y = y + 1
        x = coorX

        for val in line:
            x = x + 1
            if ( off ):
                val = 0

            lcd.set_pixel(x, y, val)
    
    lcd.show()



# LAB 7 =====================

def eraseObject(obj,x=0,y=0):
    displayObjectNoAnimation(obj, x, y, True )

def moveObject(obj,x=0,y=0,vx=0,vy=0):
    eraseObject(obj, x, y)
    displayObjectNoAnimation( obj, x+vx, y+vy )
    return x+vx, y+vy

# Returns (TRUE, TRUE), if both coordinates collide 
def checkCollision(obj,x=0,y=0,vx=0,vy=0,Sx=128,Sy=64):
    objHeight = len( obj ) + 1
    objWidth  = len( obj[0] )

    if ( ( x + objWidth + vx ) >= Sx ):
        # print('collition in X')
        return True, False
    
    if ( ( y + objHeight + vy ) >= Sy ):
        # print('collition in Y')
        return False, True
    
    if ( x <= 0 ):
        # print('collition in x')
        return True, False
    
    if ( y <= 0 ):
        # print('collition in Y')
        return False, True

    # print('no collition')
    return False, False
        
