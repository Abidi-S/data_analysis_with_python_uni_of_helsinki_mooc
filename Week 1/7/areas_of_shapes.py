#!/usr/bin/env python3

import math

def triangle():
    base = float(input("Give base of the triangle: "))
    height = float(input("Give height of the triangle: "))
    print(f"The area is {(base*height)/2}")

def rectangle():
    width = float(input("Give width of the rectangle: "))
    height = float(input("Give height of the rectangle: "))
    print(f"The area is {width*height}")

def circle():
    r = float(input("Give the radius of the circle: "))
    print(f"The area is {math.pi*r**2}")

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        if shape == "triangle":
            triangle()
        elif shape == "rectangle":
            rectangle()
        elif shape == "circle":
            circle()
        else:
            print("Unknown shape!")
    # enter you solution here

if __name__ == "__main__":
    main()
