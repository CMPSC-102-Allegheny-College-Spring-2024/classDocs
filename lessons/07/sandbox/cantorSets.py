#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random

myColors = mcolors.TABLEAU_COLORS
line = [0,1]
depth = 6

def divide(line, level=0):
    """ partition the lines to form the sets. """
#    thisColour = "k" # black
    thisColour = random.choice(list(myColors.values()))
    plt.plot(line,[level,level], color=thisColour, lw=5, solid_capstyle="butt")
    if level < depth:
        s = np.linspace(line[0],line[1],4)
        divide(s[:2], level+1)
        divide(s[2:], level+1)

divide(line)
plt.gca().invert_yaxis()
plt.show()