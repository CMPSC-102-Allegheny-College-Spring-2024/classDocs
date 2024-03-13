#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Code to demonstrate how to fine the union, intersection and difference of finite sets.

# Create finite sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Display sets
print("Set 1:", set1)
print("Set 2:", set2)

# Union of sets
union_set = set1.union(set2)
print("Union of Set 1 and Set 2:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

# Difference between sets
difference_set = set1.difference(set2)
print("Set 1 - Set 2:", difference_set)

# Check if a set is a subset or superset of another set
is_subset = set1.issubset(set2)
is_superset = set1.issuperset(set2)

print("Is Set 1 a subset of Set 2?", is_subset)
print("Is Set 1 a superset of Set 2?", is_superset)
