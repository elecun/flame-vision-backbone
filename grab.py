'''
Multiple Basler Camera Grabber
'''

import os

os.environ["PYLON_CAMEMU"] = "3"
from pypylon import genicam
from pypylon import pylon
import sys

maxCamerasToUse = 2

if __name__ == "__main__":
    pass