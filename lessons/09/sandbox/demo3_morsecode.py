#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Code to show how to convert a dictionary to a set. We use morse code in this example as sample data in a dictionary.

# Define Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

# Create finite sets for Morse code characters
morse_code_set = set(morse_code_dict.values())
alphabet_set = set(morse_code_dict.keys())

# Display sets
print("Morse Code Set:", morse_code_set)
print("Alphabet Set:", alphabet_set)
