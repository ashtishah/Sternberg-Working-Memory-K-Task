""" KTaskTest: Execute this file to run the Sternberg 
    Working Memory K Task.
    
    Authors:
        Ashti M. Shah
        Hannah Grotzinger
        """

from __future__ import absolute_import, division, print_function
from psychopy import core, data, event, gui, logging, visual
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
import sys
import pandas as pd
import csv

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'ktask'
expInfo = {'participant' : ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if not dlg.OK:
    core.quit()  # User pressed cancel
expInfo['date'] = data.getDateStr()  # Add a simple timestamp
expInfo['expName'] = expName
expInfo['participant'] = str(expInfo['participant'])

from KTaskTools import *
"""
# Data file name stem = absolute path + name; later add .csv, .log, etc
filename = os.path.join(_thisDir, 'output',
        '%s_%s_%s'%(expInfo['participant'],expInfo['expName'],expInfo['date']))

# Save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # This outputs to the screen"""
filename=(expInfo['participant'],expInfo['expName'],expInfo['date'])

encodeLetters = []
retrievalLetters = []

# Stimuli specific to each trial
encodeLetters = [['N', 'R', 'L', 'F', 'Q'], ['L', 'F', 'B', 'S', 'M'],
    ['J', 'M', 'X', 'S', 'W', 'N', 'G'], ['G', 'M', 'F', 'W', 'X'],
    ['S', 'W', 'L'], ['R', 'Q', 'N', 'B'], ['F', 'W', 'R', 'J', 'S'],
    ['L', 'W', 'R', 'F', 'B', 'S'], ['R', 'N', 'L', 'F', 'J'],
    ['L', 'G', 'X', 'R'], ['M', 'G', 'S', 'W', 'J', 'L'], ['Q', 'R', 'W'],
    ['X', 'J', 'B', 'G', 'M', 'L'], ['G', 'X', 'F', 'N'],
    ['X', 'M', 'B', 'Q', 'F', 'J'], ['Q', 'F', 'N'],
    ['G', 'F', 'R', 'L', 'S', 'M', 'B'], ['J', 'M', 'W', 'B', 'N', 'X'],
    ['H', 'F', 'J', 'X', 'L', 'G', 'R'], ['W', 'H', 'M', 'N', 'R', 'L'],
    ['G', 'Q', 'B', 'W', 'F', 'X', 'R'], ['H', 'W', 'J'], ['G', 'R', 'M', 'J'],
    ['R', 'N', 'W', 'L', 'B', 'M', 'X'], ['W', 'H', 'Q', 'X', 'N'],
    ['Q', 'S', 'L', 'F', 'G', 'R', 'H'], ['L', 'R', 'W', 'H'],
    ['G', 'F', 'B', 'H', 'J'], ['S', 'X', 'M', 'F', 'H', 'L'],
    ['R', 'L', 'B', 'W', 'S', 'J', 'H'], ['R', 'G', 'N', 'H'], ['Q', 'H', 'N'],
    ['J', 'Q', 'R'], ['R', 'X', 'N'], ['G', 'M', 'W', 'Q']]

retrievalLetters = [['L'], ['B'], ['F'], ['J'], ['W'], ['G'], ['N'], ['M'],
    ['J'], ['F'], ['W'], ['R'], ['M'], ['N'], ['B'], ['W'], ['F'], ['L'], ['M'],
    ['G'], ['G'], ['R'], ['M'], ['J'], ['W'], ['L'], ['L'], ['M'], ['L'], ['H'],
    ['W'], ['B'], ['R'], ['X'], ['M']]

jitteredTimes = 3
demo()
print_experimenter()
run_task(encodeLetters, retrievalLetters, jitteredTimes, filename)

