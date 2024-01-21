#!/usr/bin/env python3
""" Demo program"""

sum = 0
count = 0
file = open("data.txt")
for line in file:
  n = int(line)
  sum += n
  count += 1
print(sum/count)