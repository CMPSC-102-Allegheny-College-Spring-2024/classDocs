#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# simple plotting tool for frequencies of characters in a string
import matplotlib.pyplot as plt
from pylab import plot, show, title, savefig, xlabel, ylabel, legend

s_str = "hello" # string to study
# s_str = "Python is developed under an OSI-approved open source license, making it freely usable and distributable, even for commercial use. Python's license is administered by the Python Software Foundation."
sCount_dict = {} # save the counts here

# count the letters in the word
for i in s_str:
    if i not in sCount_dict:
        sCount_dict[i] = 1 # add the char to the dictionary with count of one
    else: # this char is already in the dictionary
        sCount_dict[i] = sCount_dict[i] + 1

print(f" Character Counts: {sCount_dict}")

freq_list = [] # list of the frquencies for the chars
for i in sCount_dict:
    freq_list.append(sCount_dict[i]/len(s_str))

print(f" Frequencies: {freq_list}")

y = freq_list
x = [i for i in range(len(freq_list))]
plot(x,y, marker = 'o')
plt.title("Probability")
plt.ylabel('Magnitude')
plt.xlabel('Frequency')
plt.savefig('frequencyPlot.png')
# show()
