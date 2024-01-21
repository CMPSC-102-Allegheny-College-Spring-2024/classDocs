import math, random
# make a data file: 
# Unix command: python3 makeRandomNumbers.py > data_i.txt
for i in range(100): print(f"{math.floor(random.random()*15 + 1)}")