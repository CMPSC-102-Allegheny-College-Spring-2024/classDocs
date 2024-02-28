#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# setup a python virtual environment
# python3 -m venv myVenv
# source myVenv/bin/activate
# pip install matplotlib_venn

import matplotlib.pyplot as plt
from matplotlib_venn import venn3

set1 = set(['A', 'B', 'C'])
set2 = set(['A', 'B', 'D'])
set3 = set(['A', 'E', 'F'])

venn3([set1, set2, set3], ('Group1', 'Group2', 'Group3'))

plt.show()
