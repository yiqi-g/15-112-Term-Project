
import os, sys #main os driver

from cmu_graphics import *
from cmu_cpcs_utils import *

import model
import view
import controller
import math

from PIL import Image #this is the pillow module for image recognition



def main():
    runApp(width = view.newWindow.width, height = view.newWindow.width)

main()