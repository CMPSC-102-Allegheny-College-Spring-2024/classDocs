#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def squareArea(s: float ) -> float:
    return s*s # area of square is s*s
# end of squareArea()

def main() -> None:
    sideLength = 5
    # Testing value
    print(f"Length {sideLength}")
    print(f"  Area: {squareArea(sideLength)}")

    # These inputs work
    testValues_list =[2,0,-3,2 + 5j] 

    # why will these inputs not work?
    # testValues_list =[True, "radius"] 

    print("\n Iterating over the list.")
    for val in testValues_list: #iteration
        print(f"  Length {val},  Area: {squareArea(val)}")
# end main()

main() # call the driver function