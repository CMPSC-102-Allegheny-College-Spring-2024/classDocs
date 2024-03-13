#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A complicated example to convert multiple dictionaries to sets or lists. The example demonstrates how the order of elements is not conserved in sets. For example, we prepare two sets from dictionaries which are not in alignment. We show that two lists do contain their alignments.

def dictKeysToSet(in_dic:dict, in_set:set) -> set:
    """ Function to strip away the keys and values of a dictionary."""
    for i in in_dic.keys():
        in_set.add(i)
    return in_set
# end of dictKeysToSet()

def dictValuesToSet(in_dic:dict, in_set:set) -> set:
    """ Function to strip away the keys and values of a dictionary."""
    for i in in_dic.values():
        in_set.add(i)
    return in_set
# end of dictValuesToSet()

def dictKeysToList(in_dic:dict, in_list:list) -> list:
    """ Function to strip away the keys and values of a dictionary."""
    for i in in_dic.keys():
        in_list.append(i)
    return in_list
# end of dictKeysToSet()

def dictValuesToList(in_dic:dict, in_list:list) -> list:
    """ Function to strip away the keys and values of a dictionary."""
    for i in in_dic.values():
        in_list.append(i)
    return in_list
# end of dictValuesToSet()


# add several different dictionaries to a single set

# Define Morse code dictionaries
morse_code_AH_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....'}
morse_code_IP_dict = {'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.'}
morse_code_QZ_dict = {'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
morse_code_09_dict = {'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....','6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}



print(f"  A through H: {morse_code_AH_dict}")
print(f"  I through P: {morse_code_IP_dict}")
print(f"  Q through Z: {morse_code_QZ_dict}")
print(f"  0 through 9: {morse_code_09_dict}")

print("----------------------")

### SETS ####

### A through H
print("Breaking apart the dictionary into two separate dictionaries")
morse_code_values_set = set()
myValues_set = dictValuesToSet(morse_code_AH_dict, morse_code_values_set)
print(f"\t myValues_set -> {myValues_set}")

morse_code_keys_set = set()
mykeys_set = dictKeysToSet(morse_code_AH_dict, morse_code_keys_set)
print(f"\t mykeys_set -> {mykeys_set}")


### I through P
myValues_set = dictValuesToSet(morse_code_IP_dict, morse_code_values_set)
print(f"\t myValues_set -> {myValues_set}")

mykeys_set = dictKeysToSet(morse_code_IP_dict, morse_code_keys_set)
print(f"\t mykeys_set -> {mykeys_set}")

### Q through Z
myValues_set = dictValuesToSet(morse_code_QZ_dict, morse_code_values_set)
print(f"\t myValues_set -> {myValues_set}")

mykeys_set = dictKeysToSet(morse_code_QZ_dict, morse_code_keys_set)
print(f"\t mykeys_set -> {mykeys_set}")

### 0 through 9
myValues_set = dictValuesToSet(morse_code_09_dict, morse_code_values_set)
print(f"\t myValues_set -> {myValues_set}")

mykeys_set = dictKeysToSet(morse_code_09_dict, morse_code_keys_set)
print(f"\t mykeys_set -> {mykeys_set}")

print("Notice how the order between both sets may not have been conserved? Unless we know the keys and values, we might never know about this restructuring of our data.")

print("----------------------")


### LISTS ####

### A through H
print("Breaking apart the dictionary into two separate dictionaries")
morse_code_values_list= list()
myValues_list = dictValuesToList(morse_code_AH_dict, morse_code_values_list)
print(f"\t myValues_list -> {myValues_list}")

morse_code_keys_list = list()
mykeys_list = dictKeysToList(morse_code_AH_dict, morse_code_keys_list)
print(f"\t mykeys_list -> {mykeys_list}")

# ### I through P
print("Breaking apart the dictionary into two separate dictionaries")
morse_code_values_list= list()
myValues_list = dictValuesToList(morse_code_IP_dict, morse_code_values_list)
print(f"\t myValues_list -> {myValues_list}")

morse_code_keys_list = list()
mykeys_list = dictKeysToList(morse_code_IP_dict, morse_code_keys_list)
print(f"\t mykeys_list -> {mykeys_list}")

# ### Q through Z
print("Breaking apart the dictionary into two separate dictionaries")
morse_code_values_list= list()
myValues_list = dictValuesToList(morse_code_QZ_dict, morse_code_values_list)
print(f"\t myValues_list -> {myValues_list}")

morse_code_keys_list = list()
mykeys_list = dictKeysToList(morse_code_QZ_dict, morse_code_keys_list)
print(f"\t mykeys_list -> {mykeys_list}")

# ### 0 through 9
print("Breaking apart the dictionary into two separate dictionaries")
morse_code_values_list= list()
myValues_list = dictValuesToList(morse_code_09_dict, morse_code_values_list)
print(f"\t myValues_list -> {myValues_list}")

morse_code_keys_list = list()
mykeys_list = dictKeysToList(morse_code_09_dict, morse_code_keys_list)
print(f"\t mykeys_list -> {mykeys_list}")
print("Notice how the order between both sets has been conserved?")

