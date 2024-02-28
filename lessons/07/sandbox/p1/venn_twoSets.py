#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# setup a python virtual environment
# python3 -m venv myVenv
# source myVenv/bin/activate
# pip install matplotlib_venn


import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Define the two sets
set1 = set([1, 2, 3, 4, 5])
set2 = set([3, 4, 5, 6, 7])

# Create a Venn diagram
venn2([set1, set2],('Group1', 'Group2'))

# Add a title
plt.title('Venn Diagram of Two Sets')

# Show the plot
plt.show()
